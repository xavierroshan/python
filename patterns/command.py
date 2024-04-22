#Receiver
class Light:
    def turnon(self):
        print("Turn on lights")
    def turnoff(self):
        print("Turn off lights")   


# Command Interface
class Command:
    def execute(self):
        pass
#Concrete command class   
class LightsOn(Command):
    def __init__(self, light):
        self.light = light
    def execute(self):
        self.light.turnon()
#Concrete command class   
class LightsOff(Command):
    def __init__(self, light):
        self.light = light
    def execute(self):
        self.light.turnoff()
#Remote
class Remote:
    def __init__(self):
        self.commandlist = []
    def add_command(self, command):
        if command not in self.commandlist:
            self.commandlist.append(command)
    def execute_command(self):
        for command in self.commandlist:
            command.execute()

light = Light()     
lights_on = LightsOn(light)
lights_off = LightsOff(light)
remote = Remote()
remote.add_command(lights_on)
remote.add_command(lights_off)
remote.execute_command()
        
        
        
        