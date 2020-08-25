import datetime
import hashlib
import os

import requests
from requests.exceptions import HTTPError


def get_query_with_authentication_params(payload, PUBLIC_KEY, PRIVATE_KEY):
    """
    Authenticate a request.
    :param payload: dict
    :return: dict
    """
    now_string = datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')
    auth_hash = hashlib.md5()
    auth_hash.update(now_string.encode('utf-8'))
    auth_hash.update(PRIVATE_KEY.encode('utf-8'))
    auth_hash.update(PUBLIC_KEY.encode('utf-8'))

    payload['hash'] = auth_hash.hexdigest()
    payload['ts'] = now_string
    payload['apikey'] = PUBLIC_KEY
    return payload


publickey = os.getenv('PUBLIC_KEY')
privatekey = os.getenv('PRIVATE_KEY')

characterName = "Spider"
resourcePath = "https://gateway.marvel.com:443/v1/public/characters"

try:
    payload = {'nameStartsWith': characterName}
    payload = get_query_with_authentication_params(payload, publickey, privatekey)
    response = requests.get(resourcePath, params=payload)
    response.raise_for_status()

    jsonResponse = response.json()
    print("Entire JSON response")
    print(jsonResponse)

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')

