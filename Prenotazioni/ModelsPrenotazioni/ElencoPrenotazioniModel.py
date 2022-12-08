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
                dictPrenotazioneFile = prenotazioneFile.getInfoPrenotazione()
                for chiaveParametro, valoreParametro in dictParametri.items():
                    if valoreParametro != '':
                        if valoreParametro != dictPrenotazioneFile[chiaveParametro]:  #le chiavi del dizionario che è la prenotazione devono coincidere con le chiavi dei dizionario dei parametri
                            trovato = False
                if trovato:
                    prenotazioniRisultato[codicePrenotazione] = prenotazioneFile

            return prenotazioniRisultato

        except:
            print(traceback.format_exc())
            print("Impossibile eseguire la ricerca")

    def eliminaTrattamento(self,trattamento):

        trattamentiFile = self.getTrattamentiFile()
        del trattamentiFile[trattamento.codiceTrattamento]

        try:
            if os.path.isfile('Dati/Trattamenti.pickle') and os.path.getsize('Dati/Trattamenti.pickle') > 0:
                with open('Dati/Trattamenti.pickle', 'wb') as file:
                    pickle.dump(trattamentiFile, file, pickle.HIGHEST_PROTOCOL)
            trattamento.eliminaTrattamento()
        except:
            print(traceback.format_exc())
            print("Impossibile aprire il file dei trattamenti")

    def modificaTrattamento(self, trattamento, nome, classe, costo, durata):

        trattamentiFile = self.getTrattamentiFile()
        trattamentoModifica=trattamentiFile[trattamento.codiceTrattamento]
        trattamentoModifica.modificaTrattamento(nome, classe, costo, durata)
        trattamentiFile[trattamentoModifica.codiceTrattamento]=trattamentoModifica

        try:
            if os.path.isfile('Dati/Trattamenti.pickle') and os.path.getsize('Dati/Trattamenti.pickle') > 0:
                with open('Dati/Trattamenti.pickle', 'wb') as file:
                    pickle.dump(trattamentiFile, file, pickle.HIGHEST_PROTOCOL)
        except:
            print(traceback.format_exc())
            print("Impossibile aprire il file dei trattamenti")

