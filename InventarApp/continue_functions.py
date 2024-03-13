def continue_using():
    choice = input("Do you want to continue using the program? (yes/no): ")
    return choice.lower() == 'yes'
 
def stop_program():
    print("Stopping the program...")
    return False