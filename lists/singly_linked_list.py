from tad_list import List
from exceptions import *
from nodes import SingleListNode
import sll_iterator

class SinglyLinkedList(List):
    def __init__(self):
        self.head = None
        self.tail = None
        self.interated_node = None
        self.count = 0
    # Returns true iff the list contains no elements.
    def is_empty(self):
        return self.head == None

    # Returns the number of elements in the list.
    
    def size(self):
        return self.count

    # Returns the first element of the list.
    # Throws EmptyListException.
    
    def get_first(self):
        try:
            return self.head.get_element()
        except:
            raise EmptyListException()

    # Returns the last element of the list.
    # Throws EmptyListException.
    
    def get_last(self):
        try:
            return self.tail.get_element()
        except:
            raise EmptyListException()

    # Returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    
    def get(self, position):
        if self.size()!=0:
            if -1 < position <=self.size():
                current_node = self.head
                for _ in range(position):
                    current_node = current_node.get_next()
                return current_node.get_element()
            else:
                raise InvalidPositionException()
        else:
            raise EmptyListException()


    # Returns the position in the list of the
    # first occurrence of the specified element,
    # or -1 if the specified element does not
    # occur in the list.
    
    def find(self, element):
        if self.size() != 0:
            node = self.head
            position = 0
            while position <= self.size():
                if node.get_element() == element:
                    return position
                node = node.get_next()
                position += 1

            return -1

    # Inserts the specified element at the first position in the list.
    
    def insert_first(self, element):
        if self.size()==0:
            self.head = SingleListNode(element, None)
            self.tail=self.head
        else:
            before_node= self.head
            self.head = SingleListNode(element, before_node)
        self.count+=1

    # Inserts the specified element at the last position in the list.
    
    def insert_last(self, element):
        if self.size()==0:
            self.tail=SingleListNode(element, None)
            self.head = self.tail
        else:
            self.tail.set_next(SingleListNode(element, None))
            self.tail = self.tail.get_next()
        self.count += 1

    # Inserts the specified element at the specified position in the list.
    # Range of valid positions: 0, ..., size().
    # If the specified position is 0, insert corresponds to insertFirst.
    # If the specified position is size(), insert corresponds to insertLast.
    # Throws InvalidPositionException.
    
    def insert(self, element, position):
        if self.size()==0:
            raise EmptyListException()
        else:
            if -1 < position <=self.size():
                if position==0:
                    self.insert_first(element)
                elif position == self.size()-1:
                    self.insert_last(element)
                else:
                    current_node=self.head
                    for i in range(position-1):
                        current_node=current_node.get_next()
                        
                    new_node= SingleListNode(element,current_node.get_next())
                    current_node.set_next(new_node)
                    self.count+=1

    # Removes and returns the element at the first position in the list.
    # Throws EmptyListException.
    
    def remove_first(self):
        if self.size() == 0:
            raise EmptyListException()
        else:
            previous_first = self.head
            self.head = previous_first.get_next()
            self.count -= 1
            return previous_first.get_element()

    # Removes and returns the element at the last position in the list.
    # Throws EmptyListException.
    
    def remove_last(self):
        try:
            current = self.head
            for _ in range(0,self.size()-2):
                current = current.get_next()
            current.set_next(None)
            self.tail = current
            self.count-=1
        except:
            raise EmptyListException()
    
    # Removes and returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    # Throws InvalidPositionException.
    
    def remove(self, position):
        try:
            current = self.head
            if position == 0:
                self.remove_first()
            elif position == self.size():
                self.remove_last()
            else:
                previous = None
                count = 1
                while count != position:
                    previous = current
                    current = current.get_next()
                    count +=1
                previous.set_next(current.get_next())
                self.count-=1
        except:
            raise InvalidPositionException()
    
    # Removes all elements from the list.
    
    def make_empty(self):
        self.head = None
        self.tail = None
        self.count = 0
    # Returns an iterator of the elements in the list (in proper sequence).
    
    def iterator(self, reset = False):
        if self.iterated_node == None:
            self.iterated_node = self.head
        it = sll_iterator.Iterator(self.iterated_node, self.head)
        if reset == False:
            self.iterated_node=self.iterated_node.get_next()
        else:
            self.iterated_node = self.head
        return it
