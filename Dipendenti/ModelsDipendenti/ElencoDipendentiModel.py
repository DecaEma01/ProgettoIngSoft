import os
import pickle

class ElencoDipendentiModel():

    numDipendenti = 0

    def visualizzaElencoDipendenti(cls):
        if os.path.isfile('Dati/Dipendenti.pickle'):
            with open('Dati/Dipendenti.pickle', 'rb') as file:
                dipendenti = dict(pickle.load(file))
        return dipendenti

    def ricercaDipendente(cls,**kwargs):
        dipendenti = ElencoDipendentiModel.visualizzaElencoDipendenti(ElencoDipendentiModel)
        trovato = None
        dipendentiTrovati = {}

        for chiaveDip in dipendenti:
            trovato = True
            for chiave, valore in kwargs.items():
                dipendente = dipendenti[chiaveDip].visualizzaDipendente()
                if valore != '' and valore != None:
                    if valore != dipendente[chiave]:
                        trovato = False
                        break
            if trovato:
                dipendentiTrovati[chiaveDip] = dipendenti[chiaveDip]

        return dipendentiTrovati

    def calcolaUltimoCodiceDipendente(cls):

        dipendenti = {}
        if os.path.isfile('Dati/Dipendenti.pickle'):
            with open('Dati/Dipendenti.pickle', 'rb') as file:
                dipendenti = dict(pickle.load(file))

        codMax = 0

        if dipendenti:
            for chiave in dipendenti:
                if dipendenti[chiave].codiceDipendente > codMax:
                    codMax = dipendenti[chiave].codiceDipendente

        return codMax

