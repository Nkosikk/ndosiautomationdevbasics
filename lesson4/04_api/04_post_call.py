import requests


email = "admin@gmail.com"
password = "@12345678"

request = {
    'email': email,
    'password': password
}

response = requests.post(f'https://www.ndosiautomation.co.za/APIDEV/login', json=request)

print(response)

print('')
print('Response from API')
groups_response = response.json()   # Get output from the API response
print(groups_response)


print()
print(f'Status code is {response.status_code}')   # Status code of API response

