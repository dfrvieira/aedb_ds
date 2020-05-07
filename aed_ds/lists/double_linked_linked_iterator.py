from .singly_linked_linked_iterator import Iterator


class TwoWayIterator(Iterator):
    def __init__(self, target, first, last):
        Iterator.__init__(self, target, first)
        self.last = last

    def has_previous(self):
        if self.target != None:
            return True
        return False

    def previous(self):
        if self.has_previous():
            elem = self.target.get_element()
            self.target = self.target.get_previous()
            return elem

    def full_forward(self):
        self.target = self.last
