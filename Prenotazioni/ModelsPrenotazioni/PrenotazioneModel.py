import os
import pickle

from Prenotazioni.ModelsPrenotazioni.ElencoPrenotazioniModel import ElencoPrenotazioniModel


class PrenotazioneModel:

    def __init__(self):
        self.codicePrenotazione = -1
        self.trattamento = None
        self.paziente = None
        self.tipologia = ""
        self.data = ""
        self.ora = ""
        self.completata = False

    def setInfoPrenotazione(self, paziente, tipologia, data, ora, completata, trattamento=None):   #impostazione dei parametri per una nuova prenotazione
        self.codicePrenotazione = int(ElencoPrenotazioniModel().calcolaUltimoCodicePrenotazione())+1
        self.trattamento = trattamento
        self.paziente = paziente
        self.tipologia = tipologia
        self.data = data
        self.ora = ora
        self.completata = completata

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


    def modificaTrattamento(self, nome, classe, costo, durata): #nuova impostazione dei parametri per un trattamento già registrato
        self.nome = nome
        self.classe = classe
        self.costo = costo
        self.durata = durata

    def eliminaPrenotazione(self):
        self.codicePrenotazione = -1
        self.trattamento = None
        self.paziente = None
        self.tipologia = ""
        self.data = ""
        self.ora = ""
        self.completata = False
        del self

    def getInfoPrenotazione(self):
        return {
            "codicePrenotazione": self.codicePrenotazione,
            "trattamento": self.trattamento,
            "paziente": self.paziente,
            "tipologia": self.tipologia,
            "data": self.data,
            "ora": self.ora,
            "completata": self.completata,
        }