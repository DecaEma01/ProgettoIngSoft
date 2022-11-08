from PyQt5 import uic
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox

from Pazienti.ControllersPazienti.ElencoPazientiController import ElencoPazientiController
from Pazienti.ViewsPazienti.VisualizzaPazienteView import VisualizzaPazienteView

class PazientiRegistratiView(QWidget):
    def __init__(self, logout,parent=None):
        super(PazientiRegistratiView,self).__init__(parent)
        
        uic.loadUi("Pazienti/ViewsPazienti/UI/registroPazienti.ui",self)

        
        self.logout = self.findChild(QPushButton, "logoutButton")
        self.indietro = self.findChild(QPushButton, "indietroButton")
        self.ricerca = self.findChild(QPushButton, "ricercaButton")
        self.visualizza = self.findChild(QPushButton, "visualizzaButton")

        self.codice = self.findChild(QLineEdit, "codEdit")
        self.nome = self.findChild(QLineEdit, "nomeEdit")
        self.cognome = self.findChild(QLineEdit, "cognomeEdit")
        self.listViewPazienti = self.findChild(QListView, "listView")

        self.logout.clicked.connect(exit)
        self.indietro.clicked.connect(self.close)
        
        self.visualizza.clicked.connect(self.visualizzaPaziente)
        
        self.ricerca.clicked.connect(self.ricercaPaziente)
        
        self.parametriRicerca = {'codicefiscale':self.codice,'nome':self.nome,'cognome':self.cognome}
        self.aggiornaPazienti()
    
    def caricaPazienti(self):
        pazienti = ElencoPazientiController.listaPazientiC(ElencoPazientiController)
        self.pazienti.extend(pazienti.values())
        
    def aggiornaPazienti(self):
        self.pazienti = []
        self.caricaPazienti()
        listviewModel = QStandardItemModel(self.listViewPazienti)
        for paziente in self.pazienti:
            item = QStandardItem()
            nome = f'{paziente.codicePaziente} - {paziente.nome} {paziente.cognome}'
            item.setText(nome)
            item.setEditable(False)

            listviewModel.appendRow(item)   #viene inserito nella lista inserisce riga(row)
        self.listViewPazienti.setModel(listviewModel)
        
    def ricercaPaziente(self):
        parametri = {}

        for chiave in self.parametriRicerca:
            if self.parametriRicerca[chiave].text() != '':
                parametri[chiave] = self.parametriRicerca[chiave].text()

        pTrovati = ElencoPazientiController.ricercaPazienteC(ElencoPazientiController, **parametri)
        lTrovati = []
        lTrovati.extend(pTrovati.values())
        listviewModel = QStandardItemModel(self.listViewPazienti)

        for paziente in lTrovati:
            item = QStandardItem()
            nome = f'{paziente.codicePaziente} - {paziente.nome} {paziente.cognome}'
            item.setText(nome)
            item.setEditable(False)

            listviewModel.appendRow(item)   #viene inserito nella lista inserisce riga(row)
        self.listViewPazienti.setModel(listviewModel)
        
    def visualizzaPaziente(self):
        try:
            selected = self.listViewPazienti.selectedIndexes()[0].data()
            codice = int(selected[0])

            paziente = ElencoPazientiController.ricercaPazienteC(ElencoPazientiController, codicePaziente = codice)[codice]

            self.vistaPaziente = VisualizzaPazienteView(paziente, callback = self.aggiornaPazienti)
            self.vistaPaziente.show()

        except IndexError:
            QMessageBox.critical(self, 'Errore', 'Selezionare un paziente specifico! ', QMessageBox.Ok)
            return