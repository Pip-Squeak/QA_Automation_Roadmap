# Exercise: API Request
import requests

response = requests.get("https://api.github.com")
print("Status code:", response.status_code)
print("Content:", response.json())
