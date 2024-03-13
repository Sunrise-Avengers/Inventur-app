import json
from read_functions import display_locations
 
def update_location(data):
    print("Choose a location to update:")
    display_locations(data)
    location_id = input("Enter the ID of the location you want to update: ")
 
    # Find the location with the specified ID
    location = next((loc for loc in data['locations'] if loc['id'] == int(location_id)), None)
 
    if location:
        update_choice = input(f"What do you want to update for {location['name']}?\n1. Update a single attribute\n2. Update the entire location\n")
 
        if update_choice == '1':
            # Get the attribute to update
            attribute = input(f"What attribute of {location['name']} do you want to change? (name, address, floor, city, postal_code): ")
 
            if attribute in location.keys():
                # Prompt for the new value of the selected attribute
                new_value = input(f"Enter the new value for {attribute}: ")
 
                # Show the old and new values before updating
                print(f"Old {attribute}: {location[attribute]}")
                print(f"New {attribute}: {new_value}")
 
                # Prompt for confirmation
                confirmation = input("Are you sure you want to make these changes? (yes/no): ")
 
                if confirmation.lower() == 'yes':
                    # Update the location's attribute
                    location[attribute] = new_value
 
                    # Update db.json with the changes
                    with open('db.json', 'w') as f:
                        json.dump(data, f, indent=4)
 
                    print(f"{attribute} updated successfully for {location['name']}")
                else:
                    print("Changes discarded")
            else:
                print("Invalid attribute")
        elif update_choice == '2':
            # Prompt for the new values for the entire location
            name = input("Enter the new name for the location: ")
            address = input("Enter the new address for the location: ")
            floor = input("Enter the new floor for the location: ")
            city = input("Enter the new city for the location: ")
            postal_code = input("Enter the new postal code for the location: ")
 
            # Show the old and new values before updating
            print(f"Old name: {location['name']}, address: {location['address']}, floor: {location['floor']}, city: {location['city']}, postal_code: {location['postal_code']}")
            print(f"New name: {name}, address: {address}, floor: {floor}, city: {city}, postal_code: {postal_code}")
 
            # Prompt for confirmation
            confirmation = input("Are you sure you want to make these changes? (yes/no): ")
 
            if confirmation.lower() == 'yes':
                # Update the location
                location.update({
                    "name": name,
                    "address": address,
                    "floor": floor,
                    "city": city,
                    "postal_code": postal_code
                })
 
                # Update db.json with the changes
                with open('db.json', 'w') as f:
                    json.dump(data, f, indent=4)
 
                print(f"{location['name']} updated successfully")
            else:
                print("Changes discarded")
        else:
            print("Invalid choice")
    else:
        print("Location not found")