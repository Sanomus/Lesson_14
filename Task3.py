import random

class Account:
    def __init__(self, account_number: str, balance: float):
        self.account_number = account_number
        self.balance = balance

    @classmethod
    def create_account(cls, account_number):
        return cls(account_number, 0.0)
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError('Amount must be positive')

    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount
        else:
            raise ValueError('Amount must be positive')

    def get_balance(self):
        return self.balance
    
    def get_account_number(self):
        return self.account_number
    
    def __str__(self):
        return f'Account number: {self.account_number}, balance: {self.balance}'

    
class SavingsAccount(Account):
    def __init__(self, account_number: str, balance: float, interest: float):
        super().__init__(account_number, balance)
        self.interest = interest

    @classmethod
    def create_account(cls, account_number, interest):
        return cls(account_number, 0.0, interest)

    def add_interest(self):
        # adds interest to the account
        self.balance = self.balance + self.balance * self.interest
        pass

class CurrentAccount(Account):
    def __init__(self, account_user: str, balance: float,  overdraft_limit: float):
        super().__init__(account_user, balance)
        self.overdraft_limit = overdraft_limit

    @classmethod
    def create_account(cls, account_number, overdraft_limit):
        return cls(account_number, 0.0, overdraft_limit)


class Bank:
    def __init__(self, accounts: list[Account]):
        self.accounts = accounts

    def print_all_account_state(self):
        for account in self.accounts:
            print(account)

    
    def get_all_accounts_name(self):
        list_of_account_name = []
        for account in self.accounts:
            list_of_account_name.append(account.account_number)
        return list_of_account_name
    
    def get_all_accounts_types(self):
        list_of_account_types = []
        for account in self.accounts:
            list_of_account_types.append(account.__class__.__name__)
        return list_of_account_types
    
    def get_account_by_name(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
    
    def get_account_by_type(self, account_type):
        for account in self.accounts:
            if account.__class__.__name__ == account_type:
                return account

    def update_account(self):
        for account in self.accounts:
            if isinstance(account, SavingsAccount):
                account.add_interest()
            elif isinstance(account, CurrentAccount):
                if account.get_balance() < 0:
                    print('send')
    
    def open_account(self, account_type, account_number):
        if account_type == Account.__name__:
            account = Account.create_account(account_number)
            bank.accounts.append(account)
        if account_type == SavingsAccount.__name__:
            interest = random.choice(list(range(5, 15)))/100 
            account = SavingsAccount.create_account(account_number, interest)
            bank.accounts.append(account)
        if account_type == CurrentAccount.__name__:
            overdraft = random.choice(list(range(100, 500, 100))) * -1
            account = CurrentAccount.create_account(account_number, overdraft)
            bank.accounts.append(account)

    def close_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                self.accounts.pop(self.accounts.index(account))

    def pay_dividend(self, income):
        for account in self.accounts:
            account.balance += income


print([cls.__name__ for cls in Account.__subclasses__()])
    


bank = Bank([])

account_types = [Account.__name__] + [cls.__name__ for cls in Account.__subclasses__()]
print('types', account_types)
accounts_quantity = random.randint(5, 15)

for i in range(accounts_quantity):
    account_type = random.choice(account_types)
    if account_type == Account.__name__:

        account = Account.create_account(i)
        bank.accounts.append(account)
    if account_type == SavingsAccount.__name__:
        interest = random.choice(list(range(5, 15)))/100 
        account = SavingsAccount.create_account(i, interest)
        bank.accounts.append(account)
    if account_type == CurrentAccount.__name__:
        overdraft = random.choice(list(range(100, 500, 100))) * -1
        account = CurrentAccount.create_account(i, overdraft)
        bank.accounts.append(account)

print(bank.get_all_accounts_types())
my_account = bank.get_account_by_type('CurrentAccount')
my_account.withdraw(1000)
bank.update_account()
bank.open_account(SavingsAccount.__name__, 'New_acc')
print(bank.get_all_accounts_name())
bank.close_account('New_acc')
print(bank.get_all_accounts_name())
print('before devidents payment')
bank.print_all_account_state()
bank.pay_dividend(100)
print('after devidents payment')
bank.print_all_account_state()

