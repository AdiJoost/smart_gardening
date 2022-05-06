# -*- coding: utf-8 -*-
"""
Created on Fri May  6 19:52:26 2022

@author: Adi

This is the Pump-Controller. Its a Singleton-class that will hold all 
pump-objects and handles their activation
"""

class Pump_controller():
    __instance = None
     
    @staticmethod
    def get_instance():
        if Pump_controller.__instance == None:
            Pump_controller()
        return Pump_controller.__instance
    
    def __init__(self):
        if Pump_controller.__instance is not None:
            raise Exception("This constructer can olny be called by the"\
                            " the class itself")
        else:
            Pump_controller.__instance = self