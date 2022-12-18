from Pazienti.ModelsPazienti.ElencoPazientiModel import ElencoPazientiModel

import pickle, os

class PazienteModel:
    
    # __init__ ha anche la funzione di creazione del paziente
    def __init__(self, nome, cognome, codicefiscale, telefono, via, civico, citta, provincia, prescrizioni):
        
        pazienti = {}
        codicePaziente = ElencoPazientiModel.calcolaUltimoCodicePazienteM(ElencoPazientiModel)
        
        self.codicePaziente = codicePaziente + 1
        self.nome = nome
        self.cognome = cognome
        self.codicefiscale = codicefiscale
        self.telefono = telefono
        self.via = via
        self.civico = civico
        self.citta = citta
        self.provincia = provincia
        self.prescrizioni = prescrizioni

        if os.path.isfile('Dati/Pazienti.pickle'):
            with open('Dati/Pazienti.pickle', 'rb') as file:
                    pazienti = pickle.load(file)
        pazienti[self.codicePaziente] = self
        with open('Dati/Pazienti.pickle', 'wb') as file:
            pickle.dump(pazienti, file, pickle.HIGHEST_PROTOCOL)

    def modificaPazienteM(self, nome, cognome, codicefiscale, telefono, via, civico, citta, provincia, prescrizioni):
        self.nome = nome
        self.cognome = cognome
        self.codicefiscale = codicefiscale
        self.telefono = telefono
        self.via = via
        self.civico = civico
        self.citta = citta
        self.provincia = provincia
        self.prescrizioni = prescrizioni
        
        if os.path.isfile('Dati/Pazienti.pickle'):
            with open('Dati/Pazienti.pickle','rb') as file:
                pazienti = pickle.load(file)
        pazienti[self.codicePaziente] = self
        with open('Dati/Pazienti.pickle', 'wb') as file:
            pickle.dump(pazienti, file, pickle.HIGHEST_PROTOCOL)

    def visualizzaPazienteM(self, paziente):
        return {
            'codicePaziente': self.codicePaziente,
            'nome': self.nome,
            'cognome': self.cognome,
            'codicefiscale': self.codicefiscale,
            'telefono': self.telefono,
            'indirizzoResidenza': self.getIndirizzoResidenza(),
            'prescrizioni': self.prescrizioni
        }

    def eliminaPazienteM(self):
        if os.path.isfile('Dati/Pazienti.pickle'):
            with open('Dati/Pazienti.pickle', 'rb') as file:
                pazienti = dict(pickle.load(file))
                del pazienti[self.codicePaziente]
                with open('Dati/Pazienti.pickle', 'wb') as file:
                    pickle.dump(pazienti, file, pickle.HIGHEST_PROTOCOL)
                del self

    def getIndirizzoResidenza(self):
        return 'Via ' + self.via + ' N° ' + str(self.civico) + ' ' + self.citta + ', in provincia di ' + self.provincia