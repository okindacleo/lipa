
from django.contrib import admin
from django.urls import path, include

from mpesa.api.views import LNMCallbackUrlAPIView,TransStatusResultCallbackurlAPIView,TransStatusTimeoutCallbackurlAPIView,ReversalResultCallbackUrlAPIView,ReversalTimeoutCallbackUrlAPIView,BillManagerOptinCallbackUrlAPIView



urlpatterns = [
    
    path("lnm/", LNMCallbackUrlAPIView.as_view(), name="lnm-callbackurl" ),

    path("trans_status/result/", TransStatusResultCallbackurlAPIView.as_view(), name="trans-status-result" ),
    path("trans_status/timeout/", TransStatusTimeoutCallbackurlAPIView.as_view(), name="trans-status-timeout" ),

    path("reversal/result/", ReversalResultCallbackUrlAPIView.as_view(), name='reversal-result'),
    path("reversal/timeout/", ReversalTimeoutCallbackUrlAPIView.as_view(), name='reversal-timeout'),

    path("bill_manager_optin/result/", BillManagerOptinCallbackUrlAPIView.as_view(), name='bill_manager-result'),



]














"""
from django.contrib import admin
from django.urls import path, include
from mpesa.api.views import LNMCallbackUrlAPIView,C2BValidationAPIView,C2BConfirmationAPIView 


urlpatterns = [
    path("lnm/", LNMCallbackUrlAPIView.as_view(), name="lnm-callbackurl"),
    path("c2b-validation/", C2BValidationAPIView.as_view(), name="c2b-validation"),
    path("c2b-confirmation/", C2BConfirmationAPIView.as_view(), name="c2b-confirmation"),


    ]

"""