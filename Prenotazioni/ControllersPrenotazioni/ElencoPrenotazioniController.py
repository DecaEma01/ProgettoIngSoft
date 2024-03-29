from Prenotazioni.ModelsPrenotazioni.ElencoPrenotazioniModel import ElencoPrenotazioniModel

class ElencoPrenotazioniController:

    def getElencoPrenotazioni(self):
        return ElencoPrenotazioniModel().getPrenotazioniFile()

    def ricercaPrenotazione(self,dictParametri):
        return ElencoPrenotazioniModel().ricercaPrenotazione(dictParametri)

    def ricercaPrenotazioneCodice(self, dictParametri):
        return ElencoPrenotazioniModel().ricercaPrenotazioneCodice(dictParametri)