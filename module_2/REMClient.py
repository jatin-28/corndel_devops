import http.client
import json
import string
from random import random

resourcePath = "/api/users"


def randomName():
    return ''.join(random.choices(string.ascii_uppercase, k=1)).join(random.choices(string.ascii_lowercase, k=5))


def makeRequest(method = "GET", payload = "", path = resourcePath):
    conn = http.client.HTTPConnection("rem-rest-api.herokuapp.com")
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache"
    }

    conn.request(method, path, payload, headers)

    res = conn.getresponse()
    resdata = res.read()
    jsondata = json.loads(resdata.decode("utf-8"))

    print("--------")
    print(method)
    print(jsondata)
    print("--------")

    return jsondata


makeRequest("GET")

# POST
firstName = randomName()
lastName = randomName()
payload = "{\"firstName\": \""+ firstName + "\", \"lastName\": \""+lastName+"\"}"
jsonData = makeRequest("POST", payload)
createdId = jsonData['id']

# GET with query params
uriPath = f"{resourcePath}?offset={createdId - 1}&limit=10"
makeRequest("GET", path=uriPath)

# PUT
firstName = randomName()
lastName = randomName()
payload = "{\"firstName\": \""+ firstName + "\", \"lastName\": \""+lastName+"\"}"
uriPath = f"{resourcePath}/{createdId}"
makeRequest("PUT", payload, uriPath)

# GET with query params
uriPath = f"{resourcePath}?offset={createdId - 1}&limit=10"
makeRequest("GET", path=uriPath)

# DELETE
uriPath = f"{resourcePath}/{createdId}"
makeRequest("DELETE", payload, uriPath)




