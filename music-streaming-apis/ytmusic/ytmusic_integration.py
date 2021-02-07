import requests
import getpass
from ytmusicapi import YTMusic

user_gmail = input("Enter your Google account email id: ")
user_password = getpass.getpass("Enter your Google account password: ")

auth_request = requests.get('https://music.youtube.com/signin', auth=(user_gmail, user_password))

try:
    auth_request.raise_for_status()
except requests.HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
else:
    print('Success!')

print(auth_request.headers)

# print(auth_request.raw)

# auth_header_json = auth_request.json()
# print(auth_header_json)