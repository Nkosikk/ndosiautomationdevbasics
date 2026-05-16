import requests


limit = 50
offset = 0


# Hard coded values
# response = requests.get(f'https://www.ndosiautomation.co.za/APIDEV/testimonials?limit=50&offset=0')


response = requests.get(f'https://www.ndosiautomation.co.za/APIDEV/testimonials?limit={limit}&offset={offset}')

print(response)

print('')
print('Response from API')
groups_response = response.json()   # Get output from the API response
print(groups_response)


print()
print(f'Status code is {response.status_code}')   # Status code of API response

