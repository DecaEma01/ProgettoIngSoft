from PyQt5.QtWidgets import *
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from Amministratore.Dipendenti.ControllersDipendenti.GestioneDipendentiController import GestioneDipendentiController

class NuovoDipendenteView(QWidget):

    def __init__(self, proffessioneDipendente):
        super(NuovoDipendenteView, self).__init__()

        self.resize(900, 700)

        #self.callback = callback
        self.proffessioneDipendente = proffessioneDipendente
        layoutVerticale = QVBoxLayout()     # LAYOUT MAIN
        layoutOrizButton = QHBoxLayout()

        self.attributiDipendente = {}

        #dati sensibili
        layoutVerticale.addLayout(self.generaLinea('nome', 'Nome: '))
        layoutVerticale.addLayout(self.generaLinea('cognome', 'Cognome: '))
        layoutVerticale.addLayout(self.generaLinea('codicefiscale', 'Codice Fiscale: '))
        layoutVerticale.addLayout(self.generaLinea('telefono', 'Telefono: '))

        layoutVerticale.addLayout(self.generaLineaIndirizzo())

        # contenitore dei certificati
        if self.proffessioneDipendente == 'Fisioterapista':
            layoutVerticale.addItem(QSpacerItem(75, 50))
            descrizione = QLabel('Certificazioni possedute:')
            layoutVerticale.addWidget(descrizione)
            layoutVerticale.addLayout(self.generaLayoutCertificazioni())

        layoutOrizButton.addStretch()

        layoutOrizButton.addWidget(self.generaBottone('Ok', self.nuovoDipendente))
        layoutOrizButton.addWidget(self.generaBottone('Cancel', self.chiudiFinestra))

        layoutVerticale.addStretch()
        layoutVerticale.addLayout(layoutOrizButton)

        self.setLayout(layoutVerticale)
        self.setWindowTitle('Amministratore - crea ' + self.proffessioneDipendente)

    def generaBottone(self, titolo, onClick):
        button = QPushButton(titolo)
        button.setFixedWidth(90)
        button.clicked.connect(onClick)
        return button

    def generaLinea(self, nomeLabel, label):# da aggiungere la var placeholder
        layoutOriz = QHBoxLayout()
        nLabel = QLabel(label)
        nLabel.setFixedWidth(100)
        layoutOriz.addWidget(nLabel)
        testo = QLineEdit(self)
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
        layoutOriz.addWidget(via)
        civico = QLineEdit()
        civico.setPlaceholderText('N°')
        civico.setFixedWidth(30)
        layoutOriz.addWidget(civico)
        citta = QLineEdit()
        citta.setPlaceholderText('Città')
        layoutOriz.addWidget(citta)
        provincia = QLineEdit()
        provincia.setPlaceholderText('Provincia')
        layoutOriz.addWidget(provincia)
        layoutOriz.addStretch()
        self.attributiDipendente['via'] = via
        self.attributiDipendente['numeroCivico'] = civico
        self.attributiDipendente['citta'] = citta
        self.attributiDipendente['provincia'] = provincia

        return layoutOriz

    def generaLayoutCertificazioni(self):
        layoutOrizzontale = QHBoxLayout()
        layoutVerticale = QVBoxLayout()

        self.listaCertificazioni = QListView()
        self.listViewModel = QStandardItemModel()

        layoutOrizzontale.addWidget(self.listaCertificazioni)

        layoutVerticale.addWidget(self.generaBottone('Aggiungi', self.aggiungiCertificazione))
        layoutVerticale.addWidget(self.generaBottone('Elimina', self.eliminaCertificazione))
        layoutVerticale.addStretch()

        layoutOrizzontale.addLayout(layoutVerticale)

        return layoutOrizzontale

    def aggiungiCertificazione(self):

        window = QWidget()
        window.resize(100, 100)
        window.setWindowTitle("CodersLegacy")

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

    def nuovoDipendente(self):

        # controllo campi inseriti
        try:
            for chiave in self.attributiDipendente:
                if self.attributiDipendente[chiave].text() == '':
                    raise Exception()
        except:
            QMessageBox.critical(self, 'Errore', 'Tutti i campi sono obbligatori! ', QMessageBox.Ok)
            return

        # controllo esistenza dipendente con lo stesso codice fiscale
        try:
            elencoDip = GestioneDipendentiController.listaDipendenti(GestioneDipendentiController)

            for chiave in elencoDip:
                if elencoDip[chiave].codicefiscale == self.attributiDipendente['codicefiscale'].text():
                    raise Exception()

        except:
            QMessageBox.critical(self, 'Errore', 'Esiste già un dipendente con lo stesso CF. Per inserirne uno nuovo,bisogna eliminare il vecchio! ', QMessageBox.Ok)
            return

        #controllo numero telefonico
        try:

            for valore in self.attributiDipendente['telefono'].text():
                if ord(valore)<48 or ord(valore)>57:
                    raise Exception()

        except:
            QMessageBox.critical(self, 'Errore', 'Il numero di telefono contiene dei valori scorretti ', QMessageBox.Ok)
            return

        for chiave5 in self.attributiDipendente:
            print(self.attributiDipendente[chiave5].text())

        self.creaDipendente()
        print('son qui')
        self.close()

    def creaDipendente(self):

        args = []
        args.append(self.attributiDipendente['nome'].text())
        args.append(self.attributiDipendente['cognome'].text())
        args.append(self.attributiDipendente['codicefiscale'].text())
        args.append(self.attributiDipendente['telefono'].text())
        args.append(self.attributiDipendente['via'].text())
        args.append(self.attributiDipendente['numeroCivico'].text())
        args.append(self.attributiDipendente['citta'].text())
        args.append(self.attributiDipendente['provincia'].text())

        if self.proffessioneDipendente == 'Fisioterapista':
            listaCertificazioni = []

            if self.listViewModel.rowCount() != 0:
                for index in range(self.listViewModel.rowCount()):
                    listaCertificazioni.append(self.listViewModel.item(index).text().split(": ")[1])

            args.append(listaCertificazioni)

        GestioneDipendentiController.creaDipendete(GestioneDipendentiController, self.proffessioneDipendente, *args)


    def chiudiFinestra(self):
        self.close()
