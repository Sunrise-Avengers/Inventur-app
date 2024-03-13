import json
from read_functions import display_locations

def delete_location(data):
    print("Choose a location to delete:")
    display_locations(data)
    location_id = input("Enter the ID of the location you want to delete: ")

    # Find the location with the specified ID
    location = next((loc for loc in data['locations'] if loc['id'] == int(location_id)), None)

    if location:
        print(location)

        # Bestätigungsfrage stellen
        confirm_delete = input("Are you sure you want to delete this location? (yes/no): ").lower()

        if confirm_delete == 'yes':
            data['locations'].remove(location)

            # Update db.json with the changes
            with open('db.json', 'w') as f:
                json.dump(data, f, indent=4)

            print(f"Location {location['name']} deleted successfully")
        else:
            print("Deletion canceled by user.")
    else:
        print("Location not found")