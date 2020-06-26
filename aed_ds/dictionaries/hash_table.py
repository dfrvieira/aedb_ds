from .tad_dictionary import Dictionary
from ..exceptions import NoSuchElementException, DuplicatedKeyException
from ..lists.singly_linked_list import SinglyLinkedList
from .item import Item

import ctypes


class HashTable(Dictionary):
    def __init__(self, size=101):
        self.array_size = size
        self.num_elements = 0
        # Array of pointers
        self.table = (self.array_size * ctypes.py_object)()

        # Create an empty list for each table position
        for i in range(self.array_size):
            self.table[i] = SinglyLinkedList()

    def size(self):
        return self.num_elements

    def is_full(self):
        return self.num_elements == self.array_size

    def get(self, k):
        if not self.has_key(k):
            raise NoSuchElementException()
        else:
            idx = self.table[self.hash_function(k)]
            while idx.iterator().has_next():
                item = idx.iterator().next()
                if item.get_key() == k:
                    return item.get_value()

    def insert(self, k, v):
        # Check if it has key
        if self.has_key(k):
            raise DuplicatedKeyException()
        # Insert new item
        # Calculate the table index
        idx = self.hash_function(k)  # O(1)
        item = Item(k, v)  # Create a new Item
        # Insert the item in the colision list
        self.table[idx].insert_last(item)
        self.num_elements += 1  # Update the number of elements

    def update(self, k, v):
        if not self.has_key(k):
            raise NoSuchElementException()
        else:
            idx = self.table[self.hash_function(k)]
            while idx.iterator().has_next():
                item = idx.iterator().next()
                if item.get_key() == k:
                    item.set_value(v)
                    break

    def remove(self, k):
        if not self.has_key(k):
            raise NoSuchElementException()
        else:
            idx = self.table[self.hash_function(k)]
            while idx.iterator().has_next():
                item = idx.iterator().next()
                if item.get_key() == k:
                    idx.remove(idx.find(item))
                    self.num_elements -= 1
                    return item.get_value()

    def keys(self):
        result = SinglyLinkedList()
        for index in self.table:
            for _ in range(index.size()):
                result.insert_last(index.iterator().next().get_key())
        return result

    def values(self):
        result = SinglyLinkedList()
        for index in self.table:
            for _ in range(index.size()):
                result.insert_last(index.iterator().next().get_value())
        return result

    def items(self):
        result = SinglyLinkedList()
        for index in self.table:
            for _ in range(index.size()):
                item = SinglyLinkedList()
                item.insert_last(index.iterator().next().get_key())
                item.insert_last(index.iterator().next().get_value())
                result.insert_last(item)
        return result

    def hash_function(self, k):
        return sum([ord(c) for c in k]) % self.array_size

    def has_key(self, k):
        idx = self.hash_function(k)  # O(1)
        colision_list = self.table[idx]
        it = colision_list.iterator()
        while it.has_next():
            current_item = it.next()
            if current_item.get_key() == k:
                return True
        return False