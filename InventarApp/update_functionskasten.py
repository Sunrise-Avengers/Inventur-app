import json
from read_functions import display_kasten

def update_kasten(data):
    print("Choose a kasten to update:")
    display_kasten(data)
    kasten_id = input("Enter the ID of the kasten you want to update: ")

    # Find the kasten with the specified ID
    kasten = next((k for k in data['kasten'] if k['id'] == int(kasten_id)), None)

    if kasten:
        update_choice = input(f"What do you want to update for {kasten['name']}?\n1. Update a single attribute\n2. Update the entire kasten\n")

        if update_choice == '1':
            # Get the attribute to update
            attribute = input(f"What attribute of {kasten['name']} do you want to change? (name, gross): ")

            if attribute in kasten.keys():
                # Prompt for the new value of the selected attribute
                new_value = input(f"Enter the new value for {attribute}: ")

                # Show the old and new values before updating
                print(f"Old {attribute}: {kasten[attribute]}")
                print(f"New {attribute}: {new_value}")

                # Prompt for confirmation
                confirmation = input("Are you sure you want to make these changes? (yes/no): ")

                if confirmation.lower() == 'yes':
                    # Update the kasten's attribute
                    kasten[attribute] = new_value

                    # Update db.json with the changes
                    with open('db.json', 'w') as f:
                        json.dump(data, f, indent=4)

                    print(f"{attribute} updated successfully for {kasten['name']}")
                else:
                    print("Changes discarded")
            else:
                print("Invalid attribute")
        elif update_choice == '2':
            # Prompt for the new values for the entire kasten
            name = input("Enter the new name for the kasten: ")
            gross = input("Enter the new value for gross (True/False): ")

            # Show the old and new values before updating
            print(f"Old name: {kasten['name']}, gross: {kasten['gross']}")
            print(f"New name: {name}, gross: {gross}")

            # Prompt for confirmation
            confirmation = input("Are you sure you want to make these changes? (yes/no): ")

            if confirmation.lower() == 'yes':
                # Update the kasten
                kasten.update({
                    "name": name,
                    "gross": bool(gross.lower() == 'true')
                })

                # Update db.json with the changes
                with open('db.json', 'w') as f:
                    json.dump(data, f, indent=4)

                print(f"{kasten['name']} updated successfully")
            else:
                print("Changes discarded")
        else:
            print("Invalid choice")
    else:
        print("Kasten not found")
