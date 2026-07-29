import json

def search_group(filename="groups.json"):
    try:
        with open(filename, "r") as file:
            data = json.load(file)

        group_name = input("Enter group name to search: ").strip().lower()

        found = False

        for group in data:
            # Adjust keys depending on actual API structure
            if group.get("name", "").lower() == group_name:
                print(f"✅ Group found! ID: {group.get('id')}")
                found = True
                break

        if not found:
            print("❌ Group not found.")

    except FileNotFoundError:
        print("File not found. Please run Task 2 first.")

    except Exception as e:
        print(f"Error reading/searching file: {e}")


search_group()

