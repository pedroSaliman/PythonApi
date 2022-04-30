import requests
response=requests.get("https://reqres.in/api/users/23")
print(response.text)
resp_json= response.json()
print(response.url)
print(response.content)
print(response.status_code)






