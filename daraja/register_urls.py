from django.http import HttpResponse, JsonResponse
import requests
from requests.auth import HTTPBasicAuth

from daraja.access_token import generate_access_token
from daraja import keys


def register_url():
	my_access_token = generate_access_token()


	api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
	#api_url = "https://api.safaricom.co.ke/mpesa/c2b/v1/registerurl"# production
	
	headers = {"Authorization": "Bearer %s" % my_access_token}


	request = {
		"ShortCode": keys.shortcode,
		"ResponseType": "Completed",
		#"ConfirmationURL": "https://9a19-197-232-105-30.ngrok.io/api/payments/c2b-confirmation/",
		#"ValidationURL": "https://9a19-197-232-105-30.ngrok.io/api/payments/c2b-validation/"

		"ConfirmationURL": "https://dundisha.herokuapp.com/api/payments/c2b-confirmation/",
		"ValidationURL": "https://dundisha.herokuapp.com/api/payments/c2b-validation/"
	
	 	
	 }

	
	try:
		response = requests.post(api_url, json=request, headers=headers)
	except:
		response = requests.post(api_url, json=request, headers=headers, verify=False)


	data = response.json()
	print(data)
	#print(response.text, 'REGISTER URL')


#register_url()