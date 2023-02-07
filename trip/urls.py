from django.urls import path
from .views import *

urlpatterns = [
    path('request' , MakeTrip.as_view()),
    
]
