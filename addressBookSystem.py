'''
    @Author: Priyanka Salunkhe
    @Date: 2022-04-11 12:00:00
    @Last Modified by: Priyanka Salunkhe
    @Last Modified time: 2022-04-14 12:40:00
    @Title :Ability to add contacts in the address book and display.
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

    def addContacts(self,firstName,lastName,address,city,state,zip,phoneNumber,emailId):
        """
        Description:
            Taking the input from the user and add into the list .
        Parameter:
            self is as parameter
        Return:
            Returning nothing but printing the list.
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
            exit()
        else:
            print('Invalid Option. Try Again!')


