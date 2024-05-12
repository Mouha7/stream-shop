from django.urls import path
from . import views

ROUTE = "gender"

urlpatterns = [
    path('<int:id>/', views.gender_list, name=f"{ROUTE}_list"),
    path('detail/<int:id>/', views.gender_detail, name=f"{ROUTE}_detail"),
    path('add/', views.gender_add, name=f"{ROUTE}_add"),
    path('edit/<int:id>/', views.gender_edit, name=f"{ROUTE}_edit"),
    path('delete/<int:id>/', views.gender_delete, name=f"{ROUTE}_delete")
]