from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from Pazienti.ControllersPazienti.ElencoPazientiController import ElencoPazientiController

from Pazienti.ControllersPazienti.PazienteController import PazienteController

class ModificaPazienteView(object):
    def setupUi(self, Form, app, paziente, callback):
        
        Form.setObjectName("Form")
        Form.resize(900, 700)
        Form.setMinimumSize(QtCore.QSize(900, 700))
        font = QtGui.QFont()
        font.setPointSize(11)
        Form.setFont(font)
        
        # INFO INIZIALI
        
        self.pazienteController = PazienteController()        
        
        self.aggiornaListaPaz = callback
        self.paziente = paziente
        self.prescrizioni = self.paziente.prescrizioni
        
        # LAYOUT
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.preScroll = QtWidgets.QScrollArea(Form)
        self.dettLayout = QtWidgets.QVBoxLayout()
        self.indLogLayout = QtWidgets.QHBoxLayout()
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.prescrizioniLayout = QtWidgets.QFormLayout()
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.formLayout_2 = QtWidgets.QFormLayout(self.scrollAreaWidgetContents)
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.prescrizioniLayout.setObjectName("prescrizioniLayout")
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout.setObjectName("verticalLayout")
        self.indLogLayout.setObjectName("indLogLayout")
        self.dettLayout.setObjectName("dettLayout")
        self.gridLayout.setObjectName("gridLayout")
        self.preScroll.setObjectName("preScroll")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.formLayout_2.setObjectName("formLayout_2")
        self.groupBox.setObjectName("groupBox")
        
        self.gridLayout.addLayout(self.indLogLayout, 1, 0, 1, 5)
        self.preScroll.setWidgetResizable(True)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 874, 252))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.prescrizioniLayout)
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.groupBox)
        self.preScroll.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.preScroll)
        self.gridLayout.addLayout(self.verticalLayout, 8, 0, 1, 5)
        
        # LABEL     
        
        self.dettLabel = QtWidgets.QLabel(Form)
        self.dettLabel.setObjectName("dettLabel")
        self.dettLayout.addWidget(self.dettLabel)
        self.gridLayout.addLayout(self.dettLayout, 2, 0, 1, 1)
        
        self.nomeLabel = QtWidgets.QLabel(Form)
        self.nomeLabel.setObjectName("nomeLabel")
        self.gridLayout.addWidget(self.nomeLabel, 3, 0, 1, 1)
        
        self.cognomeLabel = QtWidgets.QLabel(Form)
        self.cognomeLabel.setObjectName("cognomeLabel")
        self.gridLayout.addWidget(self.cognomeLabel, 4, 0, 1, 1)
        
        self.codiceLabel = QtWidgets.QLabel(Form)
        self.codiceLabel.setObjectName("codiceLabel")
        self.gridLayout.addWidget(self.codiceLabel, 5, 0, 1, 1)
        
        self.residenzaLabel = QtWidgets.QLabel(Form)
        self.residenzaLabel.setObjectName("residenzaLabel")
        self.gridLayout.addWidget(self.residenzaLabel, 6, 0, 1, 1)
        
        self.cellulareLabel = QtWidgets.QLabel(Form)
        self.cellulareLabel.setObjectName("cellulareLabel")
        self.gridLayout.addWidget(self.cellulareLabel, 7, 0, 1, 1)
        
        # LINE EDIT
        
        self.nomeEdit = QtWidgets.QLineEdit(Form)
        self.nomeEdit.setText(paziente.nome)
        self.nomeEdit.setObjectName("nomeEdit")
        self.gridLayout.addWidget(self.nomeEdit, 3, 1, 1, 4)
        
        self.cognomeEdit = QtWidgets.QLineEdit(Form)
        self.cognomeEdit.setText(paziente.cognome)
        self.cognomeEdit.setObjectName("cognomeEdit")
        self.gridLayout.addWidget(self.cognomeEdit, 4, 1, 1, 4)        
        
        self.codiceEdit = QtWidgets.QLineEdit(Form)
        self.codiceEdit.setText(paziente.codicefiscale)
        self.codiceEdit.setObjectName("codiceEdit")
        self.gridLayout.addWidget(self.codiceEdit, 5, 1, 1, 4)
        
        self.viaEdit = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.viaEdit.sizePolicy().hasHeightForWidth())
        self.viaEdit.setSizePolicy(sizePolicy)
        self.viaEdit.setText(str(paziente.via))
        self.viaEdit.setObjectName("viaEdit")
        self.gridLayout.addWidget(self.viaEdit, 6, 1, 1, 1)
        
        self.numCivEdit = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numCivEdit.sizePolicy().hasHeightForWidth())
        self.numCivEdit.setSizePolicy(sizePolicy)
        self.numCivEdit.setText(paziente.civico)
        self.numCivEdit.setObjectName("numCivEdit")
        self.gridLayout.addWidget(self.numCivEdit, 6, 2, 1, 1)
        
        self.cittaEdit = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cittaEdit.sizePolicy().hasHeightForWidth())
        self.cittaEdit.setSizePolicy(sizePolicy)
        self.cittaEdit.setText(paziente.citta)
        self.cittaEdit.setObjectName("cittaEdit")
        self.gridLayout.addWidget(self.cittaEdit, 6, 3, 1, 1)
        
        self.regioneEdit = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.regioneEdit.sizePolicy().hasHeightForWidth())
        self.regioneEdit.setSizePolicy(sizePolicy)
        self.regioneEdit.setText(paziente.provincia)
        self.regioneEdit.setObjectName("regioneEdit")
        self.gridLayout.addWidget(self.regioneEdit, 6, 4, 1, 1)
        
        self.cellulareEdit = QtWidgets.QLineEdit(Form)
        self.cellulareEdit.setText(paziente.telefono)
        self.cellulareEdit.setObjectName("cellulareEdit")
        self.gridLayout.addWidget(self.cellulareEdit, 7, 1, 1, 4)
        
        self.prescrEdit = QtWidgets.QLineEdit(Form)
        self.prescrEdit.setObjectName("prescrEdit")
        self.gridLayout.addWidget(self.prescrEdit, 9, 0, 1, 5)
        
        # PUSH BUTTON
        
        self.indietroButton = QtWidgets.QPushButton(Form)
        self.indietroButton.setObjectName("indietroButton")
        self.indLogLayout.addWidget(self.indietroButton)
        self.indietroButton.clicked.connect(Form.close)
        
        self.logoutButton = QtWidgets.QPushButton(Form)
        self.logoutButton.setObjectName("logoutButton")
        self.indLogLayout.addWidget(self.logoutButton)
        self.logoutButton.clicked.connect(exit)
       
        self.aggPrescrButton = QtWidgets.QPushButton(Form)        
        self.aggPrescrButton.setObjectName("aggPrescrButton")
        self.horizontalLayout.addWidget(self.aggPrescrButton)
        self.aggPrescrButton.clicked.connect(self.exAggiungi)
        
        self.rimPrescrButton = QtWidgets.QPushButton(Form)
        self.rimPrescrButton.setObjectName("rimPrescrButton")
        self.horizontalLayout.addWidget(self.rimPrescrButton)
        self.gridLayout.addLayout(self.horizontalLayout, 10, 0, 1, 5)
        self.rimPrescrButton.clicked.connect(lambda: self.exTogli(Form))
        
        self.salvaButton = QtWidgets.QPushButton(Form)
        self.salvaButton.setObjectName("salvaButton")
        self.gridLayout.addWidget(self.salvaButton, 11, 0, 1, 5)
        self.salvaButton.clicked.connect(lambda: self.exSalvaNuoviDatiPaziente(Form, self.paziente))

        self.aggiornaPrescrizioni(self.prescrizioni)
  
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Segretario - Modifica paziente"))
        self.dettLabel.setText(_translate("Form", "Dettagli paziente"))
        self.nomeLabel.setText(_translate("Form", "Nome:"))
        self.cognomeLabel.setText(_translate("Form", "Cognome:"))
        self.codiceLabel.setText(_translate("Form", "Codice fiscale:"))
        self.residenzaLabel.setText(_translate("Form", "Residenza:"))
        self.viaEdit.setPlaceholderText(_translate("Form", "Via"))
        self.numCivEdit.setPlaceholderText(_translate("Form", "Numero Civico"))
        self.cittaEdit.setPlaceholderText(_translate("Form", "Città"))
        self.regioneEdit.setPlaceholderText(_translate("Form", "Regione"))
        self.cellulareLabel.setText(_translate("Form", "Cellulare:"))
        self.indietroButton.setText(_translate("Form", "INDIETRO"))
        self.logoutButton.setText(_translate("Form", "LOGOUT"))
        self.groupBox.setTitle(_translate("Form", "Prescrizioni mediche registrate"))
        self.aggPrescrButton.setText(_translate("Form", "Aggiungi prescrizione medica"))
        self.rimPrescrButton.setText(_translate("Form", "Rimuovi prescrizione medica"))
        self.prescrEdit.setPlaceholderText(_translate("Form", "Prescrizione"))
        self.salvaButton.setText(_translate("Form", "Salva"))
        self.cellulareEdit.setPlaceholderText(_translate("Form", "Cellulare"))
        self.codiceEdit.setPlaceholderText(_translate("Form", "Codice fiscale"))
        self.cognomeEdit.setPlaceholderText(_translate("Form", "Cognome"))
        self.nomeEdit.setPlaceholderText(_translate("Form", "Nome"))
        
    def aggiornaPrescrizioni(self, prescr):
        try:
            for key in prescr:
                self.prescrizioniLayout.addRow(QtWidgets.QLabel(f'{key} - {prescr[key]}'))
        except:
            pass

    def cancellaLista(self):
        if self.prescrizioniLayout.rowCount != 0:
            while self.prescrizioniLayout.rowCount() > 0:
                self.prescrizioniLayout.removeRow(self.prescrizioniLayout.rowCount()-1)
    
    def exTogli(self, form):
        presente = False
        try:
            if self.prescrizioniLayout.rowCount != 0:
                
                ultimaPrescrizione = list(self.prescrizioni)[-1]
            
                for key in self.prescrizioni:
                    if self.prescrizioni[key] == self.prescrEdit.text():
                        self.prescrizioni[key] = self.prescrizioni[ultimaPrescrizione]
                        presente = True
                
                if presente == False:
                    raise Exception()

                self.cancellaLista()
                del self.prescrizioni[list(self.prescrizioni)[-1]]
                self.aggiornaPrescrizioni(self.prescrizioni)
                self.prescrEdit.setText('')       
        except:
            QtWidgets.QMessageBox.critical(form, 'Errore', 'Inserire il NOME di una prescrizione presente', QtWidgets.QMessageBox.Ok)
            return
        
    def exAggiungi(self):
        if self.prescrEdit.text() != '':
            self.prescrizioniLayout.addRow(QtWidgets.QLabel(f'{self.prescrizioniLayout.rowCount()+1} - {self.prescrEdit.text()}'))
            self.prescrizioni[self.prescrizioniLayout.rowCount()] = self.prescrEdit.text()
            self.prescrEdit.setText('')

    def exSalvaNuoviDatiPaziente(self, form, paziente):
        
        self.attributiPaziente = {'nome' : self.nomeEdit.text(),'cognome':self.cognomeEdit.text(),'codicefiscale':self.codiceEdit.text(),'telefono':self.cellulareEdit.text(),
            'via':self.viaEdit.text(),'numeroCivico':self.numCivEdit.text(),'citta':self.cittaEdit.text(),'provincia':self.regioneEdit.text(), 'prescrizioni':self.prescrizioni}        
        try:
            for chiave in self.attributiPaziente:
                if chiave != 'prescrizioni':
                    if self.attributiPaziente[chiave] == '':
                        raise Exception()
        except:
            QtWidgets.QMessageBox.critical(form, 'Errore', 'Tutti i campi sono obbligatori! ', QtWidgets.QMessageBox.Ok)
            return
        
        try:
            for chiave in self.attributiPaziente:
                if chiave == 'nome' or chiave == 'cognome' or chiave == 'via' or chiave == 'citta' or chiave == 'provincia':
                    if self.attributiPaziente[chiave].isalpha() == False:
                        raise Exception(chiave)
        except:
            QtWidgets.QMessageBox.critical(form, 'Errore', f"L'elemento {chiave} contiene dei numeri", QtWidgets.QMessageBox.Ok)
            return
        
        try:
            for chiave in self.attributiPaziente:
                if chiave == 'telefono' or chiave == 'numeroCivico':
                    if self.attributiPaziente[chiave].isnumeric() == False:
                        raise Exception(chiave)
        except:
            QtWidgets.QMessageBox.critical(form, 'Errore', f"L'elemento {chiave} contiene delle lettere", QtWidgets.QMessageBox.Ok)
            return
        if self.paziente.codicefiscale != self.attributiPaziente['codicefiscale']:
            if ElencoPazientiController.ricercaCodiceFiscaleC(ElencoPazientiController, self.attributiPaziente['codicefiscale']) == True:
                QtWidgets.QMessageBox.critical(form, 'Errore', 'Codice fiscale già presente in un altro paziente. Elimina il paziente vecchio per inserirne uno nuovo', QtWidgets.QMessageBox.Ok)
                return
        
        self.exSalva(form, paziente, self.attributiPaziente)
        self.aggiornaListaPaz()
        form.close()

    def exSalva(self, form, paziente, attributi):
        self.pazienteController.modificaPazienteC(paziente, 
            attributi['nome'],
            attributi['cognome'],
            attributi['codicefiscale'],
            attributi['telefono'],
            attributi['via'],
            attributi['numeroCivico'],
            attributi['citta'],
            attributi['provincia'],
            attributi['prescrizioni'])
            
        form.close()