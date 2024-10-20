from django.http import HttpResponse, JsonResponse
import requests
from requests.auth import HTTPBasicAuth

from daraja.access_token import generate_access_token 
from daraja.utils import get_timestamp
from daraja.encode import generate_password
from daraja import keys
from daraja.generate_account import generate_random_string
from daraja.utils import generate_security_credential

#from . import generate_random_string

'''
from access_token import generate_access_token 
from utils import get_timestamp
from encode import generate_password
import keys
'''
#   OR



#def lipa_na_mpesa():
def lipa_na_mpesa(phone_number, amount):#, account_ref):


	api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"#API Endpoint
	#api_url = "https://api.safaricom.co.ke/mpesa/stkpush/v1/processrequest"#production

	formatted_time = get_timestamp()
	decoded_password = generate_password(formatted_time)
	my_access_token = generate_access_token()

	

	headers = { "Authorization": "Bearer %s" % my_access_token }

	request = {
		"BusinessShortCode": keys.business_shortCode,
		"Password": decoded_password,
		"Timestamp": formatted_time,
		"TransactionType": "CustomerPayBillOnline",
		"Amount": amount,
		#"Amount": "1",
		#"PartyA": phone_number,
		"PartyA": "254799416398",
		"PartyB": keys.business_shortCode,
		"PhoneNumber": phone_number,
		#"PhoneNumber": "254708252968",
		"CallBackURL": "https://inject-50d08d8f31b6.herokuapp.com/api/payments/lnm/",
		#"AccountReference": "YM0001",
		"AccountReference": generate_random_string(),
		"TransactionDesc": "Hotspot Fees",
	}
		  
	#response = requests.post(api_url, json=request, headers=headers)
	#print(request["AccountReference"])
	

	try:
		response = requests.post(api_url, json=request, headers=headers)

	except:
		response = requests.post(api_url, json=request, headers=headers, verify=False)
	
	#print('THIS IS RESPONSE.HEADERS', response.headers)

	data = response.json()

	#print(data)
	#if data["ResponseCode"] == "0":
	#print('SUCCESS!! Proceed to PIN Entry')

	'''
	elif data["ResponseCode"] != "0":
		print('Oops!! Check Phone Number')	  
	#print('THIS IS RESPONSE.TEXT', response.text)
	return HttpResponse('Success')
	'''

#lipa_na_mpesa()
#response = requests.request("POST", 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest',headers=headers, data=payload)
#print(response.text.encode('utf8'))

#print('SECURITY CREDENTIAL:', generate_security_credential("cleo123"))



