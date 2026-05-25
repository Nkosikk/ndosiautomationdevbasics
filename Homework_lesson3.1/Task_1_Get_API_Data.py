import requests

# Task 1: Get API data
def get_api_data():
    url = "https://www.ndosiautomation.co.za/APIDEV/groups"

    try:
        response = requests.get(url)

        # Check if request was successful
        if response.status_code == 200:
            print("API request successful.")
            return response.json()
        else:
            print(f"Error: Received status code {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None
