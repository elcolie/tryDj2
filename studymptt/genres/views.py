from django.shortcuts import render
from django.views.generic import ListView

from genres.models import Genre


class GenreListView(ListView):
    model = Genre
    template_name = 'genre_list.html'

