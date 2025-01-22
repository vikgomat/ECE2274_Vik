# bus.py
class Bus:
    def __init__(self, name: str):
        """Initialize a bus with a name and default voltage of 0."""
        self.name = name
        self.__v = 0.0
    
    def set_bus_v(self, bus_v: float):
        """Set the voltage at the bus."""
        self.__v = bus_v
    
    def get_bus_v(self):
        """Set the voltage at the bus."""
        return self.__v
    
