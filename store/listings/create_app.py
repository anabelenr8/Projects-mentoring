import requests

# Define the URL and headers for the POST request
url = 'https://api.pythonic.me/v1/app/'
headers = {
    'Pythonic-Api-V1-Key': 'ApM8MUgSIFefsHDSSqoVKTHtEvZntOBlUW7gidnRtfazdFY4YD9EBxS54sdvIfD9NGASOJsaK2xeyXyZsw9BLw'
}

# Send the POST request to create an app
response = requests.post(url, headers=headers)

# Check if the request was successful
if response.status_code == 201:
    data = response.json()
    print("API Key:", data.get('api_key'))
    print("API Token:", data.get('api_token'))
else:
    print("Failed to create app:", response.status_code, response.text)
