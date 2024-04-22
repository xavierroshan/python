# inches class
class Inches_measurement:
    def get_inches_info(self):
        return 5
#adaptor interface        
class measurement_system:
    def get_measurement_info(self):
        pass
#concrete class    
class Inches_to_cms(measurement_system):
    def __init__(self,inches_measurement):
        self.inches_measurement = inches_measurement
        
    def get_measurement_info(self):
        return self.inches_measurement.get_inches_info()*2.5
        
inches_measurement =   Inches_measurement()
inches_to_cms = Inches_to_cms(inches_measurement)
print(inches_to_cms.get_measurement_info())
