from Error import MailError
class Email(list):
    def __init__(self, Element):
        self.element = Element
        if isinstance(Element, list) or  isinstance(Element, tuple):
            for i in Element:
                if "@gmail.com" not in i:
                    raise MailError(i)
                else:
                    self.append(i) 
    def add(self, Element):
        if "@gmail.com" not in Element:
            raise MailError(Element)
        else:
            self.append(Element)
