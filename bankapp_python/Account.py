#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Account:
    
    def __init__(self, unique_acc_nr, acc_type, balance):
        self._acc_nr = unique_acc_nr
        self._acc_type = acc_type
        self._balance = balance
    
    def get_acc_nr(self):
        """Returns the account number of an Account object"""
        return self._acc_nr
    
    def get_acc_type(self):
        """Returns the type of the account"""
        return self._acc_type
    
    def get_balance(self):
        """Returns the current balance of the Account object"""
        return self._balance
    
    def deposit(self, amount: float):
        """Increases the balance of the Account object by the amount passed to the method"""
        self._balance += amount
        
    def withdraw(self, amount: float):
        """Withdraws the amount from the balance of the Account object if there are sufficient funds
        
        Returns True if successful
        Returns False if not successful
        """
        if self._balance >= amount:
            self._balance -= amount
            return True
        else:
            return False
        
    def present(self):
        """Returns a string representation of the Account object's properties"""
        presentation = (
            f'Account number: {self._acc_nr}, '
            f'Account type: {self._acc_type}, '
            f'Balance: {self._balance}'
        )
        return presentation
    

