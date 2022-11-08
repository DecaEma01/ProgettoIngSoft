from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton, QLabel, QLineEdit, QComboBox, QMessageBox

from Amministratore.Dipendenti.ControllersDipendenti.GestioneDipendentiController import GestioneDipendentiController
from Amministratore.Dipendenti.ViewDipendenti.VisualizzaDipendenteView import VisualizzaDipendenteView

class DipendentiRegistratiView(QWidget):

    def __init__(self, bLogout, parent=None):
        super(DipendentiRegistratiView, self).__init__(parent)

        self.bLogout = bLogout
        layoutVertMain = QVBoxLayout()                          # layout MAIN quello principale utilizzato dalla  vista
        self.listViewDipendenti = QListView()
        self.parametriRicerca = {}                              # è un dizionario contenente tutti i parametri aggiornati in tempo reale(per comodità tutti i parametri sono QLineEdit)
        self.aggiornaDipendenti()

        self.resize(900, 700)

        # QBUTTON (gestione account)
        layoutBottoniSwitch = QHBoxLayout()
        layoutBottoniSwitch.addWidget(self.generaBottone('Indietro', self.chiudiFinestra))
        layoutBottoniSwitch.addWidget(self.generaBottone('Logout', self.logout))
        layoutVertMain.addLayout(layoutBottoniSwitch)       # Main

        # COMBOBOX
        layoutVertMain.addWidget(self.generaComboBox(self.selezionaProffessione, 'nessuna scelta', 'Medico', 'Fisioterapista', 'Segretario'))

        # QLABLE + QLINE + 1 QBUTTON (ricerca)
        layoutVertMain.addLayout(self.generaLinea('nome', 'Nome'))
        layoutVertMain.addLayout(self.generaLinea('cognome', 'Cognome'))
        layoutVertMain.addLayout(self.generaLinea('codicefiscale', 'Codice Fiscale'))
        layoutVertMain.addWidget(self.generaBottone('Ricerca', self.ricercaDipendente))     # Main

        # QLISTVIEW
        layoutVertMain.addWidget(self.listViewDipendenti)       # Main

        # QBUTTON (aggiorna e visualizza)
        layoutBottoni = QHBoxLayout()   # verticale per i bottoni
        layoutBottoni.addWidget(self.generaBottone('Aggiorna', self.aggiornaDipendenti))
        layoutBottoni.addStretch()
        layoutBottoni.addWidget(self.generaBottone('Visualizza', self.visualizzaDipendente))
        layoutVertMain.addLayout(layoutBottoni)     # Main

        # set Main Widget
        self.setLayout(layoutVertMain)
        self.setWindowTitle('Amministratore - Dipendenti Registrati')

    def caricaDipendenti(self):
                dipendenti = GestioneDipendentiController.listaDipendenti(GestioneDipendentiController)#dict(pickle.load(file))
                self.dipendenti.extend(dipendenti.values())

    def aggiornaDipendenti(self):
        self.dipendenti = []
        self.caricaDipendenti()
        listViewModel = QStandardItemModel()# questa è una lista composta da QStandardItems(unica cella della lista definita con item model(definisce una riga))
        for dipendente in self.dipendenti:
            item = QStandardItem()
            nome = f'{dipendente.nome} {dipendente.cognome} - {type(dipendente).__name__} {dipendente.codiceDipendente}'
            item.setText(nome)
            item.setEditable(False)

            listViewModel.appendRow(item)   #viene inserito nella lista inserisce riga(row)
        self.listViewDipendenti.setModel(listViewModel)

    def selezionaProffessione(self, testo):
        print('selezionato nella tendina: ', testo)
        if testo != 'nessuna scelta':
            l = QLineEdit()
            l.setText(testo)
            self.parametriRicerca['ruoloDipendente'] = l
        else:
            del self.parametriRicerca['ruoloDipendente']
        pass

    def ricercaDipendente(self):#DEVE MODIFICARE LA self.listViewDipendenti essenziale
        parametri = {}

        for chiave in self.parametriRicerca:
            if self.parametriRicerca[chiave].text() != '':
                parametri[chiave] = self.parametriRicerca[chiave].text()
                print(parametri[chiave])

        print('LISTA DEI PARAMETRI:::::::::::::::')
        for chiave in parametri:
            print(parametri[chiave])

        dTrovati = GestioneDipendentiController.ricercaDipendente(GestioneDipendentiController, **parametri)
        lTrovati = []
        lTrovati.extend(dTrovati.values())
        listviewModel = QStandardItemModel()

        for dipendente in lTrovati:
            item = QStandardItem()
            nome = f'{dipendente.nome} {dipendente.cognome} - {type(dipendente).__name__} {dipendente.codiceDipendente}'
            item.setText(nome)
            item.setEditable(False)

            listviewModel.appendRow(item)   #viene inserito nella lista inserisce riga(row)
        self.listViewDipendenti.setModel(listviewModel)

    def visualizzaDipendente(self):
        try:
            selected = self.listViewDipendenti.selectedIndexes()[0].data()
            codice = int(selected.split("-")[1].strip().split(" ")[1])

            dipendente = GestioneDipendentiController.ricercaDipendente(GestioneDipendentiController, codiceDipendente = codice)[codice]

            self.vistaDipendente = VisualizzaDipendenteView(dipendente, callback = self.aggiornaDipendenti)
            self.vistaDipendente.show()

        except IndexError:
            print("IndexError")
            QMessageBox.critical(self, 'Errore', 'Selezionare un dipendente specifico! ', QMessageBox.Ok)
            return

    def generaComboBox(self, onText, *args):
        tendina = QComboBox()
        tendina.addItems([*args])

        tendina.currentTextChanged.connect(self.selezionaProffessione)

        return tendina

    def generaBottone(self, titolo, onClick):
        button = QPushButton(titolo)
        button.clicked.connect(onClick)
        return button

    def generaLinea(self, nomeLabel, label):# da aggiungere la var placeholder
        layoutOriz = QHBoxLayout()
        nLabel = QLabel(label)
        nLabel.setFixedWidth(100)
        layoutOriz.addWidget(nLabel)
        testo = QLineEdit(self)
        layoutOriz.addWidget(testo)
        layoutOriz.addStretch()
        self.parametriRicerca[nomeLabel] = testo

        return layoutOriz

    def chiudiFinestra(self):
        self.close()

    def logout(self):
        self.bLogout()
        self.close()
        pass