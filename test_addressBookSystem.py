import unittest
from addressBookSystem import AddressBook
book = AddressBook()


class TestAddressBook(unittest.TestCase):
    def test_addContacts(self):
        book = AddressBook()
        book.addContacts("Siya","Salunkhe","Satara","Satara","Maharastra","415507","7066647330","priyanka.chavan1408@gmail.com")
        self.assertEqual(len(book.contact),1)
        self.assertTrue(len(book.contact), 1)


if __name__ == '__main__':
    unittest.main()


