class Account:
    def __init__(self, name):
        self.__account_name: str = name
        self.__account_balance: float = 0

        """
        Account class created acount balence defults to 0 
        """

    def deposit(self, amount):

        if amount <= 0:
            return False
        else:
            self.__account_balance += self.amount
            return True

    def withdraw(self, amount):

        if amount <= 0:
            return False
        else:
            self.__account_balance -= self.amount
            return True

        '''
        Cannot withdaw or deposit less than or = 0 
        changes the current account balance
        '''

    def get_balance(self):
        return self.__account_balance

    def get_name(self):
        return self.__account_name
        '''
        Return the Current account balance as well as name
        '''