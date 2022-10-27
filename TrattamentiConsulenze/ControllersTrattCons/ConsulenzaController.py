from TrattamentiConsulenze.ModelsTrattCons.ConsulenzaModel import ConsulenzaModel

class ConsulenzaController:

    def modificaConsulenza(self, giornoSettimana, costo, durata):
        consulenza = ConsulenzaModel()
        consulenza.setInfoConsulenza(giornoSettimana, costo, durata)
        if consulenza.giornoSettimana and consulenza.costo and consulenza.durata:
            #da aggiungere controlli sull'ammissibilità dei valori
            consulenza.salvaConsulenza()

    def visualizzaConsulenza(self):
        consulenza = ConsulenzaModel()
        return consulenza.getInfoConsulenza()