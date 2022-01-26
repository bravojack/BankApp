#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from bankapp_python.Bank import Bank
import time

class UI:
    
    def __init__(self, bank: Bank):
        self._bank = bank
    
    def run(self):
        self._show_menu()
    
    def _show_menu(self):
        while True:
            time.sleep(1)
            print("""\n\n--------------------BankApp Main Menu--------------------

1 - Exit
2 - Manage Customers
3 - Manage Accounts
4 - Make Transaction
5 - Get Information""", flush = True)
            user_input = input('Enter your choice: ')
            if user_input == '1':
                return
            elif user_input == '2':
                self._show_menu_manage_customers()
            elif user_input == '3':
                self._show_menu_manage_accounts()
            elif user_input == '4':
                self._show_menu_make_transaction()
            elif user_input == '5':
                self._show_menu_get_information()
            else:
                print('\nBad input!\n')

    def _show_menu_manage_customers(self):
        while True:
            print("""\n\n    --Manage Customers--

1 - Go back
2 - Add a customer
3 - Remove a customer
4 - Change name of a customer""", flush = True)
            user_input = input('Enter your choice: ')
            
            if user_input == '1':
                return
            elif user_input == '2':
                self._add_customer()
                return
            elif user_input == '3':
                self._remove_customer()
                return
            elif user_input == '4':
                self._change_name_of_customer()
                return
            else:
                print('\nBad input!\n')
        
    def _show_menu_manage_accounts(self):
        while True:
            print("""\n\n    --Manage Accounts--

1 - Go back
2 - Open an account
3 - Close an account""", flush = True)
            user_input = input('Enter your choice: ')
            if user_input == '1':
                return
            elif user_input == '2':
                self._open_account()
                return
            elif user_input == '3':
                self._close_account()
                return
            else:
                print('\nBad input!\n')
        
    def _show_menu_make_transaction(self):
        while True:
            print("""\n\n    --Make Transaction--

1 - Go back
2 - Deposit into account
3 - Withdraw from account""", flush = True)
            user_input = input('Enter your choice: ')
            
            if user_input == '1':
                return
            elif user_input == '2':
                self._make_deposit()
                return
            elif user_input == '3':
                self._make_withdrawal()
                return
            else:
                print('\nBad input!\n')

    def _show_menu_get_information(self):
        while True:
            print("""\n\n    --Get Information--
        
1 - Go back
2 - Show all customers in bank
3 - Show information about one customer
4 - Show information about an account
5 - Show all transactions of a specific account""", flush = True)
            user_input = input('Enter your choice: ')
            if user_input == '1':
                return
            elif user_input == '2':
                self._show_all_customers()
                return
            elif user_input == '3':
                self._show_one_customer()
                return
            elif user_input == '4':
                self._show_account()
                return
            elif user_input == '5':
                self._show_transactions_of_specific_account()
                return
            else:
                print('\nBad input!\n')
    
    def _add_customer(self):
        print('\n    --Add Customer--\n', flush = True)
        first_name = input('First name: ')
        last_name = input('Last name: ')
        ssn = input('Social security number: ')
        customer_was_added = self._bank.add_customer(first_name, last_name, ssn)
        if customer_was_added:
            print('Customer successfully added.')
        else:
            print('Customer could not be added')
    
    def _remove_customer(self):
        print('\n    --Remove Customer--\n', flush = True)
        ssn = input('Social security number of customer to be removed: ')
        result = self._bank.remove_customer(ssn)
        could_be_removed = result[0]
        if could_be_removed:
            for index, element in enumerate(result):
                if not index == 0:
                    print(element)
        else:
            print('Customer could not be added')
        
    def _change_name_of_customer(self):
        print('\n    --Change Name of Customer--\n', flush = True)
        ssn = input('Social security number of customer to be updated: ')
        for customer in self._bank.get_customers():
            if ssn == customer.get_ssn():
                print(f'Customer found: {customer.get_first_name()} {customer.get_last_name()}')
        first_name = input('Enter first name: ')
        last_name = input('Enter last name: ')
        customer_was_updated = self._bank.change_customer_name(first_name, last_name, ssn)
        if customer_was_updated:
            print('Customer successfully updated.')
        else:
            print('Customer could not be updated')
    
    def _open_account(self):
        print('\n    --Open New Account--\n', flush = True)
        ssn = input('Social security number of customer that will open a new account: ')
        result = self._bank.add_account(ssn)
        if result == -1:
            print('Account could not be created')
        else:
            print(f'Account with account number: {result} was successfully created for customer')
    
    def _close_account(self):
        print('\n    --Close Account--\n', flush = True)
        ssn = input('Social security number of customer that will close an account: ')
        acc_nr = input('Account number of account that will be closed: ')
        print(self._bank.close_account(ssn, acc_nr))
        
    def _make_deposit(self):
        print('\n    --Make Deposit--\n', flush = True)
        ssn = input('Social security number of customer that will make a deposit: ')
        acc_nr = input('Account number of account that will be deposited into: ')
        amount = input('Amount to deposit: ')
        deposit_was_made = self._bank.deposit(ssn, acc_nr, float(amount))
        if deposit_was_made:
            print('Deposit was successful.')
        else:
            print('Deposit was not successful')
        
    def _make_withdrawal(self):
        print('\n    --Make Withdrawal--\n', flush = True)
        ssn = input('Social security number of customer that will make a withdrawal: ')
        acc_nr = input('Account number of account that will be withdrawn from: ')
        amount = input('Amount to withdraw: ')
        withdrawal_was_made = self._bank.deposit(ssn, acc_nr, -float(amount))
        if withdrawal_was_made:
            print('Withdrawal was successful.')
        else:
            print('Withdrawal was not successful')
        
    def _show_all_customers(self):
        print('\n    --All customers--\n', flush = True)
        
        customers = self._bank.get_customers()
        for customer in customers:
            print(f'First name: {customer.get_first_name()}')
            print(f'Last name: {customer.get_last_name()}')
            print(f'Social security number: {customer.get_ssn()}\n')
        
    def _show_one_customer(self):
        print('\n    --Show info about a customer--\n', flush = True)
        ssn = input('Social security number of customer to be displayed: ')
        print('')
        result = self._bank.get_customer(ssn)
        for line in result:
            print(line)
        
    def _show_account(self):
        print('\n    --Show info about an account--\n', flush = True)
        ssn = input('Social security number of customer that owns the account: ')
        acc_nr = input('Account number of account to be displayed: ')
        print(self._bank.get_account(ssn, acc_nr))
        
    def _show_transactions_of_specific_account(self):
        print('\n    --Show Transactions of a Specific Account--\n')
        ssn = input('Social security number of customer: ')
        print('')
        customer_info = self._bank.get_customer(ssn)
        for line in customer_info:
            print(line)
        acc_nr = input('Show transactions for this account number: ')
        print('')
        print(self._bank.get_all_transactions_by_ssn_acc_nr(ssn, acc_nr))