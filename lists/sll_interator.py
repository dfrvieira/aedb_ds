import exceptions

class Iterator():
    def __init__(self, target):
        self.target = target
        self.first = target

    def has_next(self):
        if self.target.get_next() != None:
            return True
        return False

    def next(self):
        if self.has_next():
            elem = self.target.get_element()
            self.target.get_next()
            return elem

    def rewind(self):
        self.target = self.first
        self.next()