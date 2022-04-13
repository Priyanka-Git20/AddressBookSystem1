'''
    @Author: Priyanka Salunkhe
    @Date: 2022-04-11 11:45:00
    @Last Modified by: Priyanka Salunkhe
    @Last Modified time: 2022-04-11 12:00:00
    @Title :Ability to create a Contacts in Address Book with first and last names, address, city, state, zip, phone number and email…
'''


class AddressBook:
    def __init__(self,firstName,lastName,address,city,state,zip,phoneNumber,email):
        """
        Description:
            main constrcutor whenever we will create object then we can runn this.
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


if __name__ == '__main__':
     print("Welcome to the address book system.")
     Contact1 = AddressBook("Priyanka", "Salunkhe", "A/P-Katarkhatav,Tal-Khatav", "Satara", "maharashtra", 415507, 7066647330,
                            "priyanka.chavan1408@gmail.com")
     print(vars(Contact1))
