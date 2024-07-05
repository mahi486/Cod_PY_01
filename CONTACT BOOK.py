
#CONTACT BOOK CODE IN PYTHON
# CONTACT BOOK CONTAIN ADDING,DELETE THE CONTACT , SEARCH AND UPDATE CONTACT , DISPLAY CONTACT LIST

# USE OF DICITIONARY




contacts = {}

def add_contact():
    name = input("enter your name:")
    phone = input("enter your phone number:")
    email = input("enter your email:")
    address = input("enter your address:")
    
    if name in contacts:
        print("this number is already exists.")
    else:
        contacts[name] = phone
        print("contact added successfully.")
        
        
def view_contacts():
     if contacts == {}:
         print("there are no contacts.")
     else:
         print("display contacts list: ")
         for name,phone in contacts.items():
              print(name,phone)
             
             
def search_contact():
    name = input("enter your name:")
    phone = input("enter your phone number:")
    for contact in contacts:
        if contact.lower() == name.lower():
            print("contact is found")
            print(contact,contacts[contact])
            break
        else:
            print("contact is not found. contact is not in list.")
            
            
def update_contact():
    name = input("enter your name:") 
    for contact in contacts:
        if contact == name:
            phone = input("enter the new number :") 
            contacts[name] = phone
            
            print("contact updated successfully.")
            print(contact,contacts[contact])
            break
        else:
            print("this contact not exist in contacts list.")
            
            
def delete_contact():
    name = input("enter your name:")
    if name in contacts:
        del contacts[name]
        print("contact deleted successfully.")
    else:
        print("this contact not exist in contact list. ")
          
    
while True:
    print("CONTACT BOOK:")
    print("1. add contact")
    print("2. view contacts")
    print("3. search contact")
    print("4. update contact")
    print("5. delete contact")
    print("6. EXIT ")
   
    
    
    userchoice = int(input(" enter your choice (1-6):"))
    
    if userchoice == 1:
        add_contact()
        
    elif userchoice == 2:
        view_contacts()
        
    elif userchoice == 3:
        search_contact()
        
    elif userchoice == 4:
         update_contact()
         
    elif userchoice == 5:
        delete_contact()
        
    elif userchoice == 6:
        print("exit contact book.")
        break
    else:
        print("your choie is invalid. please enter valid choice.")
        
        
        
         
         
        
    
    
    
    
    

