from django.urls import path
from .views import *

urlpatterns = [
    path('addReview' ,MakeReview.as_view())
]
