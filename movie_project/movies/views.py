from django.shortcuts import render #se usa para las plantillas

from rest_framework import generics #Vistas genéricas de Django Rest Framework
from django.views.generic import ListView, DetailView #Vistas genéricas de Django
from .models import Director, Movie
from .serializers import DirectorSerializer, MovieSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#Vistas genéricas de Django para Director (Dejo las plantillas comentadas para ser agregadas después)
class DirectorListView(ListView):
    model = Director
    template_name = 'director_list.html'
    context_object_name = 'directors'
    
class DirectorDetailView(DetailView):
    model = Director
    template_name = 'director_detail.html'
    context_object_name = 'director' 

#Vistas genéricas de DRF para Director
class DirectorListCreateView(generics.ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    
class DirectorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    

#Vistas genéricas de Django para Movie
class MovieListView(ListView):
    model = Movie
    template_name = 'movie_list.html'
    context_object_name = 'movies'

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie_detail.html'
    context_object_name = 'movie'

#Vistas genéricas de DRF para Movie    
class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


#Vista basada en función extendida mediante decorador
@api_view(['GET'])
def movies_by_director(request, director_id):
    try:
        director = Director.objects.get(pk=director_id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #movies = Movie.objects.filter(director=director)
    
    # Lo anterior pero usando related_name (movies), expresado en la foreign key director
    movies = director.movies.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)   