import unittest
from addressBookSystem import AddressBook
book = AddressBook()


class TestAddressBook(unittest.TestCase):

    def test_addContacts(self):
        book.addContacts("Siya", "Salunkhe", "Satara", "Satara", "Maharastra", "415507", "7066647330",
                         "priyanka.chavan1408@gmail.com")
        self.assertEqual(len(book.contact), 1)
        self.assertTrue(len(book.contact), 1)

    def test_editContact(self):
        book.editContact("Siya", "Salunkhe", "Satara", "Satara", "Maharastra", "415507", "7066647330",
                         "priyanka.chavan1408@gmail.com")
        self.assertEqual(book.contact[0][0], "piya")

    def test_deleteContacts(self):
        book.deleteContacts()
        self.assertGreaterEqual(len(AddressBook.contact),0)


if __name__ == '__main__':
     unittest.main()