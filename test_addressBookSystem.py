import unittest
from addressBookSystem import AddressBook


class TestAddressBook(unittest.TestCase):

    def test_addContacts(self):
        book = AddressBook()
        book.addContacts()
        self.assertEqual(len(AddressBook.contact),1)