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

    def setInfoPrenotazione(self, paziente, tipologia, data, ora, completata, trattamento):   #impostazione dei parametri per una nuova prenotazione
        self.codicePrenotazione = int(ElencoPrenotazioniModel().calcolaUltimoCodicePrenotazione())+1
        self.trattamento = trattamento
        self.paziente = paziente
        self.tipologia = tipologia
        self.data = data
        self.ora = ora
        self.completata = completata

    def aggiungiPrenotazione(self):
        prenotazioni = {}
        try:
            if os.path.isfile('Dati/Prenotazioni.pickle') and os.path.getsize('Dati/Prenotazioni.pickle') > 0:
                with open('Dati/Prenotazioni.pickle', 'rb') as file:
                    prenotazioni = pickle.load(file)
            prenotazioni[self.codicePrenotazione] = self
            with open('Dati/Prenotazioni.pickle', 'wb') as file:
                pickle.dump(prenotazioni, file, pickle.HIGHEST_PROTOCOL)
        except:
            print("Impossibile aprire il file")


    def modificaPrenotazione(self, data, ora, completata, trattamento): #nuova impostazione dei parametri per una prenotazione già registrata
        self.trattamento = trattamento
        self.data = data
        self.ora = ora
        self.completata = completata

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