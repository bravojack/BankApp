#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Transaction:
    
    def __init__(self, id_: str, customer_id: str, acc_nr: str, date: str, amount: float):
        self._id = id_
        self._customer_id = customer_id
        self._acc_nr = acc_nr
        self._date = date
        self._amount = amount
        
    def get_id(self):
        return self._id
    
    def get_customer_id(self):
        return self._customer_id
    
    def get_acc_nr(self):
        return self._acc_nr
    
    def get_date(self):
        return self._date
    
    def get_amount(self):
        return self._amount
    
    def present(self):
        """Returns a string representation of this Transaction object"""
        return f'customer id: {self._customer_id}, account number: {self._acc_nr}, date: {self._date}, amount: {self._amount}'
    

