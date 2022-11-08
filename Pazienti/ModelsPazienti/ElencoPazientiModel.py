import os, pickle

class ElencoPazientiModel():    
    def visualizzaElencoPazientiM(cls):
        if os.path.isfile('Dati/Pazienti.pickle'):
            with open('Dati/Pazienti.pickle', 'rb') as file:
                pazienti = dict(pickle.load(file))
        return pazienti
        
    def ricercaPazienteM(cls,**kwargs):
        pazienti = ElencoPazientiModel.visualizzaElencoPazientiM(ElencoPazientiModel)
        trovato = None
        pazientiTrovati = {}

        for chiavePaz in pazienti:
            trovato = True
            for chiave, valore in kwargs.items():
                paziente = pazienti[chiavePaz].visualizzaPazienteM(pazienti[chiavePaz])
                if valore != '' and valore != None:
                    if valore != paziente[chiave]:
                        trovato = False
                        break
            if trovato:
                pazientiTrovati[chiavePaz] = pazienti[chiavePaz]

        return pazientiTrovati
        
    def ricercaCodiceFiscaleM(cls,str):
        trovato = None
        try:
            elencoPaz = ElencoPazientiModel.visualizzaElencoPazientiM(ElencoPazientiModel)
            for chiave in elencoPaz:
                if elencoPaz[chiave].codicefiscale == str:
                    raise Exception()
        except:
            trovato = True
            pass
        
        return trovato
    
    def codicePazM(cls):
        pazienti = {}
        if os.path.isfile('Dati/Pazienti.pickle'):
            with open('Dati/Pazienti.pickle', 'rb') as file:
                pazienti = dict(pickle.load(file))
        codMax = 0
        if pazienti:
            for chiave in pazienti:
                if pazienti[chiave].codicePaziente > codMax:
                    codMax = pazienti[chiave].codicePaziente
        return codMax
        