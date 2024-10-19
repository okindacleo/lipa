from datetime import datetime
from daraja.keys import initiator_password

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64
import os
from django.conf import settings


def get_timestamp():
    unformatted_time = datetime.now()
    formatted_time = unformatted_time.strftime("%Y%m%d%H%M%S")

    return formatted_time




def generate_security_credential(initiator_password):

    cert_file_path = os.path.join(settings.CERTIFICATES_DIR,'trans_status_public_key.cer')

    with open(cert_file_path, 'rb') as cert_file:
        public_key = cert_file.read()

    rsakey = RSA.import_key(public_key)
    cipher = PKCS1_v1_5.new(rsakey)

    encrypted_password = cipher.encrypt(initiator_password.encode('utf-8'))
    security_credential = base64.b64encode(encrypted_password).decode('utf-8')

    return security_credential
