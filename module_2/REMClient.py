import requests
import json
import string
import random

conn = requests.Session()
resourcePath = "http://rem-rest-api.herokuapp.com/api/somerandomstrings"

def randomName():
    return ''.join(random.choices(string.ascii_lowercase, k=5))


def makeRequest(method="GET", payload="", path="http://rem-rest-api.herokuapp.com/api/somerandomstrings"):

    headers = {
        'Content-Type': "application/json"
    }

    res = conn.request(method, path, data=payload, headers=headers)

    if res.status_code > 400:
        raise ValueError

    jsondata = res.json()

    print("--------")
    print(f"{method} - status: {res.status_code} reason: {res.reason}")
    print(jsondata)
    print("--------")

    return jsondata


makeRequest("GET")

# POST
firstName = randomName()
lastName = randomName()
payload = "{\"firstName\": \"" + firstName + "\", \"lastName\": \"" + lastName + "\"}"
jsonData = makeRequest("POST", payload)
createdId = jsonData['id']

# GET with query params
uriPath = f"{resourcePath}?offset=0&limit=20"
makeRequest("GET", path=uriPath)

# PUT
firstName = randomName()
lastName = randomName()
payload = "{\"firstName\": \"" + firstName + "\", \"lastName\": \"" + lastName + "\"}"
uriPath = f"{resourcePath}/{createdId}"
makeRequest("PUT", payload, uriPath)

# GET with query params
uriPath = f"{resourcePath}?offset={createdId - 1}&limit=10"
makeRequest("GET", path=uriPath)

# DELETE
uriPath = f"{resourcePath}/{createdId}"
makeRequest("DELETE", payload, uriPath)

makeRequest("GET")