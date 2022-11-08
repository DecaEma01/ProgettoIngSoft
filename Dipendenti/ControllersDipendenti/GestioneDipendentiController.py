from Amministratore.Dipendenti.ModelsDipendenti.DipendenteModel import ListaDipendentiModel

from Amministratore.Dipendenti.ModelsDipendenti.MedicoModel import MedicoModel
from Amministratore.Dipendenti.ModelsDipendenti.SegretarioModel import SegretarioModel
from Amministratore.Dipendenti.ModelsDipendenti.FisioterapistaModel import FisioterapistaModel

class GestioneDipendentiController():

    def listaDipendenti(cls):
        return ListaDipendentiModel.visualizzaElencoDipendente(ListaDipendentiModel)

    def ricercaDipendente(cls, **keyargs):
        return ListaDipendentiModel.ricercaDipendente(ListaDipendentiModel, **keyargs)

    def creaDipendete(cls, ruolo, *args):
        if ruolo == "Fisioterapista":
            dipendente = FisioterapistaModel(*args)

        elif ruolo == "Segretario":
            dipendente = SegretarioModel(*args)

        elif ruolo == "Medico":
            dipendente = MedicoModel(*args)

        del dipendente

        return

    def visualizzaDipendente(self, dipendente):
        return dipendente.visualizzaDipendente()

    def modificaDipendente(self, dipendente, *args):
        dipendente.modificaDipendente(*args)
        return

    def eliminaDipendente(self, dipendente):
        return dipendente.eliminaDipendente()



