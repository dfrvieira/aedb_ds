import unittest

from aed_ds.lists.singly_linked_list import SinglyLinkedList
from aed_ds.exceptions import NoSuchElementException

class TestSinglyLinkedListIterator(unittest.TestCase):
    def setUp(self):
        self.list = SinglyLinkedList()
        self.iterator = self.list.iterator()
    
    def add_elements(self, quantity, shift=0):
        for i in range(quantity):
            self.list.insert_last(f"element {i+1+shift}")
        self.iterator = self.list.iterator()

    def test_has_next(self):
        # 0 elements
        self.assertFalse(self.iterator.has_next())

        # 1 elements
        self.add_elements(1)
        self.assertTrue(self.iterator.has_next())

        # 2 elements
        self.add_elements(1)
        self.assertTrue(self.iterator.has_next())

        # 5 elements
        self.add_elements(3)
        self.assertTrue(self.iterator.has_next())

        # iterate to end and test
        for _ in range(5):
            self.assertTrue(self.iterator.has_next())
            self.iterator.next()
        self.assertFalse(self.iterator.has_next())

        # clear list        
        self.list.make_empty()
        self.iterator = self.list.iterator()
        self.assertFalse(self.iterator.has_next())
    
    def test_iterate_empty_list_after_removal(self):
        self.add_elements(1)
        self.list.remove_last()
        self.iterator = self.list.iterator()
        self.assertFalse(self.iterator.has_next())
        with self.assertRaises(NoSuchElementException):
            self.iterator.next()

    def test_next(self):
        with self.assertRaises(NoSuchElementException):
            self.iterator.next()
        self.add_elements(1)
        self.assertEqual(self.iterator.next(), "element 1")
        self.add_elements(4, shift=1)
        self.assertEqual(self.iterator.next(), "element 1")
        self.assertEqual(self.iterator.next(), "element 2")
        self.assertEqual(self.iterator.next(), "element 3")
        self.assertEqual(self.iterator.next(), "element 4")
        self.assertEqual(self.iterator.next(), "element 5")
        with self.assertRaises(NoSuchElementException):
            self.iterator.next()

    def test_rewind(self):
        self.iterator.rewind()

        self.add_elements(5)
        
        # Iterate to middle and rewind
        for _ in range(3):
            self.iterator.next()
        self.iterator.rewind()
        self.assertTrue(self.iterator.has_next())
        self.assertEqual(self.iterator.next(), "element 1")

        # Iterate to end and rewind
        while self.iterator.has_next():
            self.iterator.next()
        self.iterator.rewind()
        self.assertTrue(self.iterator.has_next())
        self.assertEqual(self.iterator.next(), "element 1")


        