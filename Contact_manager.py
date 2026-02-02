# Simple Contact Book (Using Dictionary)


# exmpty dict 
Contacts = {} 




# MENU 
while True:
    
    print()
    print("1. Add new contact")
    print("2. View all contacts")
    print("3. Search contact")
    print("4. Update contact number")
    print("5. Delete contact")
    print("6. Exit")
    print()
    
    user_number = int(input("Enter Number: "))
    
    
    # 1. adding elements into dictionaries
    if user_number == 1:
        add = list(Contacts.items())
        
        name = str(input("Enter Contact Name: "))
        phone = int(input("Enter Phone Number: "))
        
        add.append((name, phone))
        Contacts = dict(add)
        
        print()
        
        
    # 2. view all the elements
    elif user_number == 2:
        if len(Contacts) == 0:
            print("No Contacts available.\n")
            print()
        else:
            print("All Contacts:")
            for i, (name, phone) in enumerate(Contacts.items(), start = 1):
                print(i, "Name:", name, "Phone:", phone)
            print()
       
        
    
    # 3. Search Contacts
    elif user_number == 3:
        user_search = str(input("Enter Name: "))
        
        if user_search in Contacts:
                print("Contact Found")
                print(user_search, ":", Contacts[user_search])
                print()
        
        else:
            print("Contact Not Found!")
            print()
    
    
    
    # 4. Update contact number
    elif user_number == 4:
        print()
        print("1- To Update Contact Name")
        print("2- To Update Contact Phone Number")
         
        update_num = int(input("Enter a Number: "))
        old_name = input("Enter the existing contact name: ")


        if update_num == 1:
            new_name = input("Enter Contact Name: ")
            Contacts[new_name] = Contacts.pop(old_name)
            
        elif update_num == 2:
            new_phone = input("Enter Contact Number: ")
            Contacts[old_name] = new_phone 
             
             
        else:
            print("Wrong Number..")
            
        print()
    
    
    
    # 5. Delete contact
    elif user_number == 5:
        name = input("Enter contact name to delete: ")

        if name in Contacts:
            del Contacts[name]
            print("Contact deleted successfully!\n")
            
        else:
            print("Contact not found!\n")
        
    
    
    #6 . Exit
    elif user_number == 6:
        print("Exiting program...")
        break
    