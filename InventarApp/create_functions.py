import json

def create_location(data):
    name = input("Enter the name of the new location: ")
    address = input("Enter the address of the new location: ")
    floor = input("Enter the floor of the new location: ")
    city = input("Enter the city of the new location: ")
    postal_code = input("Enter the postal code of the new location: ")

    new_location_id = len(data['locations']) + 1

    new_location = {
        "id": new_location_id,
        "name": name,
        "address": address,
        "floor": floor,
        "city": city,
        "postal_code": postal_code,
        "boxes": []
    }

    data['locations'].append(new_location)

    with open('db.json', 'w') as f:
        json.dump(data, f, indent=4)

    print(f"Location {name} added successfully with ID {new_location_id}")
