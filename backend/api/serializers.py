from rest_framework import serializers

class RouteSerializer(serializers.Serializer):
	routes = serializers.CharField(required=True, max_length=10)


class RoutesStopidSerializer(serializers.Serializer):
    stop_id = serializers.CharField(max_length=12)
    stop_name = serializers.CharField(max_length=100)
    stop_lat = serializers.DecimalField(max_digits=25, decimal_places=20)
    stop_long = serializers.DecimalField(max_digits=25, decimal_places=20)
    true_stop_id = serializers.IntegerField()


class CoreUsersettingsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    routeid = serializers.CharField(max_length=20)
    direction_id = serializers.CharField(max_length=10)
    direction_name = serializers.CharField(max_length=40)
    originstop_id = serializers.CharField(max_length=10)
    originstop_name = serializers.CharField(max_length=40)
    destinationstop_id = serializers.CharField(max_length=10)
    destinationstop_name = serializers.CharField(max_length=50)
    journeyname = serializers.CharField(max_length=20)
    userid = serializers.CharField(max_length=10)