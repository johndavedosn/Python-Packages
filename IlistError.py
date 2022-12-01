class IntError(Exception):
    def __init__(self, Elementt) -> None:
        super().__init__(Elementt)
        self.add_note("IntError : " + str(Elementt) + " is not an interger")
