from TrattamentiConsulenze.ModelsTrattCons.ConsulenzaModel import ConsulenzaModel

class ConsulenzaController:

    def modificaConsulenza(self, giornoSettimana, costo, durata):

        if giornoSettimana and costo and durata:
            if costo.isdigit() and durata.isdigit():    #controllo che i parametri costo e durata inseriti liberamente sulla vista contengano solo numeri
                consulenza = ConsulenzaModel()
                consulenza.setInfoConsulenza(giornoSettimana, costo, durata)
                consulenza.salvaConsulenza()
                return True
            else:
                return False #costo o durata non contengono solo numeri
        else:
            return False #ci sono valori nulli


    def getConsulenza(self):
        consulenza = ConsulenzaModel()
        consulenza.setInfoConsulenzaFile()
        return consulenza