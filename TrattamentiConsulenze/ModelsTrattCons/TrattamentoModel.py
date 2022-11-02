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

    def setInfoTrattamento(self, nome, classe, costo, durata):   #impostazione dei parametri per un nuovo trattamento
        self.codiceTrattamento = int(ElencoTrattamentiModel().calcolaUltimoCodiceTra())+1
        self.nome = nome
        self.classe = classe
        self.costo = costo
        self.durata = durata

    def aggiungiTrattamento(self):
        trattamenti = {}
        try:
            if os.path.isfile('Dati/Trattamenti.pickle') and os.path.getsize('Dati/Trattamenti.pickle') > 0:
                with open('Dati/Trattamenti.pickle', 'rb') as file:
                    trattamenti = pickle.load(file)
            trattamenti[self.codiceTrattamento] = self
            with open('Dati/Trattamenti.pickle', 'wb') as file:
                pickle.dump(trattamenti, file, pickle.HIGHEST_PROTOCOL)
        except:
            print("Impossibile aprire il file")

    def setInfoTrattamentoFile(self):    #impostazione dei parametri per un trattamento già salvato
        try:
            with open('Dati/Consulenza.pickle', 'rb') as f:
                consulenza = pickle.load(f)

            self.giornoSettimana = consulenza.giornoSettimana
            self.costo = consulenza.costo
            self.durata = consulenza.durata
        except:
            print("Impossibile aprire il file")


    def modificaTrattamento(self,codiceTrattamento, nome, classe, costo, durata): #nuova impostazione dei parametri per un trattamento già registrato
        self.codiceTrattamento = codiceTrattamento
        self.nome = nome
        self.classe = classe
        self.costo = costo
        self.durata = durata

    def eliminaTrattamento(self):
        self.codiceTrattamento = -1
        self.nome = ""
        self.classe = ""
        self.costo = ""
        self.durata = ""
        del self

    def getInfoTrattamento(self):
        return {
            "codiceTrattamento": self.codiceTrattamento,
            "nome":self.nome,
            "classe":self.classe,
            "costo" :self.costo,
            "durata":self.durata,
        }

