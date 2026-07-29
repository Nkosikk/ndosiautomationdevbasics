import requests


def get_api_data():
    url = "https://www.ndosiautomation.co.za/APIDEV/groups"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error for bad responses (4xx, 5xx)
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


