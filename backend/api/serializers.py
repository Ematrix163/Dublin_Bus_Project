from rest_framework import serializers

class RouteSerializer(serializers.Serializer):
	routes = serializers.CharField(required=True, max_length=10)


class RoutesStopidSerializer(serializers.Serializer):
    stop_id = serializers.CharField(max_length=12)
    stop_name = serializers.CharField(max_length=100)
    stop_lat = serializers.DecimalField(max_digits=25, decimal_places=20)
    stop_long = serializers.DecimalField(max_digits=25, decimal_places=20)
    true_stop_id = serializers.IntegerField()
    busroute = serializers.CharField(max_length=15)

class StopInfoSerializer(serializers.Serializer):
    stop_name = serializers.CharField(max_length=100)
    true_stop_id = serializers.IntegerField()
    stop_lat = serializers.DecimalField(max_digits=25, decimal_places=20)
    stop_long = serializers.DecimalField(max_digits=25, decimal_places=20)
    stop_id = serializers.CharField(max_length=12)