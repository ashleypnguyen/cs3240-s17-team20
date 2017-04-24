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
