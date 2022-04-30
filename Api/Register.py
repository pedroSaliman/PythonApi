import json

import requests


mydata = open("register.json","r").read()
response=requests.post("https://reqres.in/api/users",data=json.loads(mydata))
print(response.json())
assert response.status_code == 201
assert response.json()['email'] == 'eve.holt@reqres.in'