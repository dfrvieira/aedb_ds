from singly_linked_list import SinglyLinkedList
from nodes import DoubleListNode
import exceptions
import dll_iterator

class DoubleLinkedList(SinglyLinkedList):

    def get(self, position):
        if position == 0:
            self.get_first()
        elif position == self.size()-1:
            self.get_last()
        elif 0 < position < self.size() -1:
            if not self.is_over_half(position):
                counter = 1
                node = self.head.get_next()
                while counter != position:
                    node.get_next()
                    counter += 1
                return node.get_element()
            else:
                counter = self.size() -1
                node = self.tail.get_previous()
                while counter != position:
                    node.get_previous()
                    counter -=1
                return node.get_element()

    def find(self, element):
        if element == self.get_first():
            return 0
        elif element == self.get_last():
            return self.size() -1
        else:
            node = self.head
            position = 0
            while position <= self.size():
                if node.get_element() == element:
                    return position
                node = node.get_next()
                position +=1
            return -1

    def insert_first(self, element):
        if self.size() == 0:
            self.head = DoubleListNode(element, None, None)
            self.tail = self.head

        elif self.size() == 1:
            self.head = DoubleListNode(element, self.tail, None)
            self.tail.set_previous(self.head)

        else:
            previous_first = self.head
            self.head = DoubleListNode(element, previous_first, None)
            previous_first.set_previous(self.head)

        self.count += 1

    def insert_last(self, element):
        if self.size() == 0:
            self.head = DoubleListNode(element, None, None)
            self.tail = self.head

        elif self.size() == 1:
            self.tail = DoubleListNode(element, None, self.head)
            self.head.set_next(self.tail)

        else:
            previous_tail = self.tail
            self.tail = DoubleListNode(element, None, previous_tail)
            previous_tail.set_next(self.tail)

        self.count += 1

    def insert(self, element, position):
        if position == 0:
            self.insert_first(element)
        elif self.size()-1 == position:
            self.insert_last()
        else:
            if self.is_over_half(position):
                current_node = self.tail
                for _ in range(position):
                    current_node = current_node.get_previous()
                next_node = current_node.get_next()
                new_node = DoubleListNode(element,current_node,next_node)
                next_node.set_next(new_node)
                current_node.set_previous(new_node)
            else:
                current_node = self.head
                for _ in range(position):
                    current_node= current_node.get_next()
                previous_node= current_node.get_previous()
                new_node = DoubleListNode(element,current_node,previous_node)
                previous_node.set_next(new_node)
                current_node.set_previous(new_node)
                
    def remove_first(self):
        if self.size() == 0:
            exceptions.EmptyListException()
        else:
            previous_first = self.head
            self.head = previous_first.get_next()
            self.head.set_previous(None)
            self.count -= 1
            return previous_first.get_element()

    def remove_last(self):
        if self.size() == 0:
            exceptions.EmptyListException()
        else:
            previous_tail = self.tail
            self.tail = previous_tail.get_previous()
            self.tail.set_next(None)
            self.count -= 1

    def remove(self, position):
        if position < 0 or position >= self.size():
            exceptions.InvalidPositionException()

        elif position == 0:
            self.remove_first()
            self.count -= 1

        elif position == self.size():
            self.remove_last()
            self.count -= 1

        else:
            if self.is_over_half(position):
                node = self.tail
                counter = self.size() - 1
                while counter != position:
                    if counter == position+1:
                        previous_node = node
                    node = node.get_previous()
                previous_node.set_previous(node.get_previous)
                node.get_previous().set_next(previous_node)
                self.count -= 1
                return node.get_element()
            else:
                #normal search
                node = self.head
                counter = 0
                while counter != position:
                    if counter == position -1:
                        previous_node = node
                    node = node.get_next()
                previous_node.set_next(node.get_next())
                node.get_next().set_previous(previous_node)
                self.count -= 1
                return node.get_element()

    def iterator(self, reverse = False):
        if reverse == False:
            if self.iterated_node == None:
                self.iterated_node = self.head
            it = dll_iterator.TwoWayIterator(self.iterated_node, self.head, self.tail)
            self.iterated_node = self.iterated_node.get_next()
        else:
            if self.iterated_node == None:
                self.iterated_node = self.tail
            it = dll_iterator.TwoWayIterator(self.iterated_node, self.head, self.tail)
            self.iterated_node = self.iterated_node.get_previous()
        return it

#################################################
    def is_over_half(self, position):
        if position > (self.size()//2):
            return True
        return False

