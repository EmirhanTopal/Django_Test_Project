from django.urls import path
from . import views

urlpatterns = [
    #path("maserati", views.ft_index, {"message": "maserati"}),
    #path("NissanR34", views.ft_index, {"message": "R34"})
    path("<int:cars>", views.ft_general_cars_by_number),
    path("<str:cars>", views.ft_general_cars, name="all-cars")
]