from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('dashboard/', views.dashboardView, name="dashboard"), # Original
    path('dashboard/api/ano/', views.DashboardView.ques_1, name="ano"),
    # path('dashboard/chart', views.ChartData.get, name="chart"),

    path('', views.indexView, name="home"),
    path('register/', views.registerView, name="register_url"),
    path('login/', LoginView.as_view(), name="login_url"),
    path('logout/', LogoutView.as_view(next_page="dashboard"), name="logout"),
]