class IndirizzoResidenza():

    def __init__(self, via, civico, citta, regione):
        self.via = via
        self.civico = civico
        self.citta = citta
        self.regione = regione

    def visualizzaResidenza(self):
        return 'Via ' + self.via + ' N° ' + str(self.civico) + ' ' + self.citta + ', in provincia di ' + self.regione