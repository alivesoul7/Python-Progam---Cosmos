import requests

#1.Dispatch GET request to github api
response = requests.get("http://api.github.com")

#2. Inspect numerical status code
print(response.status_code)

# 3. Extract and parse Json payload
print(response.json())