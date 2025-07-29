from CreditCard import CreditCard

card = CreditCard("Sarah", "MBC Bank", "1234 5678 9012 3456", 5000)

card.charge(1200)
card.charge(350)
card.make_payment(400)

print("\nCard Summary:")
print("Customer:", card.get_customer())
print("Bank:", card.get_bank())
print("Account:", card.get_account())
print("Limit:", card.get_limit())
print("Balance:", card.get_balance())
