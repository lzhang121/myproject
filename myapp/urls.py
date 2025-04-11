from django.urls import path
from . import views

urlpatterns = [
    path('api/hello/', views.api_hello),
]
