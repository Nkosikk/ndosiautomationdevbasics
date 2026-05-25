import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

API_URL = "https://www.ndosiautomation.co.za/APIDEV/groups"
FILE_NAME = "groups.json"


# -------------------------------
# Task 1: Get API Data
# -------------------------------
def get_api_data():
    try:
        response = requests.get(API_URL, verify=False)

        response.raise_for_status()

        data = response.json()
        print(data)

        print("API data fetched successfully.")
        return data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching API data: {e}")
        return None


# -------------------------------
# Task 2: Save Data to JSON File
# -------------------------------
def save_data_to_file(data):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)

        print(f"Data successfully saved to {FILE_NAME}")

    except Exception as e:
        print(f"Error saving data to file: {e}")


# -------------------------------
# Task 3: Read and Search Data
# -------------------------------
def search_group():
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)

        group_name = input("Enter group name to search: ")

        found = False

        # Access the list inside "data"
        for group in data["data"]:

            if group["Name"].lower() == group_name.lower():

                print("Group found successfully.")
                print(f"Group ID: {group['Id']}")

                found = True
                break

        if not found:
            print("Error: Group not found.")

    except FileNotFoundError:
        print("Error: JSON file not found.")

    except Exception as e:
        print(f"Error reading/searching data: {e}")


# -------------------------------
# Main Execution
# -------------------------------
if __name__ == "__main__":

    api_data = get_api_data()

    if api_data:
        save_data_to_file(api_data)

    search_group()