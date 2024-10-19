from django.forms import ModelForm
from django import forms

class CreateMpesaForm(forms.Form):
	#phone_number = forms.CharField(max_length=12, widget=forms.TextInput(attrs={'placeholder': '2547XXXXXXX'}))
	phone_number = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'id': 'phone_number', 'required':'required'}))
	amount = forms.CharField(max_length=6, widget=forms.TextInput(attrs={'id': 'amount', 'required':'required'}))
	#account_ref = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'id': 'account_ref', 'required':'required'}))
	
class CreateC2BMpesaForm(forms.Form):
	account_number = forms.CharField(max_length=10)
	amount = forms.CharField(max_length=6)



class CreateTransactionStatusForm(forms.Form):
	transaction_id = forms.CharField(max_length=10)
	initiator = forms.CharField(max_length=12)
	

class CreateReversalForm(forms.Form):
	initiator = forms.CharField(max_length=12)
	transaction_id = forms.CharField(max_length=10)
	amount = forms.CharField(max_length=10)
	receiver_party = forms.CharField(max_length=10)
	