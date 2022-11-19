class Account:
    def __init__(self, name):
        '''
        :param __account_name: provides a name for an account expected a string
        :param __account_balance: acount balance defults to 0

        '''
        self.__account_name: str = name
        self.__account_balance: float = 0

    def deposit(self, amount):
        '''
        Function to deposit money

        :param amount: how much to deposit
        :param return: returns a bool value to show if deposit was successful

        '''
        if amount <= 0:
            return False
        else:
            self.__account_balance += self.amount
            return True

    def withdraw(self, amount):
        '''
        Function to withdraw money

        :param amount: how much to withdraw
        :param return: returns a bool value to show if withdraw was successful

        '''
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
        '''

        :param __account_balance: lets us access the current balance

        '''
        return self.__account_balance

    def get_name(self):
        '''
        
        :param __account_name: lets us access the current name

        '''
        return self.__account_name
       
