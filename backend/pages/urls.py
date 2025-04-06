from django.urls import path
from . import views
from . import api_views



urlpatterns = [
    path('', views.home, name='home'),
    path('api/quarters/', api_views.QuarterListAPIView.as_view(), name='quarter-list'),
    path('api/chart/', api_views.ChartDataAPIView.as_view(), name='quarter-list'),

] 