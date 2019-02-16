from django.urls import path
from . import views

app_name = "potatoes"

urlpatterns = [
    path('igrit/', views.igrit_chart, name='igrit'),
    path('sell/', views.igrit_chart, name='igrit'),
    path('display/', views.display_chart, name='display'),
]