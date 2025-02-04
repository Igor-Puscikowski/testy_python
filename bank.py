
class Bank:
    def __init__(self, name, last_name, pesel, bonus = None ):
        self.name = name
        self.last_name = last_name
        self.pesel = pesel
        self.balance = 0
        prefix = "PROM_"

        if bonus and bonus.startswith(prefix):
            self.balance += 50

        pesel = str(pesel)
        if len(pesel) != 11:
            self.pesel = "pesel niepoprawny"
        else:
            self.pesel = ""
