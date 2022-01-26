#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bankapp_python.Account import Account

class Customer:
    
    def __init__(self, id_: str, f_name: str, l_name: str, ssn: str, accounts: []):
        self._id = id_
        self._first_name = f_name
        self._last_name = l_name
        self._ssn = ssn
        self._accounts = accounts
    
    def change_name(self, f_name: str, l_name: str):
        """Sets first and last name of the Customer object to the corresponding passed arguments"""
        self._first_name = f_name
        self._last_name = l_name
    
    def add_account(self, unique_acc_nr: str):
        """Adds a new account with the passed account number to the Customer object's list of accounts"""
        new_account = Account(unique_acc_nr, 'Debit', 0.0)
        self._accounts.append(new_account)
    
    def remove_account(self, acc_nr: str):
        """Removes account with the passed account-number from the Customer object's list of accounts"""
        account_found = False
        found_index = -1
        for index, account in enumerate(self._accounts):
            if account.get_acc_nr() == acc_nr:
                found_index = index
                account_found = True
        if account_found:
            self._accounts.__delitem__(found_index)
            
    def get_id(self):
        """Returns the id of the Customer object"""
        return self._id

    def get_first_name(self):
        """Returns the first-name attribute of the Customer object"""
        return self._first_name

    def get_last_name(self):
        """Returns the last-name attribute of the Customer object"""
        return self._last_name

    def get_ssn(self):
        """Returns the Social Security Number of the Customer object"""
        return self._ssn
    
    def get_accounts(self):
        """Returns a tuple with the accounts belonging to the Customer object"""
        return tuple(self._accounts)
                

