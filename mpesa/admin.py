from django.contrib import admin

# Register your models here.
from .models import LNMPOnline, C2BPayment


#admin.site.register(LNMPOnline)

class LNMOnlineAdmin(admin.ModelAdmin):
    list_display = ("MpesaReceiptNumber", "PhoneNumber", "Amount", "TransactionDate")
admin.site.register(LNMPOnline, LNMOnlineAdmin)


class C2BPaymentAdmin(admin.ModelAdmin):
    list_display = ("TransID", "MSISDN", "BillRefNumber", "TransAmount", "TransTime", "FirstName", "LastName", "OrgAccountBalance")
admin.site.register(C2BPayment, C2BPaymentAdmin)


