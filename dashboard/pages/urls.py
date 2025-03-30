from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('charts/<str:section>/<str:quarter>/', views.charts, name='charts'),
] 