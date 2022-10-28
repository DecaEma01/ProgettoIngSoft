import os
import pickle


class ConsulenzaModel:

    def __init__(self):
        self.giornoSettimana = ""
        self.costo = ""
        self.durata = ""

    def setInfoConsulenza(self, giornoSettimana, costo, durata):
        self.giornoSettimana = giornoSettimana
        self.costo = costo
        self.durata = durata

    def setInfoConsulenzaFile(self):
        try:
            with open('Dati/Consulenza.pickle', 'rb') as f:
                consulenza=pickle.load(f)

            self.giornoSettimana = consulenza.giornoSettimana
            self.costo = consulenza.costo
            self.durata = consulenza.durata
        except:
            print ("Impossibile aprire il file")

    def salvaConsulenza(self):
        consulenza = self
        with open('Dati/Consulenza.pickle', 'wb') as f:
            pickle.dump(consulenza, f, pickle.HIGHEST_PROTOCOL)
"""
    def getInfoConsulenza(self):
        return {
            "giornoSettimana": self.giornoSettimana,
            "costo": self.costo,
            "durata": self.durata,
        }
"""





