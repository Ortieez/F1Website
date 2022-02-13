from unittest import result
import requests
import globals

"""
# ! Usage of handler
# * handler.showAccidents("zandvoort") "track is required, season is default all" || handler.showAccidents("zandvoort", 2021)
# * handler.showCircuits(2021) || handler.showCircuits() "default is all"

"""

class Handler():
    def __init__(self) -> None:
        pass 

    # Fetch Circuit Information
    def showCircuits(self, season = "all"):
        """
        if season != "all":
            self.currentURL = globals.startURL + str(season) + "/circuits.json" + globals.limit
        else:
            self.currentURL = globals.startURL + "circuits.json" + globals.limit
        self.data = requests.get(self.currentURL).json()
        self.output = []
        for circuit in self.data["MRData"]["CircuitTable"]["Circuits"]:
            self.output.append("{},{},{}".format(circuit["circuitId"], circuit["circuitName"], circuit["url"]).split(","))
        
        """
        self.output = [['americas', 'Circuit of the Americas', 'http://en.wikipedia.org/wiki/Circuit_of_the_Americas'], ['bahrain', 'Bahrain International Circuit', 'http://en.wikipedia.org/wiki/Bahrain_International_Circuit'], ['BAK', 'Baku City Circuit', 'http://en.wikipedia.org/wiki/Baku_City_Circuit'], ['catalunya', 'Circuit de Barcelona-Catalunya', 'http://en.wikipedia.org/wiki/Circuit_de_Barcelona-Catalunya'], ['hungaroring', 'Hungaroring', 'http://en.wikipedia.org/wiki/Hungaroring'], ['imola', 'Autodromo Enzo e Dino Ferrari', 'http://en.wikipedia.org/wiki/Autodromo_Enzo_e_Dino_Ferrari'], ['interlagos', 'Autódromo José Carlos Pace', 'http://en.wikipedia.org/wiki/Aut%C3%B3dromo_Jos%C3%A9_Carlos_Pace'], ['istanbul', 'Istanbul Park', 'http://en.wikipedia.org/wiki/Istanbul_Park'], ['jeddah', 'Jeddah Street Circuit', 'http://en.wikipedia.org/wiki/Jeddah_Street_Circuit'], ['losail', 'Losail International Circuit', 'http://en.wikipedia.org/wiki/Losail_International_Circuit'], ['monaco', 'Circuit de Monaco', 'http://en.wikipedia.org/wiki/Circuit_de_Monaco'], ['monza', 'Autodromo Nazionale di Monza', 'http://en.wikipedia.org/wiki/Autodromo_Nazionale_Monza'], ['portimao', 'Autódromo Internacional do Algarve', 'http://en.wikipedia.org/wiki/Algarve_International_Circuit'], ['red_bull_ring', 'Red Bull Ring', 'http://en.wikipedia.org/wiki/Red_Bull_Ring'], ['ricard', 'Circuit Paul Ricard', 'http://en.wikipedia.org/wiki/Paul_Ricard_Circuit'], ['rodriguez', 'Autódromo Hermanos Rodríguez', 'http://en.wikipedia.org/wiki/Aut%C3%B3dromo_Hermanos_Rodr%C3%ADguez'], ['silverstone', 'Silverstone Circuit', 'http://en.wikipedia.org/wiki/Silverstone_Circuit'], ['sochi', 'Sochi Autodrom', 'http://en.wikipedia.org/wiki/Sochi_Autodrom'], ['spa', 'Circuit de Spa-Francorchamps', 'http://en.wikipedia.org/wiki/Circuit_de_Spa-Francorchamps'], ['yas_marina', 'Yas Marina Circuit', 'http://en.wikipedia.org/wiki/Yas_Marina_Circuit'], ['zandvoort', 'Circuit Park Zandvoort', 'http://en.wikipedia.org/wiki/Circuit_Zandvoort']]
        return self.output
    
    # Fetch Accidents for a track Information
    def showAccidents(self, circuit, season = "all", ):
        """
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
        """
        self.output = [['yas_marina', 'Collision damage'], ['yas_marina', 'Gearbox'], ['yas_marina', 'Suspension'], ['yas_marina', 'Suspension'], ['yas_marina', 'Suspension']]
        return self.output

    def showDrivers(self, circuit, season ="all"):
        """
        if season != "all":
            self.currentURL = globals.startURL + str(season) + "/circuits/{}".format(circuit) + "/results.json" + globals.limit
        else:
            self.currentURL = globals.startURL + "circuits/{}".format(circuit) + "/results.json" + globals.limit
        self.data = requests.get(self.currentURL).json()
        self.output = []
        for race in self.data["MRData"]["RaceTable"]["Races"]:
            for results in race["Results"]:
                if results["status"] != "Finished":
                    if results["status"].startswith("+"):
                        pass
                    else:
                        self.output.append("{},{} {}".format(results["Driver"]["driverId"], results["Driver"]["givenName"], results["Driver"]["familyName"]))
        """
        self.output = ['perez,Sergio Pérez', 'latifi,Nicholas Latifi', 'giovinazzi,Antonio Giovinazzi', 'russell,George Russell', 'raikkonen,Kimi Räikkönen', 'mazepin,Nikita Mazepin']
        return self.output

    def showConstructors(self, circuit, season ="all"):
        """
        if season != "all":
            self.currentURL = globals.startURL + str(season) + "/circuits/{}".format(circuit) + "/results.json" + globals.limit
        else:
            self.currentURL = globals.startURL + "circuits/{}".format(circuit) + "/results.json" + globals.limit
        self.data = requests.get(self.currentURL).json()
        self.output = []
        for race in self.data["MRData"]["RaceTable"]["Races"]:
            for results in race["Results"]:
                if results["status"] != "Finished":
                    if results["status"].startswith("+"):
                        pass
                    else:
                        self.output.append("{},{}".format(results["Constructor"]["constructorId"], results["Constructor"]["name"]))
        """
        self.output = ['red_bull,Red Bull', 'williams,Williams', 'alfa,Alfa Romeo', 'williams,Williams', 'alfa,Alfa Romeo', 'haas,Haas F1 Team']
        return self.output