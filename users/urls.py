from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import RegisterView

router = DefaultRouter()

router.register('register', RegisterView, basename='register')

urlpatterns = [
    path('', include(router.urls)),
]