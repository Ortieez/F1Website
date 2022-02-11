import requests
import globals

"""
- Default limit to results = 30

What to fetch - what information can you filter with:
- Circuits - Season
Driver information - Season
Race Results - Season, Round, Driver, Circuit
Race schedule - Season 

Lap Times - Season, Round, Driver, Lap
Pit stops - Season, Round, Driver, Stop

"""

class Circuit():
    def __init__(self, season = "all"):
        if season == "all":
            self.currentURL = globals.baseURL + "circuits" + globals.endURL
        else:
            self.currentURL = globals.baseURL + f"{season}/circuits" + globals.endURL
    
    def show(self):
        self.data = requests.get(self.currentURL).json()
        self.output = []
        for circuit in self.data["MRData"]["CircuitTable"]["Circuits"]:
            self.output.append("ID: {}, Name: {}, Country: {}, URL: {}".format(circuit["circuitId"], circuit["circuitName"], circuit["Location"]["country"], circuit["url"]))
        return self.output

class Driver():
    def __init__(self, season = "all"):
        if season == "all":
            self.currentURL = globals.baseURL + "drivers" + globals.endURL
        else:
            self.currentURL = globals.baseURL + f"{season}/drivers" + globals.endURL

    def show(self):
        self.data = requests.get(self.currentURL).json()
        self.output = []
        for driver in self.data["MRData"]["DriverTable"]["Drivers"]:
            self.output.append("ID: {}, Name: {} {}, URL: {}".format(driver["driverId"], driver["givenName"], driver["familyName"], driver["nationality"]))
        return self.output

# season, round, driver, circuit
def main():
    circuit = Circuit()
    driver = Driver() 
    print(circuit.show())
    print(driver.show())

main()