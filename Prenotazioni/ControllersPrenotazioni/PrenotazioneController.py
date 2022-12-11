from Prenotazioni.ModelsPrenotazioni.ElencoPrenotazioniModel import ElencoPrenotazioniModel
from Prenotazioni.ModelsPrenotazioni.PrenotazioneModel import PrenotazioneModel


class PrenotazioneController:

    def aggiungiPrenotazione(self, data, ora, paziente, trattamento):
        prenotazione = PrenotazioneModel()
        if not trattamento:
            self.tipologia = "Seduta di consulenza medica"
        else:
            self.tipologia = "Seduta di trattamento fisioterapico"
        prenotazione.setInfoPrenotazione(paziente, self.tipologia, data, ora, False, trattamento)
        prenotazione.aggiungiPrenotazione()



    def modificaPrenotazione(self, prenotazione, data, ora, completata, trattamento):
        if data and ora :
            ElencoPrenotazioniModel().modificaPrenotazione(prenotazione, data, ora, completata, trattamento)
            return True
        else:
            return False  # #data o ora non hanno valore

    def eliminaPrenotazione(self, prenotazione):
        ElencoPrenotazioniModel().eliminaPrenotazione(prenotazione)
