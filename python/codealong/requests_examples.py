import requests

request_bbc = requests.get('https://bbc.co.uk/')

print(request_bbc)

print(request_bbc.text)
print(request_bbc.status_code)
print(request_bbc.content)
