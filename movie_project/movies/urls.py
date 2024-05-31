from django.urls import path
from .views import (
    DirectorListCreateView,
    DirectorRetrieveUpdateDestroyView,
    MovieListCreateView,
    MovieRetrieveUpdateDestroyView,
    DirectorListView,
    DirectorDetailView,
    MovieListView,
    MovieDetailView,
    movies_by_director
)

urlpatterns = [
    # paths vistas genéricas DRF
    path('drf/directors/', DirectorListCreateView.as_view(), name='director-list-create'),
    path('drf/directors/<int:pk>/', DirectorRetrieveUpdateDestroyView.as_view(), name='director-detail'),
    path('drf/movies/', MovieListCreateView.as_view(), name='movie-list-create'),
    path('drf/movies/<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(), name='movie-detail'),
    
    # paths vistas genéricas Django 
    path('d/directors/', DirectorListView.as_view(), name='director2-list'),
    path('d/directors/<int:pk>/', DirectorDetailView.as_view(), name='director2-detail'),
    path('d/movies/', MovieListView.as_view(), name='movie2-list'),
    path('d/movies/<int:pk>/', MovieDetailView.as_view(), name='movie2-detail'),
    
    # path vista API view
    path('directors/<int:director_id>/movies/', movies_by_director, name='movies-by-director'),
]