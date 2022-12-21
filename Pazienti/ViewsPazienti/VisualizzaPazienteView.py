from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from Pazienti.ViewsPazienti.ModificaPazienteView import ModificaPazienteView
from Pazienti.ControllersPazienti.PazienteController import PazienteController

class VisualizzaPazienteView(object):
    def setupUi(self, Form, app, paziente, callback):
        
        # INFO INIZIALI
        
        self.aggiornaListaPaz = callback
        self.paziente = paziente
        self.attributiPaziente = PazienteController.visualizzaPazienteC(self.paziente)
        prescrizioni = self.attributiPaziente['prescrizioni']
        
        Form.setObjectName("Form")
        Form.resize(900, 700)
        Form.setMinimumSize(QtCore.QSize(900, 700))
        font = QtGui.QFont()
        font.setPointSize(11)
        Form.setFont(font)
        
        # LAYOUT
        
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        
        self.prescrizioniScroll = QtWidgets.QScrollArea(Form)
        self.prescrizioniScroll.setMinimumSize(QtCore.QSize(900, 0))
        self.prescrizioniScroll.setWidgetResizable(True)
        self.prescrizioniScroll.setObjectName("prescrizioniScroll")
        
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 898, 379))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName("groupBox")
        
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout_2.setObjectName("formLayout_2")
        
        self.prescrizioniLayout = QtWidgets.QFormLayout()
        self.prescrizioniLayout.setObjectName("prescrizioniLayout")
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.prescrizioniLayout)
        
        self.verticalLayout.addWidget(self.groupBox)
        self.prescrizioniScroll.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.prescrizioniScroll, 8, 0, 1, 2)        

        # LABEL
        
        self.codiceLabel = QtWidgets.QLabel(Form)
        self.codiceLabel.setText(self.attributiPaziente['codicefiscale'])
        self.codiceLabel.setObjectName("codiceLabel")
        self.gridLayout.addWidget(self.codiceLabel, 5, 1, 1, 1)
        
        self.label_8 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)
        
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 2)
        self.cellulareLabel = QtWidgets.QLabel(Form)
        self.cellulareLabel.setText(self.attributiPaziente['telefono'])
        self.cellulareLabel.setObjectName("cellulareLabel")
        self.gridLayout.addWidget(self.cellulareLabel, 7, 1, 1, 1)
        
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        
        self.nomeLabel = QtWidgets.QLabel(Form)
        self.nomeLabel.setText(self.attributiPaziente['nome'])
        self.nomeLabel.setObjectName("nomeLabel")
        self.gridLayout.addWidget(self.nomeLabel, 3, 1, 1, 1)
        
        self.residenzaLabel = QtWidgets.QLabel(Form)
        self.residenzaLabel.setText(self.attributiPaziente['indirizzoResidenza'])
        self.residenzaLabel.setObjectName("residenzaLabel")
        self.gridLayout.addWidget(self.residenzaLabel, 6, 1, 1, 1)
        
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        
        self.cognomeLabel = QtWidgets.QLabel(Form)
        self.cognomeLabel.setText(self.attributiPaziente['cognome'])
        self.cognomeLabel.setObjectName("cognomeLabel")
        self.gridLayout.addWidget(self.cognomeLabel, 4, 1, 1, 1)

        # LINE EDIT
        
        
        
        # PUSH BUTTON
        
        self.modificaButton = QtWidgets.QPushButton(Form)
        self.modificaButton.setObjectName("modificaButton")
        self.gridLayout.addWidget(self.modificaButton, 9, 1, 1, 1)
        self.modificaButton.clicked.connect(lambda: self.exModifica(Form, app))
        
        self.indietroButton = QtWidgets.QPushButton(Form)
        self.indietroButton.setObjectName("indietroButton")
        self.gridLayout.addWidget(self.indietroButton, 1, 0, 1, 1)
        self.indietroButton.clicked.connect(Form.close)
        
        self.eliminaButton = QtWidgets.QPushButton(Form)
        self.eliminaButton.setObjectName("eliminaButton")
        self.gridLayout.addWidget(self.eliminaButton, 9, 0, 1, 1)
        self.eliminaButton.clicked.connect(lambda: self.exElimina(Form))
        
        self.logoutButton = QtWidgets.QPushButton(Form)
        self.logoutButton.setObjectName("logoutButton")
        self.gridLayout.addWidget(self.logoutButton, 1, 1, 1, 1)
        self.logoutButton.clicked.connect(exit)
        
        try:
            for key in prescrizioni:
                self.prescrizioniLayout.addRow(QtWidgets.QLabel(f'{key} - {prescrizioni[key]}'))
        except:
            print(prescrizioni)
        

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Segretario - Visualizza paziente"))
        self.label_8.setText(_translate("Form", "Cellulare:"))
        self.label_2.setText(_translate("Form", "Dettagli paziente"))
        self.modificaButton.setText(_translate("Form", "Modifica paziente"))
        self.label_5.setText(_translate("Form", "Cognome:"))
        self.label.setText(_translate("Form", "Segretario"))
        self.indietroButton.setText(_translate("Form", "Indietro"))
        self.label_7.setText(_translate("Form", "Residenza:"))
        self.eliminaButton.setText(_translate("Form", "Elimina paziente"))
        self.label_6.setText(_translate("Form", "Codice fiscale:"))
        self.label_4.setText(_translate("Form", "Nome:"))
        self.logoutButton.setText(_translate("Form", "LOGOUT"))
        self.groupBox.setTitle(_translate("Form", "Prescrizioni mediche registrate"))
        
    def exModifica(self, form, app):
        self.viewModifica = QtWidgets.QWidget()
        uiviewModifica = ModificaPazienteView()
        uiviewModifica.setupUi(self.viewModifica, app, self.paziente, callback = self.aggiornaListaPaz)
        self.viewModifica.show()
        form.close()
        
    def exElimina(self, form):
        msg = QtWidgets.QMessageBox()
        msg.setText("Confermare la scelta?")
        msg.setWindowTitle("Conferma eliminazione")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        risp = msg.exec_()
        if risp == QtWidgets.QMessageBox.Ok:
            PazienteController.eliminaPazienteC(PazienteController, self.paziente)
            self.aggiornaListaPaz()
            form.close()