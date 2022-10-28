import os
import pickle


class ElencoTrattamentiModel:

    def __init__(self):
        pass

    def calcolaUltimoCodiceTra(cls):
        trattamenti = {}
        codiceMax = 0
        try:
            if os.path.isfile('Dati/Trattamenti.pickle'):
                with open('Dati/Trattamenti.pickle', 'rb') as file:
                    trattamenti = dict(pickle.load(file))
            if trattamenti:
                for codice in trattamenti.keys():
                    if trattamenti[codice].codiceTrattamento > codiceMax:
                        codiceMax = trattamenti[codice].codiceTrattamento

            return codiceMax
        except:
            print("Impossibile aprire il file")