import random
import string
import json
import requests
from time import time
import jwt
from runtime_business.settings import *


def generate_password():
    alphanumeric_string = ''.join(random.choices(string.ascii_letters, k=8))
    return alphanumeric_string


def generateToken():
	token = jwt.encode(
		{'iss': api_key, 'exp': time() + 5000},
		# Secret used to generate token signature
		api_sec,
		# Specify the hashing alg
		algorithm='HS256')
	return token


def createMeeting():
	headers = {'authorization': 'Bearer ' + generateToken(), 'content-type': 'application/json'}
	r = requests.post(f'https://api.zoom.us/v2/users/me/meetings', headers=headers, data=json.dumps(meetingdetails))
	y = json.loads(r.text)
	join_URL = y["join_url"]
	meetingPassword = y["password"]

	return([join_URL, meetingPassword])
