#State Pattern
from abc import ABC, abstractmethod

# context
class LightSwitch:
    def __init__(self):
        self.state = StateOff()
        
    def set_state(self, state):
        self.state = state
        
    def turn_on (self):
        self.state.turn_on()
        
    def turn_off(self):
        self.state.turn_off()
        
        
#State Interface

class State(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    @abstractmethod
    def turn_off(self):
        pass
    
#Concrete State

class StateOff(State):
    def turn_off(self):
        print("Lights already turned off")
    def turn_on(self):
        print("turning on light")
        light_switch.set_state(StateOn())
        
class StateOn(State):
    def turn_on(self):
        print("Lights already turned on")
    def turn_off(self):
        print("turning off light")
        light_switch.set_state(StateOff())
        
light_switch = LightSwitch()
light_switch.turn_off()
light_switch.turn_on()
light_switch.turn_off()
light_switch.turn_on()
light_switch.turn_off()

    