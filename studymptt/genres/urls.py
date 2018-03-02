from django.urls import path

from genres.views import GenreListView, GenreCreateView, GenreDeleteView, GenreDetailView

app_name = 'genres'
urlpatterns = [
    path('', GenreListView.as_view(), name='list'),
    path('create/', GenreCreateView.as_view(), name='create'),
    path('<int:pk>/', GenreDetailView.as_view(), name='detail'),
    path('<int:pk>/delete/', GenreDeleteView.as_view(), name='delete'),
]