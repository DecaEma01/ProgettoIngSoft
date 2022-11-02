from TrattamentiConsulenze.ModelsTrattCons.ElencoTrattamentiModel import ElencoTrattamentiModel
from TrattamentiConsulenze.ModelsTrattCons.TrattamentoModel import TrattamentoModel


class TrattamentoController:

    def aggiungiTrattamento(self,nome,classe,costo,durata):
        if nome and classe and costo and durata:
            if costo.isdigit() and durata.isdigit():  # controllo che i parametri costo e durata inseriti liberamente sulla vista contengano solo numeri
                trattamento = TrattamentoModel()
                trattamento.setInfoTrattamento(nome,classe,costo,durata)
                trattamento.aggiungiTrattamento()
                return True
            else:
                return False #costo o durata non contengono solo numeri
        else:
            return False  #ci sono valori nulli


    def modificaTrattamento(self, trattamento, nome, classe, costo, durata):
        if nome and classe and costo and durata:
            if costo.isdigit() and durata.isdigit():  # controllo che i parametri costo e durata inseriti liberamente sulla vista contengano solo numeri
                ElencoTrattamentiModel().modificaTrattamento(trattamento, nome,classe,costo,durata)
                return True
            else:
                return False  # costo o durata non contengono solo numeri
        else:
            return False  # ci sono valori nulli

    def eliminaTrattamento(self, trattamento):
        ElencoTrattamentiModel().eliminaTrattamento(trattamento)

    def visualizzaTrattamento(self):
        pass

