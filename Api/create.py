import json

import requests


mydata = open("data.json","r").read()
response=requests.post("https://reqres.in/api/users",data=json.loads(mydata))
print(response.json())
assert response.status_code == 201