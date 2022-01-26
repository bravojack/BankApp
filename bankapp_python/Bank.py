#!/usr/bin/env python
# coding: utf-8

# In[31]:

from bankapp_python.Customer import Customer
from bankapp_python.Account import Account
from bankapp_python.Transaction import Transaction
from bankapp_python.CustomerManager import CustomerManager
from bankapp_python.TransactionManager import TransactionManager
import datetime

class Bank:
    
    def __init__(self):
        self._cm = CustomerManager('data/customers.txt')
        self._tm = TransactionManager('data/transactions.txt')
        self._customers = []
        self._transactions = []
        self._next_assignable_customer_id = 111111
        self._next_assignable_acc_nr = 1001
        self._next_assignable_transaction_id = 1
        self._load()
        
    def _load(self):
        """Populates instance lists

        Populates customer list
        Populates transaction list
        Updates next assignable id according to customer list
        Updates next assignable account number according to customer list
        Updates next assignable transaction number according to transaction list
        """
        self._customers = self._cm.get_all()
        self._transactions = self._tm.get_all()
        self._update_next_assignable_variables()
        
    def _update_next_assignable_variables(self):
        """Checks what the highest value of every value in the text-file is and sets the next assignable variables to be one higher than that.
        
        Default starting values:
        _next_assignable_customer_id = 111111
        _next_assignable_acc_nr = 1001
        _next_assignable_transaction_id = 1
        """
        next_customer_id = self._next_assignable_customer_id
        next_acc_nr = self._next_assignable_acc_nr
        next_transaction_id = self._next_assignable_transaction_id
        
        for customer in self._customers:
            if int(customer.get_id()) >= next_customer_id:
                next_customer_id = int(customer.get_id()) + 1
            for account in customer.get_accounts():
                if int(account.get_acc_nr()) >= next_acc_nr:
                    next_acc_nr = int(account.get_acc_nr()) + 1
        for transaction in self._transactions:
            if int(transaction.get_id()) >= next_transaction_id:
                next_transaction_id = int(transaction.get_id())
                    
        self._next_assignable_customer_id = next_customer_id
        self._next_assignable_acc_nr = next_acc_nr
        self._next_assignable_transaction_id = next_transaction_id
    
    def _save_transaction(self, customer_id: str, acc_nr: str, amount: float):
        """Saves transaction as a transaction object in the transactions list"""
        now = datetime.datetime.now()
        self._tm.add_transaction(Transaction(self._next_assignable_transaction_id, customer_id, acc_nr, now.strftime("%x"), amount))
        self._next_assignable_transaction_id += 1
        self._load()
    
    def get_customers(self):
        """Returns a tuple of all customers"""
        return tuple(self._customers)

    def add_customer(self, f_name: str, l_name: str, ssn: str):
        """Creates a Customer object and adds it to the _customer list
        
        Creates a customer if a customer with the passed ssn does not exist in the customer list
        Returns True if a new customer was created
        Returns False if a new customer could not be created
        """
        can_be_created = True
        if self._customers:
            for customer in self._customers:
                if ssn == customer.get_ssn():
                    can_be_created = False
        if not can_be_created:
            return False
        new_customer = Customer(self._next_assignable_customer_id, f_name, l_name, ssn, [])
        self._cm.add_customer(new_customer)
        self._load()
        return True
        
    def get_customer(self, ssn: str):
        """Returns a tuple with information about the customer with the ssn passed as argument"""
        customer_info = ['No matching customer'] # Sets error message as first value
        for customer in self._customers:
            if ssn == customer.get_ssn():
                customer_info[0] = f'{customer.get_first_name()} {customer.get_last_name()} {customer.get_ssn()}' # Replaces error message with customer information if customer was found
                if customer.get_accounts(): # Makes sure list is not empty
                    for account in customer.get_accounts():
                        customer_info.append(account.present())
                else:
                    customer_info.append('No accounts')
            
        return tuple(customer_info)
    
    def change_customer_name(self, f_name: str, l_name: str, ssn: str):
        """Attempts to change the name of the customer with the passed ssn
        
        Returns True if successful
        Returns False if not succesful
        """
        customer_found = False
        for customer in self._customers:
            if ssn == customer.get_ssn():
                customer.change_name(f_name, l_name)
                self._cm.update_customer(customer)
                customer_found = True
        self._load()
        return customer_found
    
    def remove_customer(self, ssn: str):
        """Removes customer from list of customers if customer with passed ssn exists"""
        customer_found = False
        customer_index = -1
        toReturn = ['Customer not found']
        
        for index, customer in enumerate(self._customers):
            if ssn == customer.get_ssn():
                customer_found = True
                customer_index = index
                toReturn[0] = f'{customer.get_first_name()} {customer.get_last_name()} was removed'
                for account in customer.get_accounts():
                    toReturn.append( self.close_account(ssn, account.get_acc_nr()) )
        self._cm.remove_by_id(self._customers[customer_index].get_id())
        self._load()
        return tuple(toReturn)
    
    def add_account(self, ssn: str):
        """Adds a new account to the customer if the customer exists
        
        Returns the new account number if successful
        Returns -1 if not successful
        """
        customers = self._customers
        for customer in customers:
            if ssn == customer.get_ssn():
                new_acc_nr = self._next_assignable_acc_nr
                customer.add_account(str(new_acc_nr))
                self._cm.update_customer(customer)
                self._load()
                return new_acc_nr
        return -1
    
    def get_account(self, ssn: str, acc_nr: str):
        """Returns a textual representation of an account
        
        Returns appropiate informative error message if unsuccessful
        """
        for customer in self._customers:
            if ssn == customer.get_ssn():
                for account in customer.get_accounts():
                    if acc_nr == account.get_acc_nr():
                        return account.present()
                    else:
                        return 'The specified customer does not have an account with the specified account number'
        return 'Could not find a customer with the specified Social Security Number'
    
    def deposit(self, ssn: str, acc_nr: str, amount: float):
        """Makes a deposit of the specified amount to the specified account
        
        Returns True if successful
        Returns False if not successful
        """
        deposit_successful = False
        customers = self._customers
        for customer in customers:
            if ssn == customer.get_ssn():
                for account in customer.get_accounts():
                    if acc_nr == account.get_acc_nr():
                        account.deposit(amount)
                        deposit_successful = True
                        self._save_transaction(customer.get_id(), acc_nr, amount)
                        self._cm.update_customer(customer)
                        self._load()
        return deposit_successful
    
    def withdraw(self, ssn: str, acc_nr: str, amount: float):
        """Makes a withdrawal of the specified amount from the specified account
        
        Returns True if successful
        Returns False if not successful
        """
        withdrawal_successful = False
        customers = self._customers
        for customer in customers:
            if ssn == customer.get_ssn():
                for account in customer.get_accounts():
                    if acc_nr == account.get_acc_nr():
                        if account.withdraw(amount):
                            withdrawal_successful = True
                            self._save_transaction(customer.get_id(), acc_nr, -amount)
                            self._cm.update_customer(customer)
                            self._load()
        return withdrawal_successful
    
    def close_account(self, ssn: str, acc_nr: str):
        """Closes the specified account
        
        Returns a textual presentation of the accounts balance
        Returns an error message if specified customer or account does not exist
        """
        to_return = 'Customer not found'
        account_found = False
        customers = self._customers
        for customer in customers:
            if ssn == customer.get_ssn():
                found_acc_nr = -1
                for account in customer.get_accounts():
                    if acc_nr == account.get_acc_nr():
                        account_found = True
                        found_acc_nr = acc_nr
                        to_return = f'Account with account number {account.get_acc_nr()} was closed. Balance of account: {account.get_balance()}'
                if account_found:
                    customer.remove_account(found_acc_nr)
                    self._cm.update_customer(customer)
                    self._load()
                else:
                    to_return = 'Error: Customer found, but not account'
        return to_return
    
    def get_all_transactions_by_ssn_acc_nr(self, ssn: str, acc_nr: str):
        """Returns a tuple with all transactions belonging to the account that matches the passed ssn and account number"""
        customer_id = -1
        for customer in self.get_customers():
            if ssn == customer.get_ssn():
                customer_id = customer.get_id()
        if customer_id == -1:
            return 'Customer could not be found'
        all_transactions = self._tm.get_all()
        to_return = ''
        for transaction in all_transactions:
            if customer_id == transaction.get_customer_id() and acc_nr == transaction.get_acc_nr():
                to_return += transaction.present() + '\n'
        return to_return