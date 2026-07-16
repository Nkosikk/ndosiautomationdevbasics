import json


def save_to_file(data, filename="groups.json"):
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Data successfully saved to {filename}")

    except Exception as e:
        print(f"Error saving file: {e}")

