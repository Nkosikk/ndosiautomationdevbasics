import requests

response = requests.get('https://www.ndosiautomation.co.za/APIDEV/groups')

print(response)

print('')
print('Response from API')
groups_response = response.json()   # Get output from the API response
print(groups_response)


print()
print(f'Status code is {response.status_code}')   # Status code of API response



print()
print()
print()


# Access data from the API response
print(groups_response["success"])
print(groups_response["data"])
print(type(groups_response["data"]))   # 'data' is a list


print()
print()

my_list = groups_response["data"]

for group in my_list:
    # print(group)
    print(f'Group Id is {group["Id"]} and Name is {group["Name"]}')
