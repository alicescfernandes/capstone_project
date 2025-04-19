from django.urls import path
from . import views
from . import api_views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/quarters/', api_views.QuarterListAPIView.as_view(), name='api_quarter'),
    path('api/chart/', api_views.ChartDataAPIView.as_view(), name='api_chart'),
    path('quarters/edit/<uuid:uuid>/', views.edit_quarter, name='edit_quarter'),
    path('quarters/delete/<uuid:uuid>/', views.delete_quarter, name='delete_quarter'),
    path('quarters/', views.manage_quarters, name='manage_quarters'),
    path('quarters/files/delete/<uuid:uuid>/', views.delete_file, name='delete_file'),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
] 