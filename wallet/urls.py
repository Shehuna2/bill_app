from django.urls import path
from . import views

urlpatterns = [
    path("deposit/", views.deposit_view, name="wallet_deposit"),
    path("deposit/verify/", views.verify_deposit_view, name="wallet_verify"),
    path("dashboard/", views.wallet_dashboard, name="wallet_dashboard"),
]
