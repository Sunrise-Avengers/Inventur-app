def display_locations(data):
    print("Existing Locations:")
    for location in data['locations']:
        print(f"ID: {location['id']}, Name: {location['name']}")
