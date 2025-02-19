from typing import Dict, List
from bus import Bus
from resistor import Resistor
from load import Load
from vsource import Vsource

class Circuit:
    def __init__(self):
        "Init empty circuit"
        self.buses: Dict[str, Bus] = {}
        self.resistors: List[Resistor] = []
        self.loads: Dict[str, Load] = {}
        self.vsources: Vsource

    def add_bus(self, name: str):
        "Add a bus "
        if name in self.buses:
            raise ValueError(f"Bus {name} already exists")
        self.buses[name] = Bus(name)

    def add_resistor_element(self, name: str, bus1: str, bus2: str, r: float):
        "Add a resistor"
        # Check if buses exist
        if bus1 not in self.buses or bus2 not in self.buses:
            raise ValueError("Both buses must exist")
        if name in self.resistors:
            raise ValueError(f"Resistor {name} already exists")
        
        self.resistors.append(Resistor(name, bus1, bus2, r))

    def add_load_element(self, name: str, bus1: str, p: float, q: float):
        "Add a load"
        if bus1 not in self.buses:
            raise ValueError(f"Bus {bus1} does not exist")
        if name in self.loads:
            raise ValueError(f"Load {name} already exists")
        
        self.loads[name] = Load(name, bus1, p, q)

    def add_vsource_element(self, name: str, bus1: str, v: float):
        "Add a vsource"
        if bus1 not in self.buses:
            raise ValueError(f"Bus {bus1} does not exist")
        
        self.vsources = Vsource(name, bus1, v)
        # Set the bus voltage
        self.buses[bus1].set_bus_v(v)

    def calculate_currents(self):
        "Calculate all currents"
        currents = {}
        for i, resistor in enumerate(self.resistors):
            v1 = self.buses[resistor.bus1].get_bus_v()
            v2 = self.buses[resistor.bus2].get_bus_v()
            voltage_diff = v1 - v2
            current = voltage_diff * resistor.g
            currents[i] = current
        return currents

    def get_bus_voltages(self) -> Dict[str, float]:
        "Get all voltages"
        return {name: bus.v for name, bus in self.buses.items()}

    def display_circuit_state(self):
        "Display the current state"
        print("\nCircuit State:")
        print("*****************************")
        
        print("\nBuses:")
        for bus in self.buses.values():
            print(bus)
            
        print("\nVoltage Sources:")
        print(self.vsources)
            
        print("\nResistors:")
        for resistor in self.resistors:
            print(resistor)
            
        print("\nLoads:")
        for load in self.loads.values():
            print(load)
            
        print("\nCurrents:")
        currents = self.calculate_currents()
        for name, current in currents.items():
            print(f"Current through element {name + 1}: {current:.2f}A")


if __name__ == "__main__":
    # Test the Circuit class
    circuit = Circuit()
    
    # Add components
    circuit.add_bus("1")
    circuit.add_bus("2")
    
    circuit.add_vsource_element("V1", "1", 18)
    circuit.add_resistor_element("R1", "1", "2", 1000)
    circuit.add_load_element("L1", "2", 70, 0)
    
    # Display circuit state
    circuit.display_circuit_state()
    