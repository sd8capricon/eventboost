from django.urls import path
from accounts import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register_user/", views.register_user, name="signup"),
    path("login_user/", views.login_user, name="login"),
    path("logout_user/", views.logout_user, name="logout"),
]
