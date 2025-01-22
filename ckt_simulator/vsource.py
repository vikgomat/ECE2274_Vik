# vsource.py
class Vsource:
    def __init__(self, name: str, bus1: str, v: float):
        "Initialize a voltage source with name, connected bus, and voltage value"
        self.name = name
        self.bus1 = bus1
        self.v = v
    