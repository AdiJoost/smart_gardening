# -*- coding: utf-8 -*-
"""
Created on Sun May 15 11:28:36 2022

@author: AdiJo
"""
import os.path
from datetime import datetime

class Logger():
    def __init__(self):
        pass
    
    #This is a simple log system - it is not thread-safe!
    @classmethod
    def log(cls,prefix: str, message: str, file="main_log.txt"):
        entry = f"[{prefix}] {message}"
        #create correct path to file
        my_path = os.getcwd().split("smart_gardening", 1)[0]
        my_path = os.path.join(my_path, "smart_gardening", "log", file)
        
        #write to file
        if not os.path.exists(my_path):
            with open(my_path, "w", encoding=("UTF-8")) as f:
                f.write("Log-File for smart-gardening-system. Created:"\
                        f" {datetime.today().isoformat()}\n\n")
        with open(my_path, "a", encoding=("UTF-8")) as f:
            f.write(f"{entry} -- {datetime.today().isoformat()}\n")
