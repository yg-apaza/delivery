from django.http import JsonResponse
from geopy.exc import GeocoderTimedOut
from rest_framework.decorators import action

from delivery_backend.apps.delivery.models import QueryResponse
from delivery_backend.apps.delivery.serializers import QueryResponseSerializer, QueryRequestSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from geopy.geocoders import Nominatim


class QueryResponseViewSet(viewsets.mixins.ListModelMixin,
                           viewsets.GenericViewSet):

    queryset = QueryResponse.objects.all()
    serializer_class = QueryResponseSerializer
    geoLocator = Nominatim(user_agent="delivery-spike")

    @action(methods=['post'], detail=False)
    def distance(self, request):
        serializer = QueryRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        location_from = request.data.get('location_from')
        location_to = request.data.get('location_to')
        try:
            approximate_location_from = self.geoLocator.geocode(location_from).address
            approximate_location_to = self.geoLocator.geocode(location_to).address
        except GeocoderTimedOut as e:
            return JsonResponse({'message': e.message}, status=status.HTTP_504_GATEWAY_TIMEOUT)
        query_response = QueryResponse(location_from=approximate_location_from,
                                       location_to=approximate_location_to,
                                       distance=1)
        serializer = QueryResponseSerializer(data=query_response.__dict__)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED, content_type='application/json')
