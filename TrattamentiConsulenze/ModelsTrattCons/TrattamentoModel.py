import os
import pickle
from TrattamentiConsulenze.ModelsTrattCons.ElencoTrattamentiModel import ElencoTrattamentiModel


class TrattamentoModel:

    def __init__(self):
        self.codiceTrattamento = -1
        self.nome = ""
        self.classe = ""
        self.costo = ""
        self.durata = ""

    def setInfoTrattamento(self, nome, classe, costo, durata):
        self.codiceTrattamento = (ElencoTrattamentiModel().calcolaUltimoCodiceTra()+1)
        self.nome = nome
        self.classe = classe
        self.costo = costo
        self.durata = durata

    def aggiungiTrattamento(self):
        trattamenti = {}
        try:
            if os.path.isfile('Dati/Trattamenti.pickle'):
                with open('Dati/Trattamenti.pickle', 'rb') as file:
                    trattamenti = pickle.load(file)
            trattamenti[self.codiceTrattamentoe] = self
            with open('Dati/Trattamenti.pickle', 'wb') as file:
                pickle.dump(trattamenti, file, pickle.HIGHEST_PROTOCOL)
        except:
            print("Impossibile aprire il file")

    def setInfoTrattamentoFile(self):
        try:
            with open('Dati/Consulenza.pickle', 'rb') as f:
                consulenza = pickle.load(f)

            self.giornoSettimana = consulenza.giornoSettimana
            self.costo = consulenza.costo
            self.durata = consulenza.durata
        except:
            print("Impossibile aprire il file")


    def modificaTrattamento(self):
        pass

    def eliminaTrattamento(self):
        pass

    def getInfoTrattamento(self):
        return {
            "giornoSettimana": self.giornoSettimana,
            "costo": self.costo,
            "durata": self.durata,
        }

