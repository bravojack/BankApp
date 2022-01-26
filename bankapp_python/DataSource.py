#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from bankapp_python.Customer import Customer
from bankapp_python.Account import Account

class DataSource:
    
    def __init__(self, file_name: str):
        self._file_name = file_name
    
    def datasource_conn(self):
        try:
            f = open("self._file_name")
            ds = (True, "Connection successful", "self._file_name")
        except:
            ds = (False, "Connection failed", "self._file_name")
        finally:
            f.close("self._file_name")
        return ds