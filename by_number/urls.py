from django.urls import path
from .views import auth_code, auth_phone, profile

urlpatterns = [
    path('profile/<str:phone_number>', profile, name='profile'),
    path('auth/', auth_phone, name='auth_phone'),
    path('auth/<str:phone_number>', auth_code, name='auth_code'),
]
