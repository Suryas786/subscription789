from django.urls import path
from . import views

urlpatterns = [
    path("", views.subscribe_page, name="subscribe"),
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("pay/", views.create_checkout, name="pay"),
    path("success/", views.payment_success, name="success"),
    path("error/", views.payment_error, name="error"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("pay/", views.create_checkout, name="process_payment")
]
