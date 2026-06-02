'''
API Data Collector in Python
Task 1 (Get API data): Create a function that sends a GET request to a simple API endpoint and returns the data
(https://www.ndosiautomation.co.za/APIDEV/groups).

Task 2 (Save Data to a File): Create a function that takes the API response and saves it into a json file.

Task 3 (Read and Search Data): Create a function that reads the saved file, ask the user for a group name to search for,
and checks whether that group exists in the data.
If the group is not found, then display an error message.
If the group is found, display a success message with the group Id.


'''
import pprint

#API Data Collector in Python- Task 1

#The end point: https://www.ndosiautomation.co.za/APIDEV/groups

import json
import requests

url = "https://www.ndosiautomation.co.za/APIDEV/groups"


# Task 1 & 2: Get and Save API Data
def saveApiResponse(response):
    print(
        "Task 2 (Save Data to a File): Create a function that takes the API response and saves it into a json file.\n"
    )
    if response.status_code == 200:
        with open("API_Data.json", "w") as API_file:
            json.dump(response.json(), API_file, indent=4)
        print(
            f"The API data has been successfully collected. Status Code: {response.status_code} and file API_Data.json saved successfully\n"
        )
    else:
        print(
            f"The API data collection failed. Status Code: {response.status_code}"
        )
        # Only try to print json if the response actually has content
        try:
            print(f"Response body returned: {response.json()}")
        except:
            print("No JSON body returned.")
        print("No file created!")


# Task 3: Read and Search Data
def searchGroupData():
    print(
        "Task 3 (Read and Search Data): Search for a group name and display its ID.\n"
    )

    try:
        with open("API_Data.json", "r") as API_file:
            file_content = json.load(API_file)
    except FileNotFoundError:
        print("Error: 'API_Data.json' file not found. Run the data collector first.")
        return

    search_string = input("Enter group name to search for: ").strip().lower()
    found = False

    # Handle if the JSON data is a list of groups
    if isinstance(file_content, list):
        for record in file_content:
            # Safely get 'name' and 'id' (adjust keys if the API uses different names like 'group_name')
            group_name = str(record.get("name", "")).lower()

            if search_string == group_name:
                print(
                    f"Success! Group found. Group ID: {record.get('id', 'N/A')}"
                )
                found = True
                break  # Stop searching once found

    # Handle if the JSON data is a dictionary where groups are nested
    elif isinstance(file_content, dict):
        # If your API returns data wrapped in a key like {"groups": [...]}
        groups_list = file_content.get("groups", file_content.values())
        for record in groups_list:
            if isinstance(record, dict):
                group_name = str(record.get("name", "")).lower()
                if search_string == group_name:
                    print(
                        f"Success! Group found. Group ID: {record.get('id', 'N/A')}"
                    )
                    found = True
                    break

    if not found:
        print(f"Error: The group '{search_string}' was not found in the data.")


# --- Execution Flow ---

# Fetch and save data (Tasks 1 & 2)
try:
    response = requests.get(url)
    saveApiResponse(response)
except requests.exceptions.RequestException as e:
    print(f"Network Error: Could not connect to API. Details: {e}")

# Search data (Task 3)
searchGroupData()