import os
import pickle
import traceback


class ElencoPrenotazioniModel:

    def calcolaUltimoCodicePrenotazione(self):
        prenotazioni = {}
        codiceMax = 0
        try:
            if os.path.isfile('Dati/Prenotazioni.pickle') and os.path.getsize('Dati/Prenotazioni.pickle') > 0:
                with open('Dati/Prenotazioni.pickle', 'rb') as file:
                    prenotazioni = dict(pickle.load(file))
            if prenotazioni:
                for codice in prenotazioni.keys():
                    if prenotazioni[codice].codicePrenotazione > codiceMax:
                        codiceMax = prenotazioni[codice].codicePrenotazione
            return codiceMax
        except:
            print(traceback.format_exc())
            print("Impossibile aprire il file")

    def getPrenotazioniFile(self):
        prenotazioni = {}
        try:
            if os.path.isfile('Dati/Prenotazioni.pickle') and os.path.getsize('Dati/Prenotazioni.pickle') > 0:
                with open('Dati/Prenotazioni.pickle', 'rb') as file:
                    prenotazioni = dict(pickle.load(file))
            return prenotazioni
        except:
            print(traceback.format_exc())
            print("Impossibile aprire il file dei trattamenti")

    def ricercaPrenotazione(self, dictParametri):
        prenotazioniFile = self.getPrenotazioniFile()
        prenotazioniRisultato = {}

        try:
            for codicePrenotazione in prenotazioniFile.keys():
                trovato = True
                prenotazioneFile = prenotazioniFile[codicePrenotazione]
                #dictPrenotazioneFile = prenotazioneFile.getInfoPrenotazione()

                if dictParametri["tipologiaPrenotazione"]=="Seduta di trattamento fisioterapico":
                    if not prenotazioneFile.trattamento:
                        trovato = False
                if dictParametri["tipologiaPrenotazione"]=="Seduta di consulenza medica":
                    if prenotazioneFile.trattamento:
                        trovato = False
                if dictParametri["nomePaziente"]!= str(prenotazioneFile.paziente.nome) and dictParametri["nomePaziente"]!="" :
                    trovato = False
                if dictParametri["cognomePaziente"]!= str(prenotazioneFile.paziente.cognome) and dictParametri["cognomePaziente"]!="" :
                    trovato = False
                if dictParametri["codiceFiscalePaziente"]!= str(prenotazioneFile.paziente.codicefiscale) and dictParametri["codiceFiscalePaziente"]!="":
                    trovato = False
                if dictParametri["dataInizio"] > prenotazioneFile.data:
                    trovato = False
                if dictParametri["dataFine"] < prenotazioneFile.data:
                    trovato = False

                if trovato:
                    prenotazioniRisultato[codicePrenotazione] = prenotazioneFile

                """
                for chiaveParametro, valoreParametro in dictParametri.items():
                    if valoreParametro != '':
                        if valoreParametro != dictPrenotazioneFile[chiaveParametro]:  #le chiavi del dizionario che è la prenotazione devono coincidere con le chiavi dei dizionario dei parametri
                            trovato = False
                if trovato:
                    prenotazioniRisultato[codicePrenotazione] = prenotazioneFile
                """

            return prenotazioniRisultato

        except:
            print(traceback.format_exc())
            print("Impossibile eseguire la ricerca")

    #def ricercaPrenotazioneCodice(self, dictParametri):
    #    return ElencoPrenotazioniModel().ricercaPrenotazione(dictParametri)
    def ricercaPrenotazioneCodice(self, dictParametri):
        prenotazioniFile = self.getPrenotazioniFile()
        prenotazioniRisultato = {}

        try:
            for codicePrenotazione in prenotazioniFile.keys():
                trovato = True
                prenotazioneFile = prenotazioniFile[codicePrenotazione]
                dictPrenotazioneFile = prenotazioneFile.getInfoPrenotazione()
                for chiaveParametro, valoreParametro in dictParametri.items():
                    if valoreParametro != '':
                        if valoreParametro != dictPrenotazioneFile[
                            chiaveParametro]:  # le chiavi del dizionario che è la prenotazione devono coincidere con le chiavi dei dizionario dei parametri
                            trovato = False
                if trovato:
                    prenotazioniRisultato[codicePrenotazione] = prenotazioneFile

            return prenotazioniRisultato

        except:
            print(traceback.format_exc())
            print("Impossibile eseguire la ricerca")

    def eliminaPrenotazione(self,prenotazione):

        prenotazioniFile = self.getPrenotazioniFile()
        del prenotazioniFile[prenotazione.codicePrenotazione]

        try:
            if os.path.isfile('Dati/Prenotazioni.pickle') and os.path.getsize('Dati/Prenotazioni.pickle') > 0:
                with open('Dati/Prenotazioni.pickle', 'wb') as file:
                    pickle.dump(prenotazioniFile, file, pickle.HIGHEST_PROTOCOL)
            prenotazione.eliminaPrenotazione()
        except:
            print(traceback.format_exc())
            print("Impossibile aprire il file delle prenotazioni")

    def modificaPrenotazione(self, prenotazione, data, ora, completata, trattamento):

        prenotazioniFile = self.getPrenotazioniFile()
        prenotazioneModifica=prenotazioniFile[prenotazione.codicePrenotazione]
        prenotazioneModifica.modificaPrenotazione(data, ora, completata, trattamento)
        prenotazioniFile[prenotazioneModifica.codicePrenotazione]=prenotazioneModifica

        try:
            if os.path.isfile('Dati/Prenotazioni.pickle') and os.path.getsize('Dati/Prenotazioni.pickle') > 0:
                with open('Dati/Prenotazioni.pickle', 'wb') as file:
                    pickle.dump(prenotazioniFile, file, pickle.HIGHEST_PROTOCOL)
        except:
            print(traceback.format_exc())
            print("Impossibile aprire il file delle prenotazioni")

