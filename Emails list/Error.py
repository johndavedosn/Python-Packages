class MailError(Exception):
    def __init__(self, Element) -> None:
        super().__init__()
        self.add_note("MailError : " + Element + " is not an email")
