from Prenotazioni.ModelsPrenotazioni.ElencoPrenotazioniModel import ElencoPrenotazioniModel
from Prenotazioni.ModelsPrenotazioni.PrenotazioneModel import PrenotazioneModel


class PrenotazioneController:

    def aggiungiPrenotazione(self, data, ora, completata, paziente, trattamento):
        self.tipologia = ""
        if data and ora and paziente :
            prenotazione = PrenotazioneModel()
            if not trattamento:
                self.tipologia = "Seduta di consulenza medica"
            else:
                self.tipologia = "Seduta di trattamento fisioterapico"

            prenotazione.setInfoPrenotazione(self, paziente, self.tipologia, data, ora, completata, trattamento)
            prenotazione.aggiungiPrenotazione()
            return True
        else:
            return False #data o ora o paziente non hanno valore

    """
        else:
            return False  #ci sono valori nulli
    """


    def modificaPrenotazione(self, prenotazione, data, ora, completata, trattamento):
        if data and ora :
            ElencoPrenotazioniModel().modificaPrenotazione(prenotazione, data, ora, completata, trattamento)
            return True
        else:
            return False  # #data o ora non hanno valore
    """
        else:
            return False  # ci sono valori nulli
    """

    def eliminaPrenotazione(self, prenotazione):
        ElencoPrenotazioniModel().eliminaPrenotazione(prenotazione)
