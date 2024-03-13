import json
from create_functions import create_location
from read_functions import display_locations
from update_functions import update_location
from delete_functions import delete_location
from continue_functions import continue_using, stop_program  
from update_functionskasten import update_kasten

def main():
    with open('db.json', 'r') as f:
        data = json.load(f)
 
    display_locations(data)
 
    while True:
        choice = input("Choose an option:\n1. Create a new location(1)\n2. Update data of a location(2)\n3. Delete a location(3)\n4. Update Casten(4)\n4.Stop using the program(5)")
 
        if choice == '1':
            create_location(data)
        elif choice == '2':
            update_location(data)
        elif choice == '3':
            delete_location(data)
        elif choice == '4':
            update_kasten(data)    
        elif choice == '5':
            if not stop_program():
                break
        else:
            print("Invalid choice")
 
        if not continue_using():
            break
 
if __name__ == "__main__":
    main()