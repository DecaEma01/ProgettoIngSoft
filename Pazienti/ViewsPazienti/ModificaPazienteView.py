from PyQt5.QtWidgets import *
from PyQt5 import uic

from Pazienti.ControllersPazienti.ElencoPazientiController import ElencoPazientiController

from Pazienti.ControllersPazienti.PazienteController import PazienteController

class ModificaPazienteView(QWidget):

    def __init__(self, paziente, callback):
        super(ModificaPazienteView, self).__init__()

        self.pazienteController = PazienteController()
        
        uic.loadUi("Pazienti/ViewsPazienti/UI/modificaPaziente.ui",self)
        
        self.aggiornaListaPaz = callback
        self.paziente = paziente
        self.attributiPaziente = {}
        
        self.logout = self.findChild(QPushButton, "logoutButton")
        self.indietro = self.findChild(QPushButton, "indietroButton")
        self.aggiungi = self.findChild(QPushButton, "aggPrescrButton")
        self.salva = self.findChild(QPushButton, "salvaButton")
        self.rimuovi = self.findChild(QPushButton, "rimPrescrButton")
        
        self.nome = self.findChild(QLineEdit, "nomeEdit")
        self.nome.setText(paziente.nome)
        self.cognome = self.findChild(QLineEdit, "cognomeEdit")
        self.cognome.setText(paziente.cognome)
        self.codicefiscale = self.findChild(QLineEdit, "codiceEdit")
        self.codicefiscale.setText(paziente.codicefiscale)
        self.telefono = self.findChild(QLineEdit, "cellulareEdit")
        self.telefono.setText(paziente.telefono)
        self.via = self.findChild(QLineEdit, "viaEdit")
        self.via.setText(paziente.indirizzoResidenza.via)
        self.numeroCivico = self.findChild(QLineEdit, "numCivEdit")
        self.numeroCivico.setText(paziente.indirizzoResidenza.civico)
        self.citta = self.findChild(QLineEdit, "cittaEdit")
        self.citta.setText(paziente.indirizzoResidenza.citta)
        self.provincia = self.findChild(QLineEdit, "regioneEdit")
        self.provincia.setText(paziente.indirizzoResidenza.regione)
        self.prescr = self.findChild(QLineEdit, 'prescrEdit')
        self.prescrizioni = self.paziente.prescrizioni
        
        self.prLayout = self.findChild(QFormLayout, "prescrizioniLayout")
        
        self.aggiornaPrescrizioni()
        
        self.attributiPaziente = {'nome' : self.nome,'cognome':self.cognome,'codicefiscale':self.codicefiscale,'telefono':self.telefono,
            'via':self.via,'numeroCivico':self.numeroCivico,'citta':self.citta,'provincia':self.provincia, 'prescrizioni':self.prescrizioni}
            
        self.logout.clicked.connect(exit)

        self.indietro.clicked.connect(self.exIndietro)
        self.salva.clicked.connect(self.nuoviDatiPaziente)
        self.aggiungi.clicked.connect(self.exAggiungi)
        self.rimuovi.clicked.connect(self.exTogli)

    def aggiornaPrescrizioni(self):
        try:
            for key in self.prescrizioni:
                self.prLayout.addRow(QLabel(f'{key} - {self.prescrizioni[key]}'))
        except:
            pass

    def cancellaLista(self):
        if self.prLayout.rowCount != 0:
            while self.prLayout.rowCount() > 0:
                self.prLayout.removeRow(self.prLayout.rowCount()-1)
    
    def exTogli(self):
        presente = False
        try:
            if self.prLayout.rowCount != 0:
                
                ultimaPrescrizione = list(self.prescrizioni)[-1]
            
                for key in self.prescrizioni:
                    if self.prescrizioni[key] == self.prescr.text():
                        self.prescrizioni[key] = self.prescrizioni[ultimaPrescrizione]
                        presente = True
                if presente == False:
                    raise Exception()
                    
                self.cancellaLista()
                del self.prescrizioni[list(self.prescrizioni)[-1]]
                self.aggiornaPrescrizioni()
                self.prescr.setText('')       
        except:
            QMessageBox.critical(self, 'Errore', 'Inserire il NOME di una prescrizione presente', QMessageBox.Ok)
            return
        
    def exAggiungi(self):
        if self.prescr.text() != '':
            self.prLayout.addRow(QLabel(f'{self.prLayout.rowCount()+1} - {self.prescr.text()}'))
            self.prescrizioni[self.prLayout.rowCount()] = self.prescr.text()
            self.prescr.setText('')

    def nuoviDatiPaziente(self):
        try:
            for chiave in self.attributiPaziente:
                if chiave != 'prescrizioni':
                    if self.attributiPaziente[chiave].text() == '':
                        raise Exception()
        except:
            QMessageBox.critical(self, 'Errore', 'Tutti i campi sono obbligatori! ', QMessageBox.Ok)
            return
        
        try:
            for chiave in self.attributiPaziente:
                if chiave == 'nome' or chiave == 'cognome' or chiave == 'via' or chiave == 'citta' or chiave == 'provincia':
                    if self.attributiPaziente[chiave].text().isalpha() == False:
                        raise Exception(chiave)
        except:
            QMessageBox.critical(self, 'Errore', f"L'elemento {chiave} contiene dei numeri", QMessageBox.Ok)
            return
        
        try:
            for chiave in self.attributiPaziente:
                if chiave == 'telefono' or chiave == 'numeroCivico':
                    if self.attributiPaziente[chiave].text().isnumeric() == False:
                        raise Exception(chiave)
        except:
            QMessageBox.critical(self, 'Errore', f"L'elemento {chiave} contiene delle lettere", QMessageBox.Ok)
            return
        
        if ElencoPazientiController.ricercaCodiceFiscaleC(ElencoPazientiController, self.attributiPaziente['codicefiscale']) == True:
            QMessageBox.critical(self, 'Errore', 'Codice fiscale già presente in un altro paziente. Elimina il paziente vecchio per inserirne uno nuovo', QMessageBox.Ok)
            return
        
        self.exSalva()
        self.aggiornaListaPaz()
        self.close()

    def exSalva(self):
        self.pazienteController.modificaPazienteC(self.paziente,
                                                 self.attributiPaziente['nome'].text(),
                                                 self.attributiPaziente['cognome'].text(),
                                                 self.attributiPaziente['codicefiscale'].text(),
                                                 self.attributiPaziente['telefono'].text(),
                                                 self.attributiPaziente['via'].text(),
                                                 self.attributiPaziente['numeroCivico'].text(),
                                                 self.attributiPaziente['citta'].text(),
                                                 self.attributiPaziente['provincia'].text(),
                                                 self.attributiPaziente['prescrizioni'])

    def exIndietro(self):
        self.close()