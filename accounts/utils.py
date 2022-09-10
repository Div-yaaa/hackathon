import random
import string
import json
import requests
from time import time
import jwt


API_KEY = 'JhP57IGqQES4U83c5arnQQ'
API_SEC = 'LUXR5G8MXTQnHDTIKOl9mFas09f12VlykLxI'

def generate_password():
    alphanumeric_string = ''.join(random.choices(string.ascii_letters, k=6))
    return alphanumeric_string


def generateToken():
	token = jwt.encode(
		{'iss': API_KEY, 'exp': time() + 5000},
		# Secret used to generate token signature
		API_SEC,
		# Specify the hashing alg
		algorithm='HS256')
	return token


def createMeeting():
	headers = {'authorization': 'Bearer ' + generateToken(),
			   'content-type': 'application/json'}
	r = requests.post(f'https://api.zoom.us/v2/users/me/meetings', headers=headers, data=json.dumps(meetingdetails))
	print("\n creating zoom meeting ... \n")
	y = json.loads(r.text)
	join_URL = y["join_url"]
	meetingPassword = y["password"]

	return ([join_URL, meetingPassword])
