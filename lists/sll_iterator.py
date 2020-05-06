import exceptions

class sll_Iterator():
    def __init__(self, target, first):
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
