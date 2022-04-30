import json

import requests


mydata = open("login.json","r").read()
response=requests.post("https://reqres.in/api/users",data=json.loads(mydata))
print(response.json())
assert response.status_code == 201
