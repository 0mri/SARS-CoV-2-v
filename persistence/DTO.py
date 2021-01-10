class Vaccine:
    def __init__(self, vac_id, date, sup, quantity):
        self.id = vac_id
        self.date = date
        self.supplier = sup
        self.quantity = 0


class Supplier:
    def __init__(self, id, name, logistic):
        self.id = id
        self.name = name
        self.contact_information = contact_information


class Clinic:
    def __init__(self, id, location, demand, logistic):
        self.id = id
        self.location = location
        self.demand = demand
        self.logistic = logistic


class Logistic:
    def __init__(self, id, name, sent, recieved):
        self.id = id
        self.name = name
        self.sent = sent
        self.recieved = recieved
