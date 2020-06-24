from .tad_tree import Tree
from ..dictionaries.tad_ordered_dictionary import OrderedDictionary
from ..exceptions import DuplicatedKeyException, NoSuchElementException, \
    EmptyDictionaryException
from .nodes.binary_nodes import BinarySearchTreeNode


class BinarySearchTree(OrderedDictionary, Tree):
    # Returns the number of elements in the dictionary.
    def size(self): pass

    # Returns true if the dictionary is full.
    def is_full(self): pass

    # Returns the value associated with key k.
    # Throws NoSuchElementException
    def get(self, k): pass

    # Inserts a new value, associated with key k.
    # Throws DuplicatedKeyException
    def insert(self, k, v): pass

    # Updates the value associated with key k.
    # Throws NoSuchElementException
    def update(self, k, v): pass

    # Removes the key k, and the value associated with it.
    # Throws NoSuchElementException
    def remove(self, k): pass

    # Returns a List with all the keys in the dictionary.
    def keys(self): pass

    # Returns a List with all the values in the dictionary.
    def values(self): pass

    # Returns a List with all the key value pairs in the dictionary.
    def items(self): pass

    # Returns an iterator of the elements in the dictionary
    def iterator(self): pass

    # Returns the element with the smallest key
    # Throws EmptyTreeException
    def get_min_element(self): pass
    
    # Returns the element with the largest key
    # Throws EmptyTreeException
    def get_max_element(self): pass

    # Returns the root of the tree
    # Throws EmptyTreeException
    def get_root(self): pass

    # Returns the height of the tree
    # Throws EmptyTreeException
    def height(self): pass

    # Returns True if the tree is empty
    def is_empty(self): pass
    