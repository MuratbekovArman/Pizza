from django.urls import path
from api.views import *

urlpatterns = [
    path('restaurants/', RestaurantListAPIView.as_view()),
    path('restaurants/<int:pk>', RestaurantDetailAPIView.as_view()),
    path('pizzas/', PizzaListAPIView.as_view()),
    path('pizzas/<int:pk>', PizzaDetailAPIView.as_view())
]