class transaction:

    def __init__(self, date = "01/01/2023", time = "00::00::00", amount = 0, type = "none", description= "none", order=0):
        self.date = date
        self.time = time
        self.amount = amount 
        self.type = type
        self.description = description
        self.order = order
        