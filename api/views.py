from rest_framework.generics import ListAPIView
from .serializers import RestaurantSerializer
from restaurants.models import Restaurant


class RestaurantListView(ListAPIView):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()
