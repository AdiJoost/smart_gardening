# -*- coding: utf-8 -*-
"""
Created on Fri May  6 19:52:26 2022

@author: Adi

This is the Pump-Controller. Its a Singleton-class that will hold all 
pump-objects and handles their activation
"""

from models.pump_model import Pump_model
from pump import Pump

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
            self.get_pumps()
            self.queue = []
            
    def get_pumps(self):
        self.pump_list = {}
        all_pumps = Pump_model.get_all()
        for pump in all_pumps:
            self.pump_list[pump.id] = Pump(pump.pump_pin)
            
    def add_order(self, pump_pin, duration):
        self.queue.append((pump_pin, duration))
        
            
    def run_queue (self):
        while len(self.queue) is not 0:
            pump_order = self.queue.pop(0)
            self.run(*pump_order)
            
    def run(self, pump_id, duration = 10):
        self.pump_list[pump_id].activate_pump(duration)
        
    