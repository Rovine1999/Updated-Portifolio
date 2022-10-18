from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('project/preview/<int:pk>/', projectview, name='projectpreview'),
    path('contact/', message, name='contact'),
]
