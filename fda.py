import requests
import os
import urllib
import urllib.request
import getpass
import django
import webbrowser
from time import sleep

from Crypto.Cipher import AES

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cs3240project.settings')
django.setup()

username = input("Enter Username: ")
password = getpass.getpass('Enter Password: ')
payload = {
    'username': username,
    'password': password
}

host = "http://127.0.0.1:8000"

key = "Nader_is_awesome"

def decrypt_file(filename_input, symmetric_key):
    init_vec = b"1234567890123456"
    AES_key = AES.new(symmetric_key, AES.MODE_CFB, init_vec)
    output_filename = filename_input[:-4]
    with open(filename_input, 'rb') as f:
        raw_file = f.read()
        data_dec = AES_key.decrypt(raw_file)
    with open(output_filename, 'wb') as o:
        o.write(data_dec)
        print('Decrypted File Name:' + output_filename)
    return True
