class DeclarationError(Exception):
    def __init__(self, Element) -> None:
        super().__init__(Element)
        self.add_note(str(Element) + " is Not Declared.")
