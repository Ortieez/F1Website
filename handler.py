import requests
import globals

"""
Backend for website that outputs data of damages 
Url examples

Season Circuit Status Drivers = All
https://ergast.com/api/f1/results.json

Season (2020), Circuit Status Drivers = All
https://ergast.com/api/f1/2020/results.json

Season (2020), Circuit (Monza), Status Drivers = All
https://ergast.com/api/f1/2020/circuits/monza/results.json

Season (1994), Circuit (Monza), Status (number of status, out of oil) , Drivers = All
https://ergast.com/api/f1/1994/circuits/monza/status/60/results.json

"""

# Fetch Circuit Information
class Handler():
    def __init__(self) -> None:
        pass 

    def showCircuit(self, season = "all"):
        if season != "all":
            self.currentURL = globals.startURL + str(season) + "/circuits.json" + globals.limit
        else:
            self.currentURL = globals.startURL + "circuits.json" + globals.limit
        self.data = requests.get(self.currentURL).json()
        self.output = []
        for circuit in self.data["MRData"]["CircuitTable"]["Circuits"]:
            self.output.append("{},{},{}".format(circuit["circuitId"], circuit["circuitName"], circuit["url"]).split(","))
        return self.output
    
    def showAccidents(self, season = "all"):
        if season != "all":
            self.currentURL = globals.startURL + str(season) + "/results.json" + globals.limit
        else:
            self.currentURL = globals.startURL + "results.json" + globals.limit
        self.data = requests.get(self.currentURL).json()
        self.output = []
        for race in self.data["MRData"]["RaceTable"]["Races"]:
            for accident in race["Results"]:
                self.output.append("{},{}".format(race["Circuit"]["circuitId"], accident["status"]).split(","))
        return self.output

def main():
    handler = Handler()
    print(*handler.showAccidents(2021), sep="\n")


main()