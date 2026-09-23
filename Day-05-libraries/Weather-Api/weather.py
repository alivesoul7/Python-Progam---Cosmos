import requests

loc = input("Location: ")
date = input("Date (YYYY-MM-DD): ")
print("Simple Python Weather Application")

url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{loc}/{date}"

try:
	response = requests.get(url,params={"key": "2QC2WZDVJRS57AJ5RMXPJ7MPA"},timeout=10,)
	response.raise_for_status()
	print(response.status_code)

	data = response.json()
	print(data)

except requests.exceptions.RequestException as error:
	print(f"Request failed: {error}")

except ValueError:
	print("The response was not valid JSON.")