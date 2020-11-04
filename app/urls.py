from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clicked_button', views.clicked_button, name='clicked_button')
]