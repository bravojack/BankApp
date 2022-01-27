#!/usr/bin/env python
# coding: utf-8

# In[3]:


from bankapp_python.Customer import Customer
from bankapp_python.Account import Account
from bankapp_python.DataSource import DataSource

class CustomerManager(DataSource):
    
    def _write_to_file(self, customers: tuple):
        """Takes a tuple with customer objects as argument and writes over file
        
        Format used: 'c:c:c:c#a:a:a#a:a:a' where 'c' represents attributes of the customer in order: id, first name, last name, social security number; and where 'a' represents attributes of account in order: account number, account type, account balance.
        The elements are separated by the symbol: ':'
        The information groups are separated by the symbol: '#'
        The first information group is always the customer information
        There can be zero or many accounts represented by information groups
        """
        to_write = ''
        for customer in customers:
            to_write += f'{customer.get_id()}:{customer.get_first_name()}:{customer.get_last_name()}:{customer.get_ssn()}'
            for account in customer.get_accounts():
                to_write += f'#{account.get_acc_nr()}:{account.get_acc_type()}:{account.get_balance()}'
            to_write += '\n'
        with open(self._file_name, 'wt') as f:
            f.write(to_write)
    
    def get_all(self):
        """Returns a list with customer objects that has been read and translated from source file"""
        with open(self._file_name, 'rt') as f:
            lines = f.read().split('\n')
        lines.pop() #remove last item which is empty due to file_as_string always ending with a '\n'
        customers = []
        for line in lines:
            customer_id = ''
            f_name = ''
            l_name = ''
            ssn = ''
            accounts = []
            info_groups = line.split('#')
            for index, info_group in enumerate(info_groups):
                elements = info_group.split(':')
                if index == 0:
                    customer_id = elements[0]
                    f_name = elements[1]
                    l_name = elements[2]
                    ssn = elements[3]
                else:
                    acc_nr = elements[0]
                    acc_type = elements[1]
                    acc_balance = float(elements[2])
                    accounts.append(Account(acc_nr, acc_type, acc_balance))
            customers.append(Customer(customer_id, f_name, l_name, ssn, accounts))
        return customers
    
    def add_customer(self, new_customer: Customer):
        """Takes a new customer as argument and adds it to the list of customers, and writes over the file with the new list
        
        Returns the added customer
        """
        customers = self.get_all()
        customers.append(new_customer)
        self._write_to_file(customers)
        return new_customer
    
    def update_customer(self, updated_customer: Customer):
        """Updates a customer in the list and writes over the file with the updated list
        
        Returns list of customers if customer could be found
        Returns -1 if customer could not be found
        """

        if self.find_by_id(updated_customer.get_id()) == -1:
            return -1
        
        customers = self.get_all()
        found_index = -1
        for index, customer in enumerate(customers):
            if updated_customer.get_id() == customer.get_id():
                found_index = index
        customers[found_index] = updated_customer
        self._write_to_file(tuple(customers))
        return customers[found_index]
    
    def find_by_id(self, customer_id: str):
        """Takes a customer id as argument and returns customer if found
        
        Returns -1 if customer could not be found
        """
        for customer in self.get_all():
            if customer_id == customer.get_id():
                return customer
        return -1
    
    def remove_by_id(self, customer_id: str):
        """Takes a customer id as argument and removes customer from file if found
        
        Returns -1 if customer was not found
        Returns the deleted customer if customer was found
        """
        customers = self.get_all()
        found_index = -1
        for index, customer in enumerate(customers):
            if customer_id == customer.get_id():
                found_index = index
        if found_index == -1:
            return -1
        deleted_customer = customers[found_index]
        del customers[found_index]
        self._write_to_file(customers)
        return deleted_customer

