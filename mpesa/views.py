from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

#from django.shortcuts import render, render_to_response
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse

from daraja.lipanampesa import lipa_na_mpesa
from daraja.bill_manager_api import bill_manager_opt_in
from daraja.transaction_status_api import trans_status
from daraja.c2b import simulate_c2b_transaction
from daraja.register_urls import register_url


from .forms import CreateMpesaForm,CreateC2BMpesaForm,CreateTransactionStatusForm, CreateReversalForm
import re
#from.models import Mpesapay


#@require_http_methods(["GET", "POST"])
def mpesa_pay(request):

	form = CreateMpesaForm()

	if request.method == 'POST':
		form = CreateMpesaForm(request.POST)
		if form.is_valid():

			
			phone_number = form.cleaned_data.get('phone_number')
			
			phone_number = phone_number.replace('0', '254', 1)
			
			amount = form.cleaned_data.get('amount')

			#account_ref = form.cleaned_data.get('account_ref')

			data = {"phone_number":phone_number, 'amount': amount} #, 'account_ref':account_ref}

			
			lipa_na_mpesa(data['phone_number'], data['amount'])#, data['account_ref'])

			form = CreateMpesaForm() # cleans the phone_number, amount and account fields

			messages.success(request, 'SUCCESS!!Check phone for a PIN prompt.')
		
			
			'''
			if (match and data['account_ref'].upper() in accounts):
			
				lipa_na_mpesa(data['phone_number'], data['amount'], data['account_ref'])

				form = CreateMpesaForm() # cleans the phone_number, amount and account fields

				messages.success(request, 'Success!! Check your phone for a PIN prompt.')

			else:
				messages.success(request, 'Failed!! Account number Does NOT Exist.Please Confirm with Admin')
			'''
			return HttpResponseRedirect('/')
	else:
		form = CreateMpesaForm()

			
	context = {'form':form, 'title': True, 'mpesa_pay': True }


	return render(request, 'mpesa/mpesa_pay3.html', context)




def transaction_status(request):

	form = CreateTransactionStatusForm()

	if request.method == 'POST':
		form = CreateTransactionStatusForm(request.POST)
		if form.is_valid():

			
			transaction_id = form.cleaned_data.get('transaction_id')
			
			initiator = form.cleaned_data.get('initiator')


			data = {"transaction_id":transaction_id, 'initiator': initiator} #, 'account_ref':account_ref}

			
			trans_status(data['transaction_id'], data['initiator'])#, data['account_ref'])

			form = CreateTransactionStatusForm() # cleans the phone_number, amount and account fields

			messages.success(request, 'SUCCESS! TRANSACTION STATUS.')


			return HttpResponseRedirect('/transaction_status/')

			
	else:
		form = CreateTransactionStatusForm()

			
	context = {'form':form, 'title': True, 'transaction_status': True }

	return render(request, 'mpesa/transaction_status.html', context)



def initiate_reversal(request):

	form = CreateReversalForm()

	if request.method == 'POST':
		form = CreateReversalForm(request.POST)
		if form.is_valid():

			
			initiator = form.cleaned_data.get('initiator')
			transaction_id = form.cleaned_data.get('transaction_id')
			amount = form.cleaned_data.get('amount')
			receiver_party = form.cleaned_data.get('receiver_party')


			data = {'initiator': initiator,"transaction_id":transaction_id,'amount': amount,'receiver_party': receiver_party} #, 'account_ref':account_ref}

			
			trans_status(data['initiator'], data['transaction_id'], data['amount'], data['receiver_party'])#, data['account_ref'])

			form = CreateReversalForm() # cleans the phone_number, amount and account fields

			messages.success(request, 'REVERSAL.')

			return HttpResponseRedirect('/reversal/')

			
	else:
		form = CreateReversalForm()

			
	context = {'form':form, 'title': True, 'initiate_reversal': True }

	return render(request, 'mpesa/reversal.html', context)





def c2b_pay(request):

	c2b_form = CreateC2BMpesaForm()

	if request.method == 'POST':
		c2b_form = CreateC2BMpesaForm(request.POST)
		if c2b_form.is_valid():

			
			account_number = c2b_form.cleaned_data.get("account_number")
			amount = c2b_form.cleaned_data.get("amount")


			data = {"account_number":account_number, "amount": amount}
			print('FORM:', data["account_number"], data["amount"])

			accounts= ['NEX001', 'NEX002', 'NEX003', 'NEX004' ]
			#pattern = r'^NEX\d{3,}$'
			match = re.search(pattern, data["account_number"], re.IGNORECASE)

			#register_url()
			simulate_c2b_transaction(data["account_number"], data["amount"])

			c2b_form = CreateC2BMpesaForm() # cleans the phone_number and amount fields

			messages.success(request, 'Success!! wait for Mpesa confirmation message.')

			
			if (match and data['account_number'].upper() in accounts):
				register_url()
				simulate_c2b_transaction(data['account_number'], data['amount'])

				c2b_form = CreateC2BMpesaForm() # cleans the phone_number and amount fields

				messages.success(request, 'Success!! wait for Mpesa confirmation message.')

			else:
				messages.success(request, 'Failed!! Account number Does NOT Exist.Please Confirm with Admin')
			

			return HttpResponseRedirect('/c2b/')



	else:
		c2b_form = CreateC2BMpesaForm()

			
	context = {'c2b_form':c2b_form, 'title': True, 'c2bmpesa_pay': True}

	return render(request, 'mpesa/c2bmpesa_pay.html', context)

