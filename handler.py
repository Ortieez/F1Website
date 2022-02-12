import requests
import globals

"""
# ! Usage of handler
# * handler.showAccidents("zandvoort") "track is required, season is default all" || handler.showAccidents("zandvoort", 2021)
# * handler.showCircuit(2021) || handler.showCircuit() "default is all"

"""


class Handler():
    def __init__(self) -> None:
        pass 

    # Fetch Circuit Information
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
    
    # Fetch Accidents for a track Information
    def showAccidents(self, circuit, season = "all", ):
        if season != "all":
            self.currentURL = globals.startURL + str(season) + "/circuits/{}".format(circuit) + "/results.json" + globals.limit
        else:
            self.currentURL = globals.startURL + "circuits/{}".format(circuit) + "/results.json" + globals.limit
        self.data = requests.get(self.currentURL).json()
        self.output = []
        for race in self.data["MRData"]["RaceTable"]["Races"]:
            for accident in race["Results"]:
                if accident["status"] != "Finished":
                    if accident["status"].startswith("+"):
                        pass
                    else:
                        self.output.append("{},{}".format(race["Circuit"]["circuitId"], accident["status"]).split(","))
        return self.output