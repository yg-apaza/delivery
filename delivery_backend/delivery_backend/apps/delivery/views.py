from django.http import JsonResponse
from geopy.exc import GeocoderTimedOut
from rest_framework.decorators import action
from delivery_backend.apps.delivery.models import QueryResponse
from delivery_backend.apps.delivery.serializers import QueryResponseSerializer, QueryRequestSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from geopy.geocoders import Nominatim
import math


class QueryResponseViewSet(viewsets.mixins.ListModelMixin,
                           viewsets.GenericViewSet):

    queryset = QueryResponse.objects.all()
    serializer_class = QueryResponseSerializer
    geoLocator = Nominatim(user_agent='delivery-spike')

    @action(methods=['post'], detail=False)
    def distance(self, request):
        serializer = QueryRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        location_from = request.data.get('location_from')
        location_to = request.data.get('location_to')
        try:
            approximate_location_from = self.geoLocator.geocode(location_from)
            approximate_location_to = self.geoLocator.geocode(location_to)
        except GeocoderTimedOut as e:
            return JsonResponse({'message': e.message}, status=status.HTTP_504_GATEWAY_TIMEOUT)

        if approximate_location_from is None or approximate_location_to is None:
            return JsonResponse({'message': 'Invalid addresses. Couldn\'t find an approximate address'},
                                status=status.HTTP_400_BAD_REQUEST)

        distance = QueryResponseViewSet.calculate_distance(approximate_location_from, approximate_location_to)
        query_response = QueryResponse(location_from=approximate_location_from.address,
                                       location_to=approximate_location_to.address,
                                       distance=int(distance))
        serializer = QueryResponseSerializer(data=query_response.__dict__)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED, content_type='application/json')

    @staticmethod
    def calculate_distance(from_address, to_address):
        earth_radius = 6373.0
        lat1 = math.radians(from_address.latitude)
        lon1 = math.radians(from_address.longitude)
        lat2 = math.radians(to_address.latitude)
        lon2 = math.radians(to_address.longitude)
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = earth_radius * c
        return distance
