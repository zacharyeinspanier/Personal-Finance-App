class transaction:

    def __init__(self, date, time, amount, type, description, order=0):
        self.date = date
        self.time = time
        self.amount = amount 
        self.type = type
        self.description = description
        self.order = order
        