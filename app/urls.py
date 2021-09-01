from django.urls import path
from . import views


urlpatterns = [
    path('pokemons/', views.PokeList.as_view(), name="pokemons"),
    path('pokemons/<str:pk>/', views.SinglePoke.as_view(), name="pokemons"),
]