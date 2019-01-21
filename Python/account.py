class Account:
    id          = int
    name        = str
    document    = str
    email       = str
    password    = str

    def __init__(self, name, document):
        self.name       = name
        self.document   = document