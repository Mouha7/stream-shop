from django.urls import path
from . import views

ROUTE = "serie"

urlpatterns = [
    path('', views.serie_list, name=f"{ROUTE}_list"),
    path('detail/<int:id>/', views.serie_detail, name=f"{ROUTE}_detail"),
    path('add/', views.serie_add, name=f"{ROUTE}_add"),
    path('edit/<int:id>/', views.serie_edit, name=f"{ROUTE}_edit"),
    path('delete/<int:id>/', views.serie_delete, name=f"{ROUTE}_delete")
]