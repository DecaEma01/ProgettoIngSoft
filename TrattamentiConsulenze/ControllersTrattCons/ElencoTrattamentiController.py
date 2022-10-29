from TrattamentiConsulenze.ModelsTrattCons.ElencoTrattamentiModel import ElencoTrattamentiModel


class ElencoTrattamentiController:

    def getElencoTrattamenti(self):
        return ElencoTrattamentiModel().getTrattamentiFile()

    def ricercaTrattamento(self):
        pass
