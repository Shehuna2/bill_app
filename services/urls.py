from django.urls import path
from . import views

urlpatterns = [
    path('purchase/<int:service_id>/', views.purchase_service, name='purchase_service'),
    path('history/', views.purchase_history, name='purchase_history'),
]
