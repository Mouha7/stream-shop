from django.urls import path
from . import views

ROUTE = "movie"

urlpatterns = [
    path('', views.movie_list, name=f"{ROUTE}_list"),
    path('detail/<int:id>/', views.movie_detail, name=f"{ROUTE}_detail"),
    path('add/', views.movie_add, name=f"{ROUTE}_add"),
    path('edit/<int:id>/', views.movie_edit, name=f"{ROUTE}_edit"),
    path('delete/<int:id>/', views.movie_delete, name=f"{ROUTE}_delete")
]