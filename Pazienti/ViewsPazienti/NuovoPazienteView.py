from PyQt5 import uic
from PyQt5.QtWidgets import *

from Pazienti.ControllersPazienti.PazienteController import PazienteController
from Pazienti.ControllersPazienti.ElencoPazientiController import ElencoPazientiController

class NuovoPazienteView(QWidget):
    def __init__(self):
        super(NuovoPazienteView,self).__init__()

        uic.loadUi("Pazienti/ViewsPazienti/UI/nuovoPaziente.ui",self)

        self.controllerPaziente = PazienteController()

        self.logout = self.findChild(QPushButton, "logoutButton")
        self.indietro = self.findChild(QPushButton, "indietroButton")
        self.aggiungi = self.findChild(QPushButton, "aggPrescrButton")
        self.salva = self.findChild(QPushButton, "salvaButton")

        self.nome = self.findChild(QLineEdit, "nomeEdit")
        self.cognome = self.findChild(QLineEdit, "cognomeEdit")
        self.codicefiscale = self.findChild(QLineEdit, "codiceEdit")
        self.telefono = self.findChild(QLineEdit, "cellulareEdit")
        self.via = self.findChild(QLineEdit, "viaEdit")
        self.numeroCivico = self.findChild(QLineEdit, "numCivEdit")
        self.citta = self.findChild(QLineEdit, "cittaEdit")
        self.provincia = self.findChild(QLineEdit, "regioneEdit")
        self.prescr = self.findChild(QLineEdit, 'prescrEdit')
        
        self.prescrizioni = {}
        
        self.prLayout = self.findChild(QFormLayout, "prescrizioniLayout")
        
        self.logout.clicked.connect(exit)
        self.indietro.clicked.connect(self.exIndietro)
        self.salva.clicked.connect(self.exSalva)
        self.aggiungi.clicked.connect(self.exAggiungi)        
        
        self.attributiPaziente = {'nome' : self.nome,'cognome':self.cognome,'codicefiscale':self.codicefiscale,'telefono':self.telefono,
            'via':self.via,'numeroCivico':self.numeroCivico,'citta':self.citta,'provincia':self.provincia, 'prescrizioni':self.prescrizioni}       
            
    def exAggiungi(self):
        if self.prescr.text() != '':
            self.prLayout.addRow(QLabel(f'{self.prLayout.rowCount()+1} - {self.prescr.text()}'))
            self.prescrizioni[self.prLayout.rowCount()] = self.prescr.text()
            self.prescr.setText('')

    def exSalva(self):
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

        self.creaPaziente()
        self.close()

    def creaPaziente(self):
        self.controllerPaziente.creaPazienteC(self.attributiPaziente['nome'].text(),
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