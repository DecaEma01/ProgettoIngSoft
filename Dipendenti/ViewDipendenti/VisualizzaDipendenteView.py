from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QHBoxLayout, QPushButton, QMessageBox, QListView

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from Amministratore.Dipendenti.ViewDipendenti.ModificaDipendenteView import ModificaDipendenteView
from Amministratore.Dipendenti.ControllersDipendenti.GestioneDipendentiController import GestioneDipendentiController

class VisualizzaDipendenteView(QWidget):
    def __init__(self, dipendente, callback):
        super(VisualizzaDipendenteView, self).__init__()
        self.aggiornaListaDip = callback
        self.dipendente = dipendente
        gestoreDipendenti = GestioneDipendentiController()
        self.attributiDipendente = gestoreDipendenti.visualizzaDipendente(self.dipendente)

        self.resize(900, 700)

        layoutVerticale = QVBoxLayout()

        nome = f'{self.dipendente.nome} {self.dipendente.cognome}'
        labelNome = QLabel(nome)
        fontNome = labelNome.font()
        fontNome.setPointSize(20)
        labelNome.setFont(fontNome)

        layoutVerticale.addWidget(labelNome)
        layoutVerticale.addLayout(self.generaLinea("Nome:", self.attributiDipendente['nome']))
        layoutVerticale.addLayout(self.generaLinea("Cognome:", self.attributiDipendente['cognome']))
        layoutVerticale.addLayout(self.generaLinea("CF:", self.attributiDipendente['codicefiscale']))
        layoutVerticale.addLayout(self.generaLinea("Telefono:", self.attributiDipendente['telefono']))
        layoutVerticale.addLayout(self.generaLinea("Residenza:", self.attributiDipendente['indirizzoResidenza']))
        layoutVerticale.addLayout(self.generaLinea("Ruolo:", self.attributiDipendente['ruoloDipendente']))

        if type(self.dipendente).__name__ == "Fisioterapista":
            freeRow = QLabel('')
            layoutVerticale.addWidget(freeRow)
            descrizione = QLabel('Certificazioni possedute:')
            layoutVerticale.addWidget(descrizione)
            layoutVerticale.addWidget(self.generaListaCertificazioni())

        else:
            layoutVerticale.addItem(QSpacerItem(75, 50))

        layoutOrizontale = QHBoxLayout()
        layoutOrizontale.addWidget(self.generaBottone('Cancel', self.chiudiFinestra))
        layoutOrizontale.addStretch()
        layoutOrizontale.addWidget(self.generaBottone('Modifica', self.modificaDipendente))
        layoutOrizontale.addWidget(self.generaBottone('Elimina', self.eliminaDipendente))

        layoutVerticale.addLayout(layoutOrizontale)

        self.setLayout(layoutVerticale)
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
        self.modificaDipendente = ModificaDipendenteView(self.dipendente, callback=self.aggiornaListaDip)
        self.modificaDipendente.show()
        self.close()

    def chiudiFinestra(self):
        self.close()