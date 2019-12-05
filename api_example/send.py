import requests

headers = {}

headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTc0NTQzNjAwLCJqdGkiOiI2MzE0OTJhNDc2Yzk0ODg2ODZlMDZlNjYyODNjYTE4NiIsInVzZXJfaWQiOjF9.MvTVoe3mkj2E58EzMGFb8oftddEppTHPo-juEpzc1dE'

r = requests.get('http://127.0.0.1:8000/paradigms/', headers = headers)

print(r.text)