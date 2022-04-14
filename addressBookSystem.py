'''
    @Author: Priyanka Salunkhe
    @Date: 2022-04-11 1:30:00
    @Last Modified by: Priyanka Salunkhe
    @Last Modified time: 2022-04-14 3:00:00
    @Title :Ability to edit the contact in address book.
'''

class AddressBook:
    contact = {}
    contact_length = len(contact)

    def __init__(self, firstName=None, lastName=None, address=None, city=None, state=None, zip=None, phoneNumber=None,
                 email=None):
        """
        Description:
            main constructor whenever we will create object then we can run this.
        Parameter:
            passing all contact details.
        Return:
            Returning nothing but saving values in main variables.
        """
        self.firstName = firstName
        self.lastName = lastName
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.phoneNumber = phoneNumber
        self.email = email

    def addContacts(self, firstName, lastName, address, city, state, zip, phoneNumber, emailId):
        """
        Description:
            Taking the input from the user and add into the list .
        Parameter:
            person info like first name,last name, city,state,zip,phone number,emailId.
        Return:
            Returning the dictionary.
        """
        lst = []
        lst.append(firstName)
        lst.append(lastName)
        lst.append(address)
        lst.append(city)
        lst.append(state)
        lst.append(zip)
        lst.append(phoneNumber)
        lst.append(emailId)
        contact_length = len(AddressBook.contact)
        AddressBook.contact[contact_length] = lst
        AddressBook.contact_length += 1
        return AddressBook.contact

    def displayContact(self):
        """
        Description:
            Display the list .
        Parameter:
            self is as parameter
        Return:
            Returning nothing but printing the list.
        """
        print(AddressBook.contact)

    def editContact(self,firstName, lastName, address, city, state, zip, phoneNumber, emailId):
        """
        Description:
            First check the input taken from user is in list and then modify the list .
        Parameter:
             person info like first name,last name, city,state,zip,phone number,emailId.
        Return:
            Returning the name which we check is it in list or not and dictionary
        """

        checkName = input("Enter the first name to check is it in contact or not")
        for i in range(AddressBook.contact_length):
            if checkName == AddressBook.contact[i][0]:
                print("Exists in list")
                break
        else:
            print("Not in list")
            exit()

        while True:
            option = int(input(
                '1. To modify First name, 2. To modify last name, 3. To modify address, 4. To modify city, 5. To modify state, 6. To modify zip, 7.To modify email, 8. To modify phone number'))
            if option == 1:
                firstName = str(input("Enter the first name : "))
                del AddressBook.contact[i][0]
                AddressBook.contact[i].insert(0, firstName)
            elif option == 2:
                lastName = str(input("Enter the last name : "))
                del AddressBook.contact[i][1]
                AddressBook.contact[i].insert(1, lastName)
            elif option == 3:
                address = str(input("Enter the address : "))
                del AddressBook.contact[i][2]
                AddressBook.contact[i].insert(2, address)
            elif option == 4:
                city = str(input("Enter the city : "))
                del AddressBook.contact[i][3]
                AddressBook.contact[i].insert(3, city)
            elif option == 5:
                state = str(input("Enter the state : "))
                del AddressBook.contact[i][4]
                AddressBook.contact[i].insert(4, state)
            elif option == 6:
                zip = str(input("Enter the zip : "))
                del AddressBook.contact[i][5]
                AddressBook.contact[i].insert(5, zip)
            elif option == 7:
                phoneNumber = str(input("Enter the phone number : "))
                del AddressBook.contact[i][6]
                AddressBook.contact[i].insert(6, phoneNumber)
            elif option == 8:
                emailId = str(input("Enter the email id : "))
                del AddressBook.contact[i][7]
                AddressBook.contact[i].insert(7, emailId)
            else:
                break

        return checkName, AddressBook.contact,AddressBook.contact_length


if __name__ == '__main__':
    print("Welcome to the address book system.")
    myBook = AddressBook()
    print(
        'Enter 1. To Add Contacts 2. For display a Contact  3.To Exit')
    while True:
        choice = int(input('Enter your choice: '))
        if choice == 1:
            firstName = str(input("Enter the first name :\n"))
            lastName = str(input("Enter the last name :\n"))
            address = str(input("Enter the address :\n"))
            city = str(input("Enter the city :\n"))
            state = str(input("Enter the state :\n"))
            zip = input("Enter the zip :\n")
            phoneNumber = input("Enter the phone number :\n")
            emailId = str(input("Enter the email address :\n"))
            myBook.addContacts(firstName,lastName,address,city,state,zip,phoneNumber,emailId)
        elif choice == 2:
            myBook.displayContact()
        elif choice == 3:
            myBook.editContact(firstName=1, lastName=2, address=3,city= 4, state=5, zip=6, phoneNumber=7, emailId=8)
        elif choice == 4:
            exit()
        else:
            print('Invalid Option. Try Again!')

