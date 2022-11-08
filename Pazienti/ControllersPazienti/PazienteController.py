from Pazienti.ModelsPazienti.PazienteModel import PazienteModel


class PazienteController:

    def creaPazienteC(self, nome, cognome, codiceFiscale, telefono, via, civico, citta, provincia, prescrizioni):
        paz = PazienteModel(nome, cognome, codiceFiscale, telefono, via, civico, citta, provincia, prescrizioni)
        del paz

    def visualizzaPazienteC(paziente):
        return paziente.visualizzaPazienteM(paziente)

    def modificaPazienteC(self, paziente, nome, cognome, codicefiscale, telefono, via, civico, citta, provincia, prescrizioni):
        paz = paziente
        paz.modificaPazienteM(nome, cognome, codicefiscale, telefono, via, civico, citta, provincia, prescrizioni)

    def eliminaPazienteC(self, paziente):
        paz = paziente
        paz.eliminaPazienteM()
        