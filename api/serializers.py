from rest_framework.serializers import ModelSerializer
from restaurants.models import Restaurant


class RestaurantSerializer(ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [
            'name',
            'opening_time',
            'closing_time',
        ]
