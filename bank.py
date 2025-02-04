
class Bank:
    def __init__(self, name, last_name, pesel, bonus = None ):
        self.name = name
        self.last_name = last_name
        self.pesel = pesel
        self.balance = 0
        prefix = "PROM_"
        pesel = str(pesel)
        rr = pesel[:2]

        if bonus and bonus.startswith(prefix):
            if int(rr) > 60 or str(rr).startswith('0'):
                self.balance += 50


        if len(pesel) != 11:
            self.pesel = "pesel niepoprawny"
        else:
            self.pesel = pesel


