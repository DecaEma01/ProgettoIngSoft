import os
import pickle
import traceback


class ElencoTrattamentiModel:

    def __init__(self):
        pass

    def calcolaUltimoCodiceTra(self):
        trattamenti = {}
        codiceMax = 0
        try:
            if os.path.isfile('Dati/Trattamenti.pickle') and os.path.getsize('Dati/Trattamenti.pickle') > 0:
                with open('Dati/Trattamenti.pickle', 'rb') as file:
                    trattamenti = dict(pickle.load(file))
            if trattamenti:
                for codice in trattamenti.keys():
                    if trattamenti[codice].codiceTrattamento > codiceMax:
                        codiceMax = trattamenti[codice].codiceTrattamento
            return codiceMax
        except:
            print(traceback.format_exc())
            print("Impossibile aprire il file")

    def getTrattamentiFile(self):
        trattamenti = {}
        try:
            if os.path.isfile('Dati/Trattamenti.pickle') and os.path.getsize('Dati/Trattamenti.pickle') > 0:
                with open('Dati/Trattamenti.pickle', 'rb') as file:
                    trattamenti = dict(pickle.load(file))
            return trattamenti
        except:
            print(traceback.format_exc())
            print("Impossibile aprire il file")

    def ricercaTrattamentoCodice(self, codiceTrattamento):
        pass
