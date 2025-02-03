from django.urls import path
from .views import index, hello_world, bad_request  # Importing views from views.py

urlpatterns = [
    path('', index, name='index'),
    path('hello/', hello_world, name='hello_world'),
    path('bad/', bad_request, name='bad_request'),
]
