from Prenotazioni.ModelsPrenotazioni.ElencoPrenotazioniModel import ElencoPrenotazioniModel

class ElencoPrenotazioniController:

    def getElencoTrattamenti(self):
        return ElencoPrenotazioniModel().getTPrenotazioniFile()

    def ricercaTrattamento(self,dictParametri):
        return ElencoPrenotazioniModel().ricercaPrenotazione(dictParametri)