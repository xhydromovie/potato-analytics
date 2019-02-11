from django.urls import path
from . import views

app_name = "potatoes"

urlpatterns = [
    path('', views.index, name='index'),
]