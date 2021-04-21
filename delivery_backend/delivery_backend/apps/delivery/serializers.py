from rest_framework import serializers
from delivery_backend.apps.delivery.models import QueryResponse, QueryRequest


class QueryResponseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QueryResponse
        fields = ['location_from', 'location_to', 'distance']


class QueryRequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QueryRequest
        fields = ['location_from', 'location_to']
