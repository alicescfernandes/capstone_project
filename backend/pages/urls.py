from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('api/quarters/', views.QuarterListAPIView.as_view(), name='quarter-list'),
] 