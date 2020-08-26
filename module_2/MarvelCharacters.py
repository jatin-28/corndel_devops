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


def makeGetRequest(url, payload):
    try:
        payload = get_query_with_authentication_params(payload, publickey, privatekey)
        response = requests.get(url, params=payload)
        response.raise_for_status()

        jsonResponse = response.json()

        return jsonResponse["data"]["results"]

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')


def printName(counter, character):
    print(f"[] {counter}. {character['name']}")


resourcePath = "https://gateway.marvel.com:443/v1/public/characters"
publickey = os.getenv('PUBLIC_KEY')
privatekey = os.getenv('PRIVATE_KEY')

characterResults = []
while not characterResults:
    characterName = input("Search for a Marvel character starting with: ")

    payload = {'nameStartsWith': characterName}

    characterResults = makeGetRequest(resourcePath, payload)


#print(characterResults)

while True:
    print("Choose a character: ")
    [printName(counter, x) for counter,x in enumerate(characterResults)]
    index = int(input("Enter a number (-1 to exit): "))
    if index == -1:
        break

    character = characterResults[index]
    # print(f"You chose: {character}")

    comics = makeGetRequest(character["comics"]["collectionURI"], {})

    print(f"{character['description']}")
    print()
    print(comics)
    for c in comics:
        print(f'Title: c["title"]')
        # comic = makeGetRequest(c["collections"], {})
        # print(f"Title: {comic}")
        print(f"\t\tDescription: {c['description']}")
    print()
    input("Press enter to continue.....")



