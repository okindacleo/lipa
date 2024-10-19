from rest_framework import serializers


from mpesa.models import LNMPOnline
class LNMOnlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = LNMPOnline
        fields = 'id'
















"""

from rest_framework import serializers
from mpesa.models import LNMPOnline, C2BPayment


class LNMPOnlineSerializer(serializers.ModelSerializer):

    class Meta:
        model = LNMPOnline
        #fields = ("id",)
        
        fields = ("CheckoutRequestID",
        		  "MerchantRequestID",
        		  "ResultCode",
        		  "ResultDesc",
        		  "Amount",
        		  "MpesaReceiptNumber",
        		  "Balance",
        		  "TransactionDate",
        		  "PhoneNumber",
        		)
        

    
class C2BPaymentSerializer(serializers.ModelSerializer):
	
    class Meta:
        model = C2BPayment
        #fields = ("id",)
        
        fields =("TransactionType",
			"TransID",
			"TransTime",
			"TransAmount",
			"BusinessShortCode",
			"BillRefNumber",
			"InvoiceNumber",
			"OrgAccountBalance",
			"ThirdPartyTransID",
			"MSISDN",
			"FirstName",
			"MiddleName",
			"LastName",
			)
		
"""