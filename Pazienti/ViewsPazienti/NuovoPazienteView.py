from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from Pazienti.ControllersPazienti.PazienteController import PazienteController
from Pazienti.ControllersPazienti.ElencoPazientiController import ElencoPazientiController

class NuovoPazienteView(object):
    
    def setupUi(self, Form, app):
      
        Form.setObjectName("Form")
        Form.resize(900, 700)
        Form.setMinimumSize(QtCore.QSize(900, 700))
        font = QtGui.QFont()
        font.setPointSize(11)
        Form.setFont(font)
        
        # LAYOUT
        
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        
        self.indLogLayout = QtWidgets.QHBoxLayout()
        self.indLogLayout.setObjectName("indLogLayout")
        
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.preScroll = QtWidgets.QScrollArea(Form)
        self.preScroll.setWidgetResizable(True)
        self.preScroll.setObjectName("preScroll")
        
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 874, 254))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        
        self.formLayout_2 = QtWidgets.QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout_2.setObjectName("formLayout_2")
        
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        
        self.prescrizioniLayout = QtWidgets.QFormLayout()
        self.prescrizioniLayout.setObjectName("prescrizioniLayout")
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.prescrizioniLayout)
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.groupBox)
        
        self.preScroll.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.preScroll)
        self.gridLayout.addLayout(self.verticalLayout, 8, 0, 1, 5)
        
        self.dettLayout = QtWidgets.QVBoxLayout()
        self.dettLayout.setObjectName("dettLayout")
        self.gridLayout.addLayout(self.dettLayout, 2, 0, 1, 5)

        # LABEL
        
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
        
        self.dettLabel = QtWidgets.QLabel(Form)
        self.dettLabel.setObjectName("dettLabel")
        self.dettLayout.addWidget(self.dettLabel)
        
        # LINE EDIT

        self.nomeEdit = QtWidgets.QLineEdit(Form)
        self.nomeEdit.setText("")
        self.nomeEdit.setObjectName("nomeEdit")
        self.gridLayout.addWidget(self.nomeEdit, 3, 1, 1, 4)
        
        self.cognomeEdit = QtWidgets.QLineEdit(Form)
        self.cognomeEdit.setObjectName("cognomeEdit")
        self.gridLayout.addWidget(self.cognomeEdit, 4, 1, 1, 4)
        
        self.codiceEdit = QtWidgets.QLineEdit(Form)
        self.codiceEdit.setObjectName("codiceEdit")
        self.gridLayout.addWidget(self.codiceEdit, 5, 1, 1, 4)
        
        self.viaEdit = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.viaEdit.sizePolicy().hasHeightForWidth())
        self.viaEdit.setSizePolicy(sizePolicy)
        self.viaEdit.setText("")
        self.viaEdit.setObjectName("viaEdit")
        self.gridLayout.addWidget(self.viaEdit, 6, 1, 1, 1)
        
        self.numCivEdit = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numCivEdit.sizePolicy().hasHeightForWidth())
        self.numCivEdit.setSizePolicy(sizePolicy)
        self.numCivEdit.setObjectName("numCivEdit")
        self.gridLayout.addWidget(self.numCivEdit, 6, 2, 1, 1)
        
        self.cittaEdit = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cittaEdit.sizePolicy().hasHeightForWidth())
        self.cittaEdit.setSizePolicy(sizePolicy)
        self.cittaEdit.setObjectName("cittaEdit")
        self.gridLayout.addWidget(self.cittaEdit, 6, 3, 1, 1)
        
        self.regioneEdit = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.regioneEdit.sizePolicy().hasHeightForWidth())
        self.regioneEdit.setSizePolicy(sizePolicy)
        self.regioneEdit.setObjectName("regioneEdit")
        self.gridLayout.addWidget(self.regioneEdit, 6, 4, 1, 1)
        
        
        self.cellulareEdit = QtWidgets.QLineEdit(Form)
        self.cellulareEdit.setObjectName("cellulareEdit")
        self.gridLayout.addWidget(self.cellulareEdit, 7, 1, 1, 4)
        
        self.prescrEdit = QtWidgets.QLineEdit(Form)
        self.prescrEdit.setObjectName("prescrEdit")
        self.gridLayout.addWidget(self.prescrEdit, 9, 0, 1, 5)
        
        # ATTRIBUTI AGGIUNTIVI
        
        self.controllerPaziente = PazienteController()
        self.prescrizioni = {}
        self.attributiPaziente = {}
        
        
        # PUSH BUTTON
        
        self.indietroButton = QtWidgets.QPushButton(Form)
        self.indietroButton.setObjectName("indietroButton")
        self.indLogLayout.addWidget(self.indietroButton)
        self.indietroButton.clicked.connect(Form.close)
        
        self.logoutButton = QtWidgets.QPushButton(Form)
        self.logoutButton.setObjectName("logoutButton")
        self.indLogLayout.addWidget(self.logoutButton)
        self.gridLayout.addLayout(self.indLogLayout, 1, 0, 1, 5)
        self.logoutButton.clicked.connect(exit)
        
        self.aggPrescrButton = QtWidgets.QPushButton(Form)
        self.aggPrescrButton.setObjectName("aggPrescrButton")
        self.gridLayout.addWidget(self.aggPrescrButton, 10, 0, 1, 5)
        self.aggPrescrButton.clicked.connect(self.exAggiungi)
        
        self.salvaButton = QtWidgets.QPushButton(Form)
        self.salvaButton.setObjectName("salvaButton")
        self.gridLayout.addWidget(self.salvaButton, 11, 0, 1, 5)
        self.salvaButton.clicked.connect(lambda: self.exSalva(Form, self.attributiPaziente))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Segretario - Nuovo paziente"))
        self.nomeLabel.setText(_translate("Form", "Nome:"))
        self.cognomeLabel.setText(_translate("Form", "Cognome:"))
        self.codiceLabel.setText(_translate("Form", "Codice fiscale:"))
        self.residenzaLabel.setText(_translate("Form", "Residenza:"))
        self.dettLabel.setText(_translate("Form", "Dettagli paziente"))
        self.cellulareLabel.setText(_translate("Form", "Cellulare:"))
        self.nomeEdit.setPlaceholderText(_translate("Form", "Nome"))
        self.cognomeEdit.setPlaceholderText(_translate("Form", "Cognome"))
        self.codiceEdit.setPlaceholderText(_translate("Form", "Codice fiscale"))
        self.viaEdit.setPlaceholderText(_translate("Form", "Via"))
        self.numCivEdit.setPlaceholderText(_translate("Form", "Numero Civico"))
        self.cittaEdit.setPlaceholderText(_translate("Form", "Città"))
        self.regioneEdit.setPlaceholderText(_translate("Form", "Provincia"))
        self.cellulareEdit.setPlaceholderText(_translate("Form", "Cellulare"))
        self.prescrEdit.setPlaceholderText(_translate("Form", "Prescrizione"))
        self.indietroButton.setText(_translate("Form", "INDIETRO"))
        self.logoutButton.setText(_translate("Form", "LOGOUT"))
        self.groupBox.setTitle(_translate("Form", "Prescrizioni mediche registrate"))
        self.aggPrescrButton.setText(_translate("Form", "Aggiungi prescrizione medica"))
        self.salvaButton.setText(_translate("Form", "Salva"))
    
    def exAggiungi(self):
        if self.prescrEdit.text() != '':
            self.prescrizioniLayout.addRow(QtWidgets.QLabel(f'{self.prescrizioniLayout.rowCount()+1} - {self.prescrEdit.text()}'))
            self.prescrizioni[self.prescrizioniLayout.rowCount()] = self.prescrEdit.text()
            self.prescrEdit.setText('')

    def exSalva(self, form, attributi):
        
        attributi = {'nome' : self.nomeEdit.text(),'cognome':self.cognomeEdit.text(),'codicefiscale':self.codiceEdit.text(),'telefono':self.cellulareEdit.text(),
            'via':self.viaEdit.text(),'numeroCivico':self.numCivEdit.text(),'citta':self.cittaEdit.text(),'provincia':self.regioneEdit.text(), 'prescrizioni':self.prescrizioni}
        
        try:
            for chiave in attributi:
                if chiave != 'prescrizioni':
                    if attributi[chiave] == '':
                        raise Exception()
        except:
            QtWidgets.QMessageBox.critical(form, 'Errore', 'Tutti i campi sono obbligatori! ', QtWidgets.QMessageBox.Ok)
            return
        
        try:
            for chiave in attributi:
                if chiave == 'nome' or chiave == 'cognome' or chiave == 'via' or chiave == 'citta' or chiave == 'provincia':
                    if attributi[chiave].isalpha() == False:
                        raise Exception(chiave)
        except:
            QtWidgets.QMessageBox.critical(form, 'Errore', f"L'elemento {chiave} contiene dei numeri", QtWidgets.QMessageBox.Ok)
            return
        
        try:
            for chiave in attributi:
                if chiave == 'telefono' or chiave == 'numeroCivico':
                    if attributi[chiave].isnumeric() == False:
                        raise Exception(chiave)
        except:
            QtWidgets.QMessageBox.critical(form, 'Errore', f"L'elemento {chiave} contiene delle lettere", QtWidgets.QMessageBox.Ok)
            return
        
        if ElencoPazientiController.ricercaCodiceFiscaleC(ElencoPazientiController, attributi['codicefiscale']) == True:
            QtWidgets.QMessageBox.critical(form, 'Errore', 'Codice fiscale già presente in un altro paziente. Elimina il paziente vecchio per inserirne uno nuovo', QtWidgets.QMessageBox.Ok)
            return

        self.creaPaziente(attributi)
        form.close()

    def creaPaziente(self, attributi):
        self.controllerPaziente.creaPazienteC(attributi['nome'],
            attributi['cognome'],
            attributi['codicefiscale'],
            attributi['telefono'],
            attributi['via'],
            attributi['numeroCivico'],
            attributi['citta'],
            attributi['provincia'],
            attributi['prescrizioni'])