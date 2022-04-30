#import RPi.GPIO as GPIO
import time

class Pump():
    
    is_setup = False
    
    def __init__(self, pump_pin: int):
        self.pump_pin = pump_pin
        if not Pump.is_setup:
            Pump.setup_board()
        self.set_pin()
        
    def set_pin(self):
#        GPIO.setup(self.pump_pin, GPIO.OUT)
        return (f"Pin {self.pump_pin} is set")
    
    def pull_up(self):
#        GPIO.output(self.pump_pin, 1)
        return (f"Pin {self.pump_pin} is high")
        
    def pull_down(self):
#        GPIO.output(self.pump_pin, 0)
        return (f"Pin {self.pump_pin} is low")
        
    def activate_pump(self, seconds: int) -> str:
        self.pull_up()
        time.sleep(seconds)
        self.pull_down()
        return f"pump {self.pump_pin} has shot"
        
        
    @classmethod
    def setup_board(cls):
 #       GPIO.setmode(GPIO.BCM)
        return "GPIO Board is setup in BCM mode"
    
    @classmethod
    def shut_board():
#        GPIO.cleanup()
        return "GPIO Board is clean"
    