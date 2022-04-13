import unittest
from addressBookSystem import AddressBook


class TestAddressBook(unittest.TestCase):

    def test_addContacts(self):
        book = AddressBook()
        book.addContacts()
        self.assertEqual(len(AddressBook.contact),1)

    def test_editContact(self):
        book = AddressBook()
        book.editContact()
        self.assertEqual(AddressBook.contact[0][0],"piya")
