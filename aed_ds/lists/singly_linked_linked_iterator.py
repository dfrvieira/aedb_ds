from .tad_iterator import Iterator

class SinglyLinkedListIterator(Iterator):
    def __init__(self, target):
        self.target = target
        self.first = target
    
    def has_next(self):
        if self.target != None:
            return True
        return False

    def next(self):
            elem = self.target.get_element()
            self.target = self.target.get_next()
            return elem

    def rewind(self):
        self.target = self.first
