from Contacts import Contact

contact = Contact()


contact.contact = [
    ("John Doe", "0123456789"),
    ("Jane Smith", "0987654321"),
    ("Alice Johnson", "0456789123"),
    ("Bob Anderson", "0899990000"),
    ("Emma Brown", "0123456789"),
    ("Michael Davis", "0987654321"),
    ("Olivia Garcia", "0456789123"),
    ("William Harris", "0899990000"),
    ("Sophia Lee", "0123456789"),
    ("Daniel Miller", "0987654321"),
    ("Emily Nelson", "0456789123"),
    ("Alexander Parker", "0899990000"),
    ("Grace Robinson", "0123456789"),
    ("Benjamin Taylor", "0987654321"),
    ("Mia Turner", "0456789123"),
    ("Henry Walker", "0899990000"),
    ("Victoria Young", "0123456789"),
    ("David Adams", "0987654321"),
    ("Ella Brown", "0456789123"),
    ("Joseph Carter", "0899990000"),
    ("Scarlett Davis", "0123456789"),
    ("Jacob Evans", "0987654321"),
    ("Chloe Foster", "0456789123"),
    ("Liam Gray", "0899990000"),
    ("Harper Hill", "0123456789"),
    ("Matthew Jackson", "0987654321"),
    ("Ava Kelly", "0456789123"),
    ("Luke Mitchell", "0899990000"),
    ("Nora Phillips", "0123456789"),
    ("Gabriel Reed", "0987654321"),
    ("Lily Sanchez", "0456789123"),
    ("Christopher Turner", "0899990000"),
    ("Zoe Walker", "0123456789"),
    ("Andrew White", "0987654321"),
    ("Samantha Wilson", "0456789123"),
    ("Jack Young", "0899990000"),
    ("Grace Adams", "0123456789"),
    ("Daniel Bell", "0987654321"),
    ("Ella Carter", "0456789123"),
    ("James Davis", "0899990000"),
    ("Sophia Evans", "0123456789"),
    ("Joseph Foster", "0987654321"),
    ("Mia Garcia", "0456789123"),
    ("Oliver Hill", "0899990000"),
    ("Emily Jackson", "0123456789"),
    ("Jacob Kelly", "0987654321"),
    ("Chloe Lee", "0456789123"),
    ("Lucas Mitchell", "0899990000"),
    ("Liam Nelson", "0123456789"),
    ("Ava Parker", "0987654321"),
    ("Matthew Reed", "0456789123"),
    ("Benjamin Sanchez", "0899990000"),
    ("Mila Taylor", "0123456789"),
    ("Christopher Turner", "0987654321"),
    ("Zoe Walker", "0456789123"),
    ("William White", "0899990000")
]


contact.friends_contact = [
    ("Nora Phillips", "0123456789"),
    ("Gabriel Reed", "0987654321"),
    ("Lily Sanchez", "0456789123"),
    ("Christopher Turner", "0899990000"),
    ("Zoe Walker", "0123456789"),
    ("Andrew White", "0987654321"),
    ("Samantha Wilson", "0456789123"),
    ("Jack Young", "0899990000"),
    ("Grace Adams", "0123456789"),
    ("Daniel Bell", "0987654321"),
    ("Ella Carter", "0456789123"),
    ("James Davis", "0899990000"),
    ("Sophia Evans", "0123456789"),
    ("Joseph Foster", "0987654321"),
    ("Mia Garcia", "0456789123"),
    ("Oliver Hill", "0899990000")
]



contact.family_contact = [
    ("Bob Anderson", "0899990000"),
    ("Emma Brown", "0123456789"),
    ("Michael Davis", "0987654321"),
    ("Olivia Garcia", "0456789123"),
    ("William Harris", "0899990000"),
    ("Sophia Lee", "0123456789"),
    ("Daniel Miller", "0987654321"),
    ("Emily Nelson", "0456789123"),
    ("Alexander Parker", "0899990000"),
    ("Grace Robinson", "0123456789"),
    ("Benjamin Taylor", "0987654321"),
    ("Mia Turner", "0456789123"),
    ("Henry Walker", "0899990000"),
    ("Victoria Young", "0123456789"),
    ("David Adams", "0987654321"),
    ("Ella Brown", "0456789123")
]





def menu():
    print (" ")
    print ("         --- MENU --- \n")
    print ("       Select the number \n corresponding  to the option you want.")
    print ("______________________________\n")
    print ("1. Search for a contact? \n")
    print ("2. Display all contacts?  \n")
    print ("3. Create a new contact?  \n")
    print ("4. Edit a  contact?  \n")
    print ("5. Delete a  contact?  \n")
    print ("6. Add contact to another group?  \n")
    print ("7. Exit  \n")
    print ("______________________________")
    
    return (1, 2, 3, 4, 5, 6, 7)
    
    


def Contacts():
    a, b, c, d, e, f, g = menu()
    
    
    try:
        select = int(input("Please select options  1-7. \n"))
    except ValueError:
        print ('Invalid Selection')
        Contacts()
        
    try :   
        if select == a:
            print ("--- SEARCH FOR CONTACT ---\n")
            contact.search_contact()
            back = input ("Back? (Y/N)  ").upper()
                        
            if back == "N":
                pass 
            elif back == "Y":
                menu()
                Contacts()
                
                                                                          
        elif select == b:
            print ("--- DISPLAY CONTACT ---\n")
            contact.display_contact()
            back = input ("Back? (Y/N)  ").upper()
                        
            if back == "N":
                pass 
            elif back == "Y":
                menu()
                Contacts()
                
                                    
        elif select == c:
            print ("--- CREATE CONTACT ---\n")
            contact.create_contact()
            back = input ("Back? (Y/N)  ").upper()
                        
            if back == "N":
                pass 
            elif back == "Y":
                menu()
                Contacts()
                
                                    
        elif select == d:
            print ("--- EDIT CONTACT ---\n")
            contact.edit_contact()
            back = input ("Back? (Y/N)  ").upper()
                        
            if back == "N":
                pass 
            elif back == "Y":
                menu()
                Contacts()
                
                                    
        elif select == e:
            print ("--- DELETE CONTACT ---\n")
            contact.delete_contact()
            back = input ("Back? (Y/N)  ").upper()
                        
            if back == "N":
                pass 
            elif back == "Y":
                menu()
                Contacts()
                
                                    
        elif select == f:
            print ("--- ADD CONTACT ---\n")
            contact.add_contact()
            back = input ("Back? (Y/N)  ").upper()
                        
            if back == "N":
                pass 
            elif back == "Y":
                menu()
                Contacts()


        elif select == g:
            raise SystemExit
                 
        else:
            print ("There's no option like that")
            Contacts()

        
            
    except UnboundLocalError:
        print (' ')
        
        
        

    
Contacts()
    