import os
import datetime
import hashlib
import requests
from requests.exceptions import HTTPError


class Request:

    def __init__(self, PUBLIC_KEY, PRIVATE_KEY):
        self.publicKey = PUBLIC_KEY
        self.privateKey = PRIVATE_KEY

    def get_query_with_authentication_params(self, payload):
        """
        Authenticate a request.
        :param payload: dict
        :return: dict
        """
        now_string = datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')
        auth_hash = hashlib.md5()
        auth_hash.update(now_string.encode('utf-8'))
        auth_hash.update(self.privateKey.encode('utf-8'))
        auth_hash.update(self.publicKey.encode('utf-8'))

        payload['hash'] = auth_hash.hexdigest()
        payload['ts'] = now_string
        payload['apikey'] = self.publicKey
        return payload

    def makeGetRequest(self, url, payload):
        try:
            payload = self.get_query_with_authentication_params(payload)
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
request = Request(publickey, privatekey)

characterResults = []
while not characterResults:
    characterName = input("Search for a Marvel character starting with: ")

    payload = {'nameStartsWith': characterName}

    characterResults = request.makeGetRequest(resourcePath, payload)


#print(characterResults)

while True:
    print("Choose a character: ")
    [printName(counter, x) for counter,x in enumerate(characterResults)]
    index = int(input("Enter a number (-1 to exit): "))
    if index == -1:
        break

    character = characterResults[index]
    # print(f"You chose: {character}")

    comics = request.makeGetRequest(character["comics"]["collectionURI"], {})

    print(f"{character['description']}")
    print()
    print(comics)
    for c in comics:
        print(f'Title: {c["title"]}')
        # comic = request.makeGetRequest(c["urls"][0]["url"], {})
        # print(f"Summary: {comic}")
        # TODO wrap text
        print(f"\t\tDescription: {c['description']}")
    print()
    input("Press enter to continue.....")



