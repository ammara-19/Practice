class CreditCard:
    def __init__ (self, customer, bank, account, limit):
        self.customer = customer
        self.bank = bank
        self.account = account
        self.limit = limit
        self.balance = 0

    def get_customer (self):
        return self.customer
    def get_bank (self):
        return self.bank
    def get_account (self):
        return self.account
    def get_limit (self):
        return self.limit
    def get_balance (self):
        return self.balance
    
    def charge (self, price):
        if price + self.balance > self.limit:
            return False
        else:
            self.balance += price
            return True
        
    def make_payment (self, amount):
        if amount < 0:
            raise ValueError ("Payment amount must be positive")
        self.balance -= amount

    