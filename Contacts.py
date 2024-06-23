# Contact List 

class Contact:
    
    def __init__(self):
        self.name = ""
        self.num = ""
        self.contact = []
        self.friends_contact = []
        self.family_contact = []
        
        
        
        
    def create_contact(self):
        stop = False
        while not stop:
            print ('')
            
            self.name = input("Name: ").title()
            
            if self.name == "" or self.name == ' ': 
                while self.name == "":
                    print ("Type a Name")
                    self.name = input("Name: ").title()
                    print (" ")
            
            self.num = input ("Number: ")
            
            if len(self.num) == 10 and self.num.isdigit():
                  
                self.contact.append((self.name, self.num))
            else:
                
                while len(self.num) != 10 or not self.num.isdigit():
                    print("Invalid Input")
                    self.num = input ("Number: ")
                    print (" ")
                self.contact.append((self.name, self.num))
              
            stop = True if input('>> ') == "x" else False 
            print (f"""
Name: {self.name}           	
Phone Number: {self.num}           	
            	 """)
            print ("__________________________________")
        return self.contact 
        
        
        
    
    def display_contact(self):
        print ("      --- CONTACTS ---")
        for cont in self.contact:
            print (f"""
Name: {cont[0]}           	
Phone Number: {cont[-1]}           	
            	 """)
        print ("__________________________________")
            	 
            	 
            	 
    
    def search_contact(self):
        print(" ")
        search = input('Enter your Search 🔎: ').title()
        found_contacts = []
        
        for cont in self.contact:
            names = cont[0].split(" ")           
            if search == cont[0] or search in names:
                found_contacts.append(cont)
    
        if len(found_contacts) > 0:
            print(" ")
            print(f'{search} is Found')
            print(" ")
            for contact in found_contacts:
                print(f"""
Name: {contact[0]}           	
Phone Number: {contact[-1]}           	
                """)
            print ("__________________________________")
            return search, found_contacts[-1][-1], True
            
    
        print(f'No contacts found for the given search term: {search}')
        print ("__________________________________")
        return "", '', False



    
    @staticmethod
    def replace(list_, item, replacement):      
        for inst in list_:
            if inst[0] == item or inst[-1] == item:
                z = list_.index(inst)
                list_[z] = replacement 
        return (list_)       
        
    
    
    
    def edit_contact(self):
        while True:
            s_name, s_num, s_bool = self.search_contact()
            s_name = s_name.split(" ")
        
            if len(s_name) < 2:
                print("Please enter a full name.")
                continue

            s_name = " ".join(s_name)
            break

        if s_bool:
            action = input("Editing Name or Number ($/#): ")

            if action == "$":
                while True:
                    new_name = input("Edit name: ").title()
                    if len(new_name.split(" ")) < 2:
                        print("Please enter a full name.")
                        continue
                    self.replace(self.contact, s_name, (new_name, s_num))
                    print(f"""
Name: {new_name}
Phone Number: {s_num}
                    """)
                    print ("__________________________________")
                    break
                    

            elif action == "#":
                print(" ")
                new_num = input("Edit number: ")

                if len(new_num) == 10 and new_num.isdigit():
                    print ("__________________________________")
                    self.replace(self.contact, s_num, (s_name, new_num))
                else:
                    print("Invalid input. Please enter a 10-digit number.")
                    print(" ")
                    while len(new_num) != 10 or not new_num.isdigit():
                        new_num = input("Edit number: ")
                    print ("__________________________________")
                    self.replace(self.contact, s_num, (s_name, new_num))
                   
                    
        else:
            print(f'No contacts found for the given search term: {s_name}')
            print ("__________________________________")





    def delete_contact(self):
        while True:
            s_name, s_num, s_bool = self.search_contact()
            s_name = s_name.split(" ")
        
            if len(s_name) < 2:
                print("Please enter a full name.")
                continue

            s_name = " ".join(s_name)
            break

        if s_bool:
            for inst in self.contact:
                if inst[0] == s_name or inst[-1] == s_num:
                    self.contact.remove(inst)
            print ("__________________________________")
            return (self.contact)       
            



    def add_contact(self):
        while True:
            s_name, s_num, s_bool = self.search_contact()
            s_name = s_name.split(" ")
        
            if len(s_name) < 2:
                print("Please enter a full name.")
                continue

            s_name = " ".join(s_name)
            break
        addto = input ("Add to Family or Friends? (1 / 2).....  ")
        if addto == "1":
            self.family_contact.insert(0, (s_name, s_num))
            print ("      --- FAMILY ---")
            for cont in self.family_contact:
                print (f"""
Name: {cont[0]}           	
Phone Number: {cont[-1]}           	
            	     """)
            print ("__________________________________")
            
            
        elif addto == "2":
            self.friends_contact.insert(0, (s_name, s_num))
            print ("        --- FRIENDS ---")
            for cont in self.friends_contact:
                print (f"""
Name: {cont[0]}           	
Phone Number: {cont[-1]}           	
            	     """)
            print ("__________________________________")
             


