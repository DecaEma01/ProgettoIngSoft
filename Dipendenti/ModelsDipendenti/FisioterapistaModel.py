import pickle
import os

from Dipendenti.ModelsDipendenti.DipendenteModel import DipendenteModel

class FisioterapistaModel(DipendenteModel):

    def __init__(self, nome, cognome, codiceFiscale, telefono, via, civico, citta, provincia, listaCertificazioni):
        super().__init__(nome, cognome, codiceFiscale, telefono, via, civico, citta, provincia, ruoloDipendente='Fisioterapista')
        self.listaCertificazioni = listaCertificazioni
        for cert in self.listaCertificazioni:
            print(cert)
        super().salvaDipendenteFile()

    def modificaDipendente(self, nome, cognome, codicefiscale, telefono, via, civico, citta, provincia, listaCertificazioni):
        super().modificaDipendente(nome, cognome, codicefiscale, telefono, via, civico, citta, provincia)
        self.listaCertificazioni = listaCertificazioni
        super().salvaDipendenteFile()

    def visualizzaDipendente(self):
        fisioterapista = super().visualizzaDipendente()
        fisioterapista["listaCertificazioni"] = self.listaCertificazioni
        return fisioterapista

    def eliminaDipendente(self):
        if os.path.isfile('Dati/Dipendenti.pickle'):
            with open('Dati/Dipendenti.pickle', 'rb') as file:
                dipendenti = dict(pickle.load(file))
                del dipendenti[self.codiceDipendente]
                with open('Dati/Dipendenti.pickle', 'wb') as file:
                    pickle.dump(dipendenti, file, pickle.HIGHEST_PROTOCOL)
                del self
