class Checkout:

    def __init__(self) -> None:
        self.items = []
        self.prices = {}
        self.discounts = None
        self.total = 0
    
    def addItemPrice(self, item, price):
        self.prices[item] = price

    def addItem(self, item):
        self.items.append(item)
        self.total += self.prices[item]

    def calculateTotal(self):
        for item in list(set(self.items)):
            try:
                if self.discounts[item]:
                    pass
                if self.items.count(item) % self.discounts[item][0] == 0:
                    multplier = int(self.items.count(item)/self.discounts[item][0])
                    # if multplier < 1:
                    #     multplier = 1                
                    self.total -= self.items.count(item)*self.prices[item]
                    print(multplier)
                    self.total += self.discounts[item][1]*multplier
            except:
                continue
        return self.total

    def addDiscount(self, item, number_items, price):
        if self.discounts == None:
            self.discounts = {}
        self.discounts[item] = (number_items, price)
    
        