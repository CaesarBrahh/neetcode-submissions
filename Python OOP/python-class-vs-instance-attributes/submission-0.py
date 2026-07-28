class BankAccount: 
    total_accounts = 0
    total_balance = 0
    
    def __init__(self, name, balance) -> None:
        self.name = name
        self.balance = balance

        BankAccount.total_accounts += 1
        BankAccount.total_balance += self.balance

account_1 = BankAccount("Alice", 1000)
account_2 = BankAccount("Bob", 2000)

print(f"Alice's balance: ${account_1.balance}")
print(f"Bob's balance: ${account_2.balance}")
print(f"Total Accounts: {BankAccount.total_accounts}")
print(f"Total Balance: ${BankAccount.total_balance}")

