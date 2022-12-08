import pickle
import os

from Dipendenti.ModelsDipendenti.DipendenteModel import DipendenteModel

class SegretarioModel(DipendenteModel):

    def __init__(self, nome, cognome, codiceFiscale, telefono, via, civico, citta, provincia):
        super().__init__(nome, cognome, codiceFiscale, telefono, via, civico, citta, provincia, ruoloDipendente = 'Segretario' )
        dipendenti = {}

        super().salvaDipendenteFile()

    def modificaDipendente(self, nome, cognome, codicefiscale, telefono, via, civico, citta, provincia):
        super().modificaDipendente(nome, cognome, codicefiscale, telefono, via, civico, citta, provincia)
        super().salvaDipendenteFile()

    def visualizzaDipendente(self):
        return super().visualizzaDipendente()

    def eliminaDipendente(self):
        if os.path.isfile('Dati/Dipendenti.pickle'):
            with open('Dati/Dipendenti.pickle', 'rb') as file:
                dipendenti = dict(pickle.load(file))
                del dipendenti[self.codiceDipendente]
                with open('Dati/Dipendenti.pickle', 'wb') as file:
                    pickle.dump(dipendenti, file, pickle.HIGHEST_PROTOCOL)
                del self