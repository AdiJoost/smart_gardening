# -*- coding: utf-8 -*-
"""
Created on Fri May  6 19:52:26 2022

@author: Adi

This is the Pump-Controller. Its a Singleton-class that will hold all 
pump-objects and handles their activation

The app will call the __init__ method and then starts a deamon-thread.

get_instance() get the instance of the singleton. Do not use Pump_controller()
as the __init__ is virtually private

"""

from models.pump_model import Pump_model
from pump import Pump
import threading
import time
from log.logger import Logger

class Pump_controller():
    __instance = None
    
    @staticmethod
    def get_instance():
        """returns the instance of the Pump_Controller"""
        if Pump_controller.__instance == None:
            Pump_controller()
        return Pump_controller.__instance
    
    def __init__(self):
        """virtually privat constructor. App will call it once"""
        if Pump_controller.__instance is not None:
            raise Exception("This constructer can olny be called by the"\
                            " the class itself")
        else:
            Pump_controller.__instance = self
            self.get_pumps()
            self.queue = []
            
    def get_pumps(self):
        """loads all pumps from database"""
        self.pump_list = {}
        all_pumps = Pump_model.get_all()
        for pump in all_pumps:
            self.pump_list[pump.id] = Pump(pump.pump_pin)
    
    def add_pump(self, pump_id, pump_pin):
        """adds a pump to the list of controllable pumps"""
        if pump_id in self.pump_list:
            return -1
        self.pump_list[pump_id] = Pump(pump_pin)
            
    def add_order(self, pump_id, duration):
        """adds an order to the list for the pump_controller to 
        execute."""
        self.queue.append((pump_id, duration))
        
    def start_deamon_thread(self):
        """starts deamon_thread to execute orders in self.queue. Deamon will
        check after given intervall for new orders and executes them"""
        self.deamon_thread = threading.Thread(target=self.run_queue)
        self.deamon_thread.start()
            
    def run_queue (self, intervall=5):
        while True:
            while len(self.queue) != 0:
                pump_order = self.queue.pop(0)
                self.run(*pump_order)
        time.sleep(intervall)
        
        
    def run(self, pump_id, duration = 10):
        try:
            self.pump_list[pump_id].activate_pump(duration)
            Logger.log(__name__, f"Pump: {pump_id} shot for "\
                       f"{duration} seconds", "pump_log.txt")
        except KeyError as e:
            Logger.log(__name__, f"KeyError: no Pump with id: {e}",
                       file="error_log.txt")
         
    