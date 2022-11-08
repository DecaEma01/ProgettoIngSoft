from Pazienti.ModelsPazienti.ElencoPazientiModel import ElencoPazientiModel

class ElencoPazientiController():
    def listaPazientiC(cls):
        return ElencoPazientiModel.visualizzaElencoPazientiM(ElencoPazientiModel)
    
    def ricercaPazienteC(cls, **keyargs):
        return ElencoPazientiModel.ricercaPazienteM(ElencoPazientiModel, **keyargs)
        
    def ricercaCodiceFiscaleC(cls,str):
        return ElencoPazientiModel.ricercaCodiceFiscaleM(ElencoPazientiModel, str)