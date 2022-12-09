class DeclarationError(Exception):
    def __init__(self, Element) -> None:
        super().__init__(Element)
        self.add_note("DeclaretionError : " + str(Element) + " is Not Declared.")
class TypeNotFoundError(Exception):
    def __init__(self, Element) -> None:
        super().__init__(Element)
        self.add_note("TypeNotFoundError : Type " + str(Element) + " Is Not Found")
        