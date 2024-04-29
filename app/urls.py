from django.urls import path
from app import views

urlpatterns = [
    path('', views.indexView.as_view(), name='index'),
]


