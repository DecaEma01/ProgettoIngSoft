from PyQt5.QtWidgets import *
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from Amministratore.Dipendenti.ControllersDipendenti.GestioneDipendentiController import GestioneDipendentiController

class ModificaDipendenteView(QWidget):

    def __init__(self, dipendente, callback):
        super(ModificaDipendenteView, self).__init__()

        self.resize(900, 700)

        layoutVerticale = QVBoxLayout()     # LAYOUT MAIN
        layoutOrizButton = QHBoxLayout()

        self.aggiornaListaDip = callback
        self.dipendente = dipendente
        self.controllerDipendente = GestioneDipendentiController()
        self.attributiDipendente = self.controllerDipendente.visualizzaDipendente(self.dipendente)

        layoutVerticale.addLayout(self.generaLinea('nome', 'Nome: ', self.attributiDipendente['nome']))
        layoutVerticale.addLayout(self.generaLinea('cognome', 'Cognome: ', self.attributiDipendente['cognome']))
        layoutVerticale.addLayout(self.generaLinea('codicefiscale', 'Codice Fiscale: ', self.attributiDipendente['codicefiscale']))
        layoutVerticale.addLayout(self.generaLinea('telefono', 'Telefono: ', self.attributiDipendente['telefono']))

        layoutVerticale.addLayout(self.generaLineaIndirizzo())

        # contenitore dei certificati
        if type(self.dipendente).__name__ == 'Fisioterapista':
            layoutVerticale.addItem(QSpacerItem(75, 50))
            descrizione = QLabel('Certificazioni possedute:')
            layoutVerticale.addWidget(descrizione)
            layoutVerticale.addLayout(self.generaLayoutCertificazioni())

        layoutOrizButton.addWidget(self.generaBottone('Ok', self.nuoviDatiDipendente, False, 90))
        layoutOrizButton.addWidget(self.generaBottone('Cancel', self.chiudiFinestra, False, 90))

        layoutVerticale.addLayout(layoutOrizButton)

        self.setLayout(layoutVerticale)
        self.setWindowTitle('Amministratore - Modifica dipendente')

    def generaLinea(self, nomeLabel, label, infoDip):# da aggiungere la var placeholder
        layoutOriz = QHBoxLayout()
        nLabel = QLabel(label)
        nLabel.setFixedWidth(100)
        layoutOriz.addWidget(nLabel)
        testo = QLineEdit()
        testo.setText(infoDip)
        #testo.setMaximumWidth(500)
        testo.setMinimumWidth(300)
        #testo.setPlaceholderText() # da aggiungere la var placeholder
        layoutOriz.addWidget(testo)
        layoutOriz.addStretch()
        self.attributiDipendente[nomeLabel] = testo

        return layoutOriz

    def generaLineaIndirizzo(self):

        #indirizzoCompleto = QLineEdit()
        layoutOriz = QHBoxLayout()
        nomeRiga = QLabel('Indirizzo Residenza:')
        nomeRiga.setFixedWidth(100)
        layoutOriz.addWidget(nomeRiga)
        via = QLineEdit()
        via.setPlaceholderText('Via')
        via.setText(self.dipendente.indirizzoResidenza.via)
        layoutOriz.addWidget(via)
        civico = QLineEdit()
        civico.setPlaceholderText('N°')
        civico.setFixedWidth(30)
        civico.setText(self.dipendente.indirizzoResidenza.civico)
        layoutOriz.addWidget(civico)
        citta = QLineEdit()
        citta.setPlaceholderText('Città')
        citta.setText(self.dipendente.indirizzoResidenza.citta)
        layoutOriz.addWidget(citta)
        provincia = QLineEdit()
        provincia.setPlaceholderText('Provincia')
        provincia.setText(self.dipendente.indirizzoResidenza.regione)
        layoutOriz.addWidget(provincia)
        layoutOriz.addStretch()
        self.attributiDipendente['via'] = via
        self.attributiDipendente['numeroCivico'] = civico
        self.attributiDipendente['citta'] = citta
        self.attributiDipendente['provincia'] = provincia

        return layoutOriz

    def generaBottone(self, titolo, onClick,expanding = True, width = None):
        button = QPushButton(titolo)

        if expanding:
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        if width != None:
            button.setFixedWidth(width)

        button.clicked.connect(onClick)
        return button

    def generaLayoutCertificazioni(self):
        layoutOrizzontale = QHBoxLayout()
        layoutVerticale = QVBoxLayout()

        self.listaCertificazioni = QListView()
        self.listViewModel = QStandardItemModel()

        if len(self.attributiDipendente['listaCertificazioni']) != 0:
            for certificazione in self.attributiDipendente['listaCertificazioni']:
                item = QStandardItem()
                nome = f'Certificazione: {certificazione}'
                item.setText(nome)
                item.setEditable(False)
                self.listViewModel.appendRow(item)
                self.listaCertificazioni.setModel(self.listViewModel)

        layoutOrizzontale.addWidget(self.listaCertificazioni)

        layoutVerticale.addWidget(self.generaBottone('Aggiungi', self.aggiungiCertificazione, False))
        layoutVerticale.addWidget(self.generaBottone('Elimina', self.eliminaCertificazione, False))
        layoutVerticale.addStretch()

        layoutOrizzontale.addLayout(layoutVerticale)

        return layoutOrizzontale

    def aggiungiCertificazione(self):

        window = QWidget()
        window.resize(500, 400)
        window.setWindowTitle("Aggiungi certificazione")

        options = ("Magnetoterapia", "Elettroterapia", "Tecar-terapia", "Onde_d’urto", "Frems-terapia", "Laser-terapia",
                   "Ultrasuono-terapia", "utilizzo Formetric")
        option, pressed = QInputDialog.getItem(window, "Select Item", "Option:", options, 0, False)

        if pressed:
            try:
                if self.listViewModel.rowCount() != 0:
                    for index in range(self.listViewModel.rowCount()):
                        if option == self.listViewModel.item(index).text().split(": ")[1]:
                            raise Exception()
            except:
                QMessageBox.critical(self, 'Errore', 'Esiste già una certificazione del genere! ', QMessageBox.Ok)
                return
            item = QStandardItem()
            nome = f'Certificazione: {option}'
            item.setText(nome)
            item.setEditable(False)

            self.listViewModel.appendRow(item)
            # self.generaListaCertificazioni()
            self.listaCertificazioni.setModel(self.listViewModel)

    def eliminaCertificazione(self):
        try:
            selected = self.listaCertificazioni.selectedIndexes()[0].data()
            print(selected)

            for index in range(self.listViewModel.rowCount()):
                if selected == self.listViewModel.item(index).text():
                    self.listViewModel.removeRow(index)
                    break

            self.listaCertificazioni.setModel(self.listViewModel)

        except IndexError:
            print("IndexError")
            QMessageBox.critical(self, 'Errore', 'Selezionare una certificazione! ', QMessageBox.Ok)
            return

    def nuoviDatiDipendente(self):

        # controllo campi inseriti
        try:
            for chiave in self.attributiDipendente:
                if type(self.attributiDipendente[chiave]).__name__ !='list' :
                    if self.attributiDipendente[chiave] == '':
                        raise Exception()
        except:
            QMessageBox.critical(self, 'Errore', 'Tutti i campi sono obbligatori! ', QMessageBox.Ok)
            return

        # controllo esistenza dipendente con lo stesso codice fiscale
        try:
            elencoDip = GestioneDipendentiController.listaDipendenti(GestioneDipendentiController)

            for chiave in elencoDip:
                if elencoDip[chiave].codiceDipendente != self.dipendente.codiceDipendente:
                    if elencoDip[chiave].codicefiscale == self.attributiDipendente['codicefiscale'].text():
                        raise Exception()
        except:
            QMessageBox.critical(self, 'Errore', 'Esiste già un dipendente con lo stesso CF. Per inserirne uno nuovo,bisogna eliminare il vecchio! ', QMessageBox.Ok)
            return

        #controllo numero di telefono
        try:

            for valore in self.attributiDipendente['telefono'].text():
                if ord(valore)<48 or ord(valore)>57:
                    raise Exception()

        except:
            QMessageBox.critical(self, 'Errore', 'Il numero di telefono contiene dei valori scorretti ', QMessageBox.Ok)
            return

        self.modificaDipendente()
        print('modificato')
        self.aggiornaListaDip()
        self.close()

    def modificaDipendente(self):

        args = []
        args.append(self.attributiDipendente['nome'].text())
        args.append(self.attributiDipendente['cognome'].text())
        args.append(self.attributiDipendente['codicefiscale'].text())
        args.append(self.attributiDipendente['telefono'].text())
        args.append(self.attributiDipendente['via'].text())
        args.append(self.attributiDipendente['numeroCivico'].text())
        args.append(self.attributiDipendente['citta'].text())
        args.append(self.attributiDipendente['provincia'].text())

        if type(self.dipendente).__name__ == 'Fisioterapista':
            listaCertificazioni = []

            if self.listViewModel.rowCount() != 0:
                for index in range(self.listViewModel.rowCount()):
                    listaCertificazioni.append(self.listViewModel.item(index).text().split(": ")[1])

            args.append(listaCertificazioni)

        self.controllerDipendente.modificaDipendente(self.dipendente, *args)

    def chiudiFinestra(self):
        self.close()