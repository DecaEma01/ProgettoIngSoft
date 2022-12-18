import sys

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton, QLabel, QLineEdit, QComboBox, \
    QMessageBox, QSpacerItem

from Dipendenti.ControllersDipendenti.GestioneDipendentiController import GestioneDipendentiController
from Dipendenti.ViewsDipendenti.VisualizzaDipendenteView import VisualizzaDipendenteView

class DipendentiRegistratiView(QWidget):

    def __init__(self, app, parent=None):
        super(DipendentiRegistratiView, self).__init__(parent)
        self.app = app
        #self.bLogout = bLogout
        layoutVertMain = QVBoxLayout()                          # layout MAIN quello principale utilizzato dalla  vista
        self.listViewDipendenti = QListView()
        self.parametriRicerca = {}                              # è un dizionario contenente tutti i parametri aggiornati in tempo reale(per comodità tutti i parametri sono QLineEdit)
        self.aggiornaDipendenti()

        self.resize(900, 700)

        # QBUTTON (gestione account)
        layoutBottoniSwitch = QHBoxLayout()
        layoutBottoniSwitch.addWidget(self.generaBottone('INDIETRO', self.chiudiFinestra))
        layoutBottoniSwitch.addWidget(self.generaBottone('LOGOUT', self.logout))
        layoutVertMain.addLayout(layoutBottoniSwitch)       # Main
        layoutVertMain.addItem(QSpacerItem(10, 10))

        # COMBOBOX
        layoutCombo = QHBoxLayout()
        nLabel = QLabel("Ruolo:")
        nLabel.setMinimumWidth(100)
        layoutCombo.addWidget(nLabel)
        comboProfessione= self.generaComboBox(self.selezionaProffessione, 'nessuna scelta', 'Medico', 'Fisioterapista', 'Segretario')
        comboProfessione.setMinimumWidth(766)
        layoutCombo.addWidget(comboProfessione)
        layoutVertMain.addLayout(layoutCombo)

        # QLABLE + QLINE + 1 QBUTTON (ricerca)
        #layoutVertMain.addItem(QSpacerItem(10, 10))
        layoutVertMain.addLayout(self.generaLinea('nome', 'Nome:'))
        layoutVertMain.addLayout(self.generaLinea('cognome', 'Cognome:'))
        layoutVertMain.addLayout(self.generaLinea('codicefiscale', 'Codice Fiscale:'))
        layoutVertMain.addItem(QSpacerItem(10, 10))
        layoutVertMain.addWidget(self.generaBottone('Ricerca', self.ricercaDipendente))     # Main

        # QLISTVIEW
        layoutVertMain.addItem(QSpacerItem(10, 10))
        layoutVertMain.addWidget(self.listViewDipendenti)       # Main
        layoutVertMain.addItem(QSpacerItem(10, 10))

        # QBUTTON (aggiorna e visualizza)
        layoutBottoni = QHBoxLayout()
        BottoneReset = self.generaBottone('Ricerca senza filtri', self.aggiornaDipendenti)
        BottoneReset.setFixedWidth(415)
        layoutBottoni.addWidget(BottoneReset)
        layoutBottoni.addStretch()
        BottoneVisualizza = self.generaBottone('Visualizza dipendente', self.visualizzaDipendente)
        BottoneVisualizza.setFixedWidth(415)
        layoutBottoni.addWidget(BottoneVisualizza)
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
            nome = f'{dipendente.nome} {dipendente.cognome} : {dipendente.codicefiscale} - {dipendente.ruoloDipendente} {dipendente.codiceDipendente}'
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

    def ricercaDipendente(self):#DEVE MODIFICARE LA self.listViewDipendenti essenziale
        parametri = {}

        for chiave in self.parametriRicerca:
            if self.parametriRicerca[chiave].text() != '':
                parametri[chiave] = self.parametriRicerca[chiave].text()
                print(parametri[chiave])

        print('LISTA DEI PARAMETRI:')
        for chiave in parametri:
            print(parametri[chiave])

        dTrovati = GestioneDipendentiController.ricercaDipendente(GestioneDipendentiController, **parametri)
        lTrovati = []
        lTrovati.extend(dTrovati.values())
        listviewModel = QStandardItemModel()

        for dipendente in lTrovati:
            item = QStandardItem()
            nome = f'{dipendente.nome} {dipendente.cognome} : {dipendente.codicefiscale} - {type(dipendente).__name__} {dipendente.codiceDipendente}'
            item.setText(nome)
            item.setEditable(False)

            listviewModel.appendRow(item)   #viene inserito nella lista inserisce riga(row)
        self.listViewDipendenti.setModel(listviewModel)

    def visualizzaDipendente(self):
        try:
            selected = self.listViewDipendenti.selectedIndexes()[0].data()
            codice = int(selected.split("-")[1].strip().split(" ")[1])

            dipendente = GestioneDipendentiController.ricercaDipendente(GestioneDipendentiController, codiceDipendente = codice)[codice]

            self.vistaDipendente = VisualizzaDipendenteView(dipendente, self.app, callback = self.aggiornaDipendenti)
            self.vistaDipendente.show()

        except IndexError:
            print("IndexError")
            QMessageBox.critical(self, 'Errore', 'Selezionare un dipendente! ', QMessageBox.Ok)
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
        nLabel.setMinimumWidth(100)
        layoutOriz.addWidget(nLabel)
        testo = QLineEdit(self)
        testo.setMinimumWidth(755)
        layoutOriz.addWidget(testo)
        layoutOriz.addStretch()
        self.parametriRicerca[nomeLabel] = testo

        return layoutOriz

    def chiudiFinestra(self):
        self.close()

    def logout(self):
        sys.exit(self.app.exec_())
        #self.bLogout()
        #self.close()