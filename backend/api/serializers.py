from rest_framework import serializers

class RouteSerializer(serializers.Serializer):
	routes = serializers.CharField(required=True, max_length=10)
