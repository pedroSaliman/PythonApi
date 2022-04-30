import requests
response=requests.get("https://reqres.in/api/users?page=2")
print(response.text)
resp_json= response.json()
print(response.url)
print(response.content)
print(response.status_code)
print(resp_json['data'][0]['email'])
assert resp_json['data'][0]['email'] == 'michael.lawson@reqres.in',"the email is not match"







