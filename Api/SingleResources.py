import requests




response=requests.get("https://reqres.in/api/unknown/2")
print(response.text)
resp_json= response.json()
print(response.url)
print(response.content)
print(response.status_code)
assert response.status_code==200
assert resp_json['data']['name']=='fuchsia rose'
















