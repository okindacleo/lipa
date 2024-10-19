

from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.mpesa_pay, name='mpesapay'),
    path('c2b/', views.c2b_pay, name='c2b-mpesapay'),
    path('transaction_status/', views.transaction_status, name='transaction-status'),
    path('reversal/', views.initiate_reversal, name='reverse-transaction'),
    
]
