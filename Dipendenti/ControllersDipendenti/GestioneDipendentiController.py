from Dipendenti.ModelsDipendenti.DipendenteModel import ElencoDipendentiModel

from Dipendenti.ModelsDipendenti.MedicoModel import MedicoModel
from Dipendenti.ModelsDipendenti.SegretarioModel import SegretarioModel
from Dipendenti.ModelsDipendenti.FisioterapistaModel import FisioterapistaModel

class GestioneDipendentiController():

    def visualizzaElencoDipendenti(cls):
        return ElencoDipendentiModel.visualizzaElencoDipendenti(ElencoDipendentiModel)

    def ricercaDipendente(cls, **keyargs):
        return ElencoDipendentiModel.ricercaDipendente(ElencoDipendentiModel, **keyargs)

    def creaDipendente(cls, ruolo, *args):
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



