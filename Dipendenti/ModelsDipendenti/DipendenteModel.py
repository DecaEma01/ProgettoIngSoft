from Dipendenti.ModelsDipendenti.ElencoDipendentiModel import ListaDipendentiModel

import os
import pickle

class DipendenteModel:

    def __init__(self, nome, cognome, codicefiscale, telefono, via, civico, citta, provincia, ruoloDipendente):

        codiceDipendente = ListaDipendentiModel.codiceDip(ListaDipendentiModel)

        self.codiceDipendente = codiceDipendente + 1
        self.nome = nome
        self.cognome = cognome
        self.codicefiscale = codicefiscale
        self.telefono = telefono
        self.via = via
        self.civico = civico
        self.citta = citta
        self.provincia = provincia
        self.ruoloDipendente = ruoloDipendente

    def modificaDipendente(self, nome, cognome, codicefiscale, telefono, via, civico, citta, provincia):
        self.nome = nome
        self.cognome = cognome
        self.codicefiscale = codicefiscale
        self.telefono = telefono
        self.via = via
        self.civico = civico
        self.citta = citta
        self.provincia = provincia

    def visualizzaDipendente(self):#ritorna dizionario
        return {
            'codiceDipendente': self.codiceDipendente,
            'nome': self.nome,
            'cognome': self.cognome,
            'codicefiscale': self.codicefiscale,
            'telefono': self.telefono,
            'indirizzoResidenza': self.getIndirizzoResidenza(),
            'ruoloDipendente': self.ruoloDipendente
        }

    def eliminaDipendente(self):
        pass

    def salvaDipendenteFile(self):

        dipendenti = {}
        if os.path.isfile('Dati/Dipendenti.pickle'):
            with open('Dati/Dipendenti.pickle', 'rb') as file:
                dipendenti = pickle.load(file)
        dipendenti[self.codiceDipendente] = self
        with open('Dati/Dipendenti.pickle', 'wb') as file:
            pickle.dump(dipendenti, file, pickle.HIGHEST_PROTOCOL)

        return

    def getIndirizzoResidenza(self):
        return 'Via ' + self.via + ' N° ' + str(self.civico) + ' ' + self.citta + ', in provincia di ' + self.provincia