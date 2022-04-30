import json

import requests

mydata = open("data.json", "r").read()
response = requests.put("https://reqres.in/api/users/2", data=json.loads(mydata))
res=response.json()
assert response.status_code == 200
print(res)
print(res['name'])
print(res['job'])

print(res['updatedAt'])