class queue:
    def __init__(self, fixed_size):
        self.fixed_size = fixed_size
        self.l = []
    def add(self, element) :
        if len(self.l) == self.fixed_size:
            del self.l[0]
            self.l.append(element)
            return self
        self.l.append(element)
        return self
    def is_full(self):
        return len(self.l) == self.fixed_size
    def get_list(self):
        return self.l

