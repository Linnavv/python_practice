from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:pokemon_id>/', views.delete_pokemon, name='delete_pokemon'),
    path('battle/', views.battle, name='battle'),
]
