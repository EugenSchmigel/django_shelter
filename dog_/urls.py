from django.urls import path
from django.views.decorators.cache import cache_page

from dog_ import views
from dog_.views import IndexView, CategoryListView, DogListView, DogCreateView, DogUpdateView, DogDeleteView
from dog_.apps import DogConfig

app_name = DogConfig.name


urlpatterns = [
    # path('', IndexView.as_view(), name='index'),
    path("", cache_page(60)(views.IndexView.as_view()), name="index"),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('dogs/<int:pk>/', DogListView.as_view(), name='category'),
    path('dogs/create/', DogCreateView.as_view(), name='dog_create'),
    path('dogs/update/<int:pk>/', DogUpdateView.as_view(), name='dog_update'),
    path('dogs/delete/<int:pk>/', DogDeleteView.as_view(), name='dog_delete'),
]

