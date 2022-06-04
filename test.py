import requests

BASE = 'http://localhost:5000/'

# response=requests.get(BASE + 'get_location_names')
# print(response.json())

response=requests.post(BASE+"predict_home_price", {'total_sqft' : '1200', 'location': 'whitefield', 'bhk':3, 'bath':3})
print(response.text)