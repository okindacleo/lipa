from rest_framework.generics import CreateAPIView

from rest_framework.permissions import AllowAny

from mpesa.models import LNMPOnline
from mpesa.api.serializers import LNMOnlineSerializer

class LNMCallbackUrlAPIView(CreateAPIView):
    queryset = LNMPOnline.objects.all()
    serializer_class = LNMOnlineSerializer
    permission_classes = [AllowAny]
    

    def create(self, request):
        print('THIS IS REQUEST.DATA', request.data)

        merchant_request_id = request.data["Body"]["stkCallback"]["MerchantRequestID"]
        checkout_request_id = request.data["Body"]["stkCallback"]["CheckoutRequestID"]
        resultcode = request.data["Body"]["stkCallback"]["ResultCode"]
        resultdesc = request.data["Body"]["stkCallback"]["ResultDesc"]
        amount = request.data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][0]["Value"]
        mpesa_receipt_number = request.data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][1]["Value"]
        balance = ""
        transaction_date = request.data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][3]["Value"]
        phone_number = request.data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][4]["Value"]
        
        from datetime import datetime
        str_tranasaction_date = str(transaction_date)
        transaction_datetime = datetime.strptime(str_tranasaction_date, '%Y%m%d%H%M%S')


        import pytz
        aware_transaction_datetime = pytz.utc.localize(transaction_datetime)
        print(transaction_datetime, 'this should be an AWARE_TRANSACTION_DATETIME')

        
        from mpesa.models import LNMPOnline

        my_model = LNMPOnline.objects.create(
            CheckoutRequestID=checkout_request_id, 
            MerchantRequestID=merchant_request_id,
            ResultCode=resultcode,
            ResultDesc=resultdesc,
            Amount=amount,
            MpesaReceiptNumber=mpesa_receipt_number,
            Balance=balance,
            TransactionDate=aware_transaction_datetime,
            PhoneNumber=phone_number,
        )
        
        my_model.save()

        
        from rest_framework.response import Response
        return Response({"MyResultDesc": "YES!! It worked!"})





class TransStatusResultCallbackurlAPIView(CreateAPIView):
    pass


class TransStatusTimeoutCallbackurlAPIView(CreateAPIView):
    pass


class ReversalResultCallbackUrlAPIView(CreateAPIView):
    pass


class ReversalTimeoutCallbackUrlAPIView(CreateAPIView):
    pass


class BillManagerOptinCallbackUrlAPIView(CreateAPIView):
    pass


















"""

from rest_framework.generics import CreateAPIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response

from mpesa.models import LNMPOnline, C2BPayment
from mpesa.api.serializers import LNMPOnlineSerializer, C2BPaymentSerializer

class LNMCallbackUrlAPIView(CreateAPIView):
    queryset = LNMPOnline.objects.all()
    serializer_class = LNMPOnlineSerializer
    permission_classes = [AllowAny]

    @csrf_exempt
    def create(self, request):
        print(request.data, 'THIS IS REQUEST.DATA')

        merchant_request_id = request.data["Body"]["stkCallback"]["MerchantRequestID"]
        checkout_request_id = request.data["Body"]["stkCallback"]["CheckoutRequestID"]
        resultcode = request.data["Body"]["stkCallback"]["ResultCode"]
        resultdesc = request.data["Body"]["stkCallback"]["ResultDesc"]
        amount = request.data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][0]["Value"]
        mpesa_receipt_number = request.data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][1]["Value"]
        balance = '' 
        transaction_date = request.data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][3]["Value"]
        phone_number = request.data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][4]["Value"]
        
        from datetime import datetime
        str_tranasaction_date = str(transaction_date)
        transaction_datetime = datetime.strptime(str_tranasaction_date, '%Y%m%d%H%M%S')

        import pytz
        aware_transaction_datetime = pytz.utc.localize(transaction_datetime)
        print(transaction_datetime, 'this should be an AWARE_TRANSACTION_DATETIME')


        from mpesa.models import LNMPOnline
 
        my_model = LNMPOnline.objects.create(
            CheckoutRequestID=checkout_request_id, 
            MerchantRequestID=merchant_request_id,
            ResultCode=resultcode,
            ResultDesc=resultdesc,
            Amount=amount,
            MpesaReceiptNumber=mpesa_receipt_number,
            Balance=balance,
            TransactionDate=aware_transaction_datetime,
            PhoneNumber=phone_number,
        )
        
        my_model.save()
          
        from rest_framework.response import Response
        return Response({"MyResultDesc": "YES!! It worked!"})





class C2BValidationAPIView(CreateAPIView):
    queryset = C2BPayment.objects.all()
    serializer_class = C2BPaymentSerializer
    permission_classes = [AllowAny]

    
    @csrf_exempt
    def create(self, request):
        print(request.data, "THIS IS REQUEST.DATA Confirmation")

        context = {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
        }

        return JsonResponse(dict(context))
        



class C2BConfirmationAPIView(CreateAPIView):
    queryset = C2BPayment.objects.all()
    serializer_class = C2BPaymentSerializer
    permission_classes = [AllowAny]




    @csrf_exempt
    def create(self, request):
        print(request.data, "THIS IS REQUEST.DATA Confirmation")

        context = {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
        }

        return JsonResponse(dict(context))
        

'''
def create(self, request):
print(request.data, "THIS IS REQUEST.DATA Confirmation")

from rest_framework.response import Response
return Response({"ResultCode": 0 })
'''

"""
