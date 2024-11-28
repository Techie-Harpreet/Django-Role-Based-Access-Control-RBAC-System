from django.urls import path
from .views import RegisterUser, user_login, dashboard, logout_view

urlpatterns = [
    # path('', Dashboard, name="home"),
    path('register/', RegisterUser, name="register"),
    path('login/', user_login, name="login"),
    path('', dashboard, name="home"),
    path('logout/', logout_view, name='logout'),


]
