import requests

print(requests.get('http://127.0.0.1:5000/pill?name=daniel').text)
