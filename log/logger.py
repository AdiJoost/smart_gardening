# -*- coding: utf-8 -*-
"""
Created on Sun May 15 11:28:36 2022

@author: AdiJo
"""
import os.path
from datetime import date


#This is a simple log system - it is not thread-safe!
def log_entry(prefix: str, message: str, file="main_log.txt"):
    entry = f"[{prefix}] {message}"
    if not os.path.exists(file):
        with open(file, "w", encoding=("UTF-8")) as f:
            f.write("Log-File for smart-gardening-system. Created:"\
                    f" {date.today().isoformat()}\n\n")
    with open(file, "a", encoding=("UTF-8")) as f:
        f.write(f"{entry} -- {date.today().isoformat()}\n")
        
        