from Prenotazioni.ModelsPrenotazioni.ElencoPrenotazioniModel import ElencoPrenotazioniModel

class ElencoPrenotazioniController:

    def getElencoPrenotazioni(self):
        return ElencoPrenotazioniModel().getTPrenotazioniFile()

    def ricercaPrenotazione(self,dictParametri):
        return ElencoPrenotazioniModel().ricercaPrenotazione(dictParametri)