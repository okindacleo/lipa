from django.http import HttpResponse, JsonResponse
import requests
from requests.auth import HTTPBasicAuth

from daraja.access_token import generate_access_token
from daraja import keys

#from access_token import generate_access_token  
#import keys
 
#shortcode = "601445" # For C2B payments
#test_msisdn = "254708374149" # For C2B payments


#def simulate_c2b_transaction(account_number, amount):
def simulate_c2b_transaction():

	api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"#API Endpoint
	my_access_token = generate_access_token()

	

	headers = {"Authorization": "Bearer %s" % my_access_token, "content-type": "application/json"}

	request = { 
		"ShortCode": keys.shortcode,
		"CommandID": "CustomerPayBillOnline",
		"Amount": "2",
		"Msisdn": keys.test_msisdn,
		"BillRefNumber": "NEX0004",
	}

	#print(account_number, amount)

	try:
		response = requests.post(api_url, json=request, headers=headers)

	except:
		response = requests.post(api_url, json=request, headers=headers, verify=False)


	#print(response.text, 'SIMULATE_C2B_TRANSACTION')

	'''
	try:
		response = requests.post(api_url, json=request, headers=headers)

	except:
		response = requests.post(api_url, json=request, headers=headers, verify=False)

	print(response.text, 'SIMULATE_C2B_TRANSACTION')

	#return HttpResponse(response.text)
	'''
simulate_c2b_transaction()

#"Amount": amount,
#"Msisdn": test_msisdn,
#"BillRefNumber": account_number,
