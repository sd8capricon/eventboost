from django.urls import path
from accounts import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.register_user, name="signup"),
    path("login/", views.login_user, name="login"),
    path("logout_user/", views.logout_user, name="logout"),
]
