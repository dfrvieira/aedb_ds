import exceptions
import tad_iterator

class sll_Iterator(tad_iterator.Iterator):
    def __init__(self, target):
        self.target = target
        self.first = target

    def has_next(self):
        if self.target != None:
            return True
        return False

    def next(self):
        if self.has_next():
            elem = self.target.get_element()
            self.target = self.target.get_next()
            return elem

    def rewind(self):
        self.target = self.first
