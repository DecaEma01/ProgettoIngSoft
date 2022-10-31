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
            print("Impossibile aprire il file dei trattamenti")

    def ricercaTrattamento(self, dictParametri):
        trattamentiFile = self.getTrattamentiFile()
        trattamentiRisultato = {}

        try:
            for codiceTrattamento in trattamentiFile.keys():
                trovato = True
                trattamentoFile = trattamentiFile[codiceTrattamento]
                dictTrattamentoFile = trattamentoFile.getInfoTrattamento()
                for chiaveParametro, valoreParametro in dictParametri.items():
                    if valoreParametro != '':
                        if valoreParametro != dictTrattamentoFile[chiaveParametro]:  #le chiavi del dizionario che è il trattamento devono coincidere con le chiavi dei dizionario dei parametri
                            trovato = False
                if trovato:
                    trattamentiRisultato[codiceTrattamento] = trattamentoFile

            return trattamentiRisultato

        except:
            print(traceback.format_exc())
            print("Impossibile eseguire la ricerca")


