'''
    @Author: Priyanka Salunkhe
    @Date: 2022-04-11 1:30:00
    @Last Modified by: Priyanka Salunkhe
    @Last Modified time: 2022-04-11 3:00:00
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

    def addContacts(self):
        """
        Description:
            Taking the input from the user and add into the list .
        Parameter:
            self is as parameter
        Return:
            Returning dictionary.
        """
        lst = []
        lst.append(str(input("Enter the first name : ")))
        lst.append(str(input("Enter the last name : ")))
        lst.append(str(input("Enter the address : ")))
        lst.append(str(input("Enter the city : ")))
        lst.append(str(input("Enter the state : ")))
        lst.append(int(input("Enter the zip : ")))
        lst.append(int(input("Enter the phone number: ")))
        lst.append(str(input("Enter the emailId : ")))
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
            Returning nothing but printing the dictionary.
        """
        print(AddressBook.contact)

    def editContact(self):
        """
        Description:
            First check the input taken from user is in list and then modify the list .
        Parameter:
            self is as parameter
        Return:
            Returning dictionary.
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
                '1. To modify First name, 2. To modify last name, 3. To modify address, 4. To modify city, 5. To modify state, 6. To modify zip, 7.To modify email, 8. To modify phone number: '))
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
        return checkName, AddressBook.contact

    def deleteContacts(self):
        """
        Description:
            Delete the contact of the person using their name. .
        Parameter:
            self is as parameter
        Return:
            Returning dictionary.
        """
        checkName = input("Enter the first name to check is it in contact or not")
        for i in range(AddressBook.contact_length):
            if checkName == AddressBook.contact[i][0]:
                del AddressBook.contact[i]
                print("Delete the person")
                break
            else:
                print("Not in list")
        return AddressBook.contact

    def menu(self):
        """
        Description:
            this menu function in this we have shown total menu to the user for user interface and we are calling functions with user requirement
        Parameter:
            self is as parameter
        Return:
            Returning nothing just doing operations
        """

        print(
            'Enter 1. To Add Contacts 2. For display a Contact  3.To edit the contacts 4.To delete the contact 5.To Exit')
        while True:
            choice = int(input('Enter your choice: '))
            if choice == 1:
                self.addContacts()
            elif choice == 2:
                self.displayContact()
            elif choice == 3:
                self.editContact()
            elif choice == 4:
                self.deleteContacts()
            elif choice == 5:
                exit()
            else:
                print('Invalid Option. Try Again!')


if __name__ == '__main__':
    print("Welcome to the address book system.")
    myBook = AddressBook()
    myBook.menu()
