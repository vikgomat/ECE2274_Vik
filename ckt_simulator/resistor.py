# resistor.py
class Resistor:
    def __init__(self, name: str, bus1: str, bus2: str, r: float):
        "Initialize a resistor with name, connected buses, and resistance value"
        self.name = name
        self.bus1 = bus1
        self.bus2 = bus2
        self.__r = r  # Private resistance attribute
        self.g = self.calc_g()
    
    def calc_g(self):
        "Calculate and return the conductance value"
        if self.__r == 0:
            raise ValueError("Resistance cannot be zero (would cause infinite conductance)")
        return 1.0 / self.__r
    
    # Getter method for resistance
    def get_resistance(self):
        "Get the resistance val"
        return self.__r
    
    # Setter method for resistance
    def set_resistance(self, r: float):
        "Set the resistance"
        if r <= 0:
            raise ValueError("Resistance must be greater than zero")
        self.__r = r