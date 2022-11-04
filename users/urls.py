from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import UserRegistrationView , UserLoginView , SendPasswordResetEmailView, UserChangePasswordView, UserLoginView, UserProfileView, UserRegistrationView, UserPasswordResetView 

urlpatterns = [
    path('register' , UserRegistrationView.as_view()),
    path('login' , UserLoginView.as_view()),
    path('profile', UserProfileView.as_view(), name='profile'),
    path('changepassword', UserChangePasswordView.as_view(), name='changepassword'),
    path('send-reset-password-email', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>', UserPasswordResetView.as_view(), name='reset-password'),
]
