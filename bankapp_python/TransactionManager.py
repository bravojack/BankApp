#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from bankapp_python.DataSource import DataSource
from bankapp_python.Transaction import Transaction

class TransactionManager(DataSource):
    
    def get_all(self):
        """Returns a list with Transaction objects that has been read and translated from source file"""
        with open(self._file_name, 'rt') as f:
            lines = f.read().split('\n')
        lines.pop() #remove last item which is empty due to file_as_string ending with \n
        transactions = []
        for line in lines:
            id_ = ''
            customer_id = ''
            account_id = ''
            date = ''
            amount = ''
            transaction_info = line.split(':')
            for index, element in enumerate(transaction_info):
                if index == 0:
                    id_ = element
                elif index == 1:
                    customer_id = element
                elif index == 2:
                    account_id = element
                elif index == 3:
                    date = element
                elif index == 4:
                    amount = element
            transactions.append(Transaction(id_, customer_id, account_id, date, float(amount)))
        return tuple(transactions)

    def add_transaction(self, new_transaction: Transaction):
        """Appends the passed transaction to the end of the file with the format 'id:customer_id:acc_nr:date:amount"""
        to_write = f'{new_transaction.get_id()}:{new_transaction.get_customer_id()}:{new_transaction.get_acc_nr()}:{new_transaction.get_date()}:{new_transaction.get_amount()}\n'
        with open(self._file_name, 'at') as f:
            f.write(to_write) # Appends to the end of the file