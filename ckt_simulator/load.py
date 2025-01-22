# load.py
class Load:
    def __init__(self, name: str, bus1: str, p: float, q: float):
        "Initialize a load with name, connected bus, active and reactive power"
        self.name = name
        self.bus1 = bus1
        self.p = p  # Active power
        self.q = q  # Reactive power
        self.g = self.calc_g()
    
    def calc_g(self):
        nominal_v = 1.0
        return self.p / (nominal_v ** 2)
    
     