
class Bank:
    def __init__(self, name, last_name, pesel ):
        self.name = name
        self.last_name = last_name
        self.pesel = pesel
        self.balance = 0
        pesel = str(pesel)
        if len(pesel) != 11:
            self.pesel = "pesel niepoprawny"
        else:
            self.pesel = ""
