import sys

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QHBoxLayout, QPushButton, QMessageBox, QListView

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from Dipendenti.ViewsDipendenti.ModificaDipendenteView import ModificaDipendenteView
from Dipendenti.ControllersDipendenti.GestioneDipendentiController import GestioneDipendentiController

class VisualizzaDipendenteView(QWidget):
    def __init__(self, dipendente, app, callback):
        super(VisualizzaDipendenteView, self).__init__()
        self.aggiornaListaDip = callback
        self.dipendente = dipendente
        self.app = app
        #self.bLogout = bLogout
        gestoreDipendenti = GestioneDipendentiController()
        self.attributiDipendente = gestoreDipendenti.visualizzaDipendente(self.dipendente)

        self.resize(900, 700)

        layoutContenitore = QHBoxLayout()
        layoutVerticale = QVBoxLayout()

        layoutBottoniSwitch = QHBoxLayout()
        layoutBottoniSwitch.addWidget(self.generaBottone('INDIETRO', self.chiudiFinestra))
        layoutBottoniSwitch.addWidget(self.generaBottone('LOGOUT', self.logout))
        layoutVerticale.addLayout(layoutBottoniSwitch)

        layoutContenitore.addItem(QSpacerItem(50, 50))
        layoutVerticale.addItem(QSpacerItem(50, 50))
        nome = f'{self.dipendente.nome} {self.dipendente.cognome}'
        labelNome = QLabel(nome)
        fontNome = labelNome.font()
        fontNome.setPointSize(20)
        labelNome.setFont(fontNome)

        layoutVerticale.addWidget(labelNome)
        layoutVerticale.addLayout(self.generaLinea("Nome:", self.attributiDipendente['nome']))
        layoutVerticale.addLayout(self.generaLinea("Cognome:", self.attributiDipendente['cognome']))
        layoutVerticale.addLayout(self.generaLinea("Codice Fiscale:", self.attributiDipendente['codicefiscale']))
        layoutVerticale.addLayout(self.generaLinea("Telefono:", self.attributiDipendente['telefono']))
        layoutVerticale.addLayout(self.generaLinea("Residenza:", self.attributiDipendente['indirizzoResidenza']))
        layoutVerticale.addLayout(self.generaLinea("Ruolo:", self.attributiDipendente['ruoloDipendente']))

        if type(self.dipendente).__name__ == "FisioterapistaModel":
            freeRow = QLabel('')
            layoutVerticale.addWidget(freeRow)
            descrizione = QLabel('Certificazioni possedute:')
            layoutVerticale.addWidget(descrizione)
            layoutVerticale.addWidget(self.generaListaCertificazioni())

        else:
            layoutVerticale.addItem(QSpacerItem(75, 50))

        layoutOrizontale = QHBoxLayout()
        layoutOrizontale.addStretch()
        BottoneModifica = self.generaBottone('Modifica', self.modificaDipendente)
        BottoneModifica.setFixedWidth(395)
        BottoneElimina = self.generaBottone('Elimina', self.eliminaDipendente)
        BottoneElimina.setFixedWidth(395)
        layoutOrizontale.addWidget(BottoneModifica)
        layoutOrizontale.addWidget(BottoneElimina)

        layoutVerticale.addLayout(layoutOrizontale)
        layoutVerticale.addItem(QSpacerItem(10, 10))
        layoutContenitore.addLayout(layoutVerticale)
        layoutContenitore.addItem(QSpacerItem(50, 50))

        self.setLayout(layoutContenitore)
        self.setWindowTitle('Amministratore - Scheda del dipendente')


    def generaBottone(self, titolo, onClick):
        button = QPushButton(titolo)
        button.clicked.connect(onClick)
        return button

    def generaLinea(self, label, contenuto):# da aggiungere la var placeholder
        layoutOriz = QHBoxLayout()
        nLabel = QLabel(label)
        nLabel.setFixedWidth(100)
        layoutOriz.addWidget(nLabel)
        testo = QLabel(contenuto)
        layoutOriz.addWidget(testo)
        layoutOriz.addStretch()

        return layoutOriz

    def generaListaCertificazioni(self):

        listaCertificazioni = QListView()
        listViewModel = QStandardItemModel()

        for certificazione in self.attributiDipendente["listaCertificazioni"]:
            item = QStandardItem()
            item.setEditable(False)
            nome = f'Certificazione: {certificazione}'
            item.setText(nome)

            listViewModel.appendRow(item)
            listaCertificazioni.setModel(listViewModel)

        return listaCertificazioni

    def eliminaDipendente(self):
        msg = QMessageBox()
        msg.setText("Confermare la scelta?")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        risp = msg.exec_()
        if risp == QMessageBox.Ok:
            print('ciaociao')
            gestoreDipendenti = GestioneDipendentiController()
            gestoreDipendenti.eliminaDipendente(self.dipendente)
            #self.dipendente.eliminaDipendente()
            self.aggiornaListaDip()
            self.close()

    def modificaDipendente(self):
        self.modificaDipendente = ModificaDipendenteView(self.dipendente, self.app, callback=self.aggiornaListaDip)
        self.modificaDipendente.show()
        self.close()

    def chiudiFinestra(self):
        self.close()

    def logout(self):
        sys.exit(self.app.exec_())