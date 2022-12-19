from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from PyQt5.QtGui import QStandardItemModel, QStandardItem

from Pazienti.ControllersPazienti.ElencoPazientiController import ElencoPazientiController
from Pazienti.ViewsPazienti.VisualizzaPazienteView import VisualizzaPazienteView

class PazientiRegistratiView(object):
    
    def setupUi(self, Form, app):
        
        Form.setObjectName("Form")
        Form.resize(900, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(900, 700))
        font = QtGui.QFont()
        font.setPointSize(11)
        Form.setFont(font)
        
        # LAYOUT
        
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
  
        # LABEL
        
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        
        self.label_3 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        
        self.label_4 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")        
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        
        self.listView = QtWidgets.QListView(Form)
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 6, 0, 1, 2)
        
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
       
        # LINE EDIT

        self.codEdit = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.codEdit.sizePolicy().hasHeightForWidth())        
        self.codEdit.setSizePolicy(sizePolicy)
        self.codEdit.setObjectName("codEdit")
        self.gridLayout.addWidget(self.codEdit, 3, 1, 1, 1)
        
        self.nomeEdit = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)        
        sizePolicy.setHeightForWidth(self.nomeEdit.sizePolicy().hasHeightForWidth())
        self.nomeEdit.setSizePolicy(sizePolicy)
        self.nomeEdit.setObjectName("nomeEdit")
        self.horizontalLayout_2.addWidget(self.nomeEdit)
        
        self.cognomeEdit = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cognomeEdit.sizePolicy().hasHeightForWidth())
        self.cognomeEdit.setSizePolicy(sizePolicy)
        self.cognomeEdit.setObjectName("cognomeEdit")
        self.horizontalLayout_2.addWidget(self.cognomeEdit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 1, 1, 1)     
        
        # PUSH BUTTON
        
        self.ricercaButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ricercaButton.sizePolicy().hasHeightForWidth())
        self.ricercaButton.setSizePolicy(sizePolicy)
        self.ricercaButton.setObjectName("ricercaButton")
        self.gridLayout.addWidget(self.ricercaButton, 5, 0, 1, 2)
        self.ricercaButton.clicked.connect(self.ricercaPaziente)
        
        self.indietroButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.indietroButton.sizePolicy().hasHeightForWidth())
        self.indietroButton.setSizePolicy(sizePolicy)
        self.indietroButton.setObjectName("indietroButton")
        self.horizontalLayout_3.addWidget(self.indietroButton)
        self.indietroButton.clicked.connect(Form.close)
        
        self.logoutButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logoutButton.sizePolicy().hasHeightForWidth())
        self.logoutButton.setSizePolicy(sizePolicy)
        self.logoutButton.setObjectName("logoutButton")
        self.horizontalLayout_3.addWidget(self.logoutButton)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 2)
        self.logoutButton.clicked.connect(exit)
        
        self.visualizzaButton = QtWidgets.QPushButton(Form)
        self.visualizzaButton.setObjectName("visualizzaButton")
        self.gridLayout.addWidget(self.visualizzaButton, 7, 0, 1, 2)
        self.visualizzaButton.clicked.connect(lambda: self.visualizzaPaziente(Form, app))
        
        # ALTRO
        
        self.parametriRicerca = {'codicefiscale':self.codEdit,'nome':self.nomeEdit,'cognome':self.cognomeEdit}
        self.aggiornaPazienti()
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Segretario - Registro pazienti"))
        self.label_2.setText(_translate("Form", "Filtri:"))
        self.label_3.setText(_translate("Form", "Ricerca per codice fiscale: "))
        self.codEdit.setPlaceholderText(_translate("Form", "Codice fiscale"))
        self.label_4.setText(_translate("Form", "Ricerca per nome e cognome: "))
        self.nomeEdit.setPlaceholderText(_translate("Form", "Nome"))
        self.cognomeEdit.setPlaceholderText(_translate("Form", "Cognome"))
        self.ricercaButton.setText(_translate("Form", "Ricerca"))
        self.indietroButton.setText(_translate("Form", "INDIETRO"))
        self.logoutButton.setText(_translate("Form", "LOGOUT"))
        self.visualizzaButton.setText(_translate("Form", "Visualizza"))
        
    def caricaPazienti(self):
        pazienti = ElencoPazientiController.listaPazientiC(ElencoPazientiController)
        self.pazienti.extend(pazienti.values())
        
    def aggiornaPazienti(self):
        self.pazienti = []
        self.caricaPazienti()
        listviewModel = QStandardItemModel(self.listView)
        for paziente in self.pazienti:
            item = QStandardItem()
            nome = f'{paziente.codicePaziente} - {paziente.nome} {paziente.cognome} : {paziente.codicefiscale}'
            item.setText(nome)
            item.setEditable(False)

            listviewModel.appendRow(item)   #viene inserito nella lista inserisce riga(row)
        self.listView.setModel(listviewModel)
        
    def ricercaPaziente(self):
        parametri = {}

        for chiave in self.parametriRicerca:
            if self.parametriRicerca[chiave].text() != '':
                parametri[chiave] = self.parametriRicerca[chiave].text()

        pTrovati = ElencoPazientiController.ricercaPazienteC(ElencoPazientiController, **parametri)
        lTrovati = []
        lTrovati.extend(pTrovati.values())
        listviewModel = QStandardItemModel(self.listView)

        for paziente in lTrovati:
            item = QStandardItem()
            nome = f'{paziente.codicePaziente} - {paziente.nome} {paziente.cognome} : {paziente.codicefiscale}'
            item.setText(nome)
            item.setEditable(False)

            listviewModel.appendRow(item)   #viene inserito nella lista inserisce riga(row)
        self.listView.setModel(listviewModel)
        
    def visualizzaPaziente(self, form, app):
        try:
            selected = self.listView.selectedIndexes()[0].data()
            sel = selected.split()
            codice = int(sel[0])

            paziente = ElencoPazientiController.ricercaPazienteC(ElencoPazientiController, codicePaziente = codice)[codice]

            self.viewVisualizza = QtWidgets.QWidget()
            uiviewVisualizza = VisualizzaPazienteView()
            uiviewVisualizza.setupUi(self.viewVisualizza, app, paziente, callback = self.aggiornaPazienti)
            self.viewVisualizza.show()

        except IndexError:
            QtWidgets.QMessageBox.critical(form, 'Errore', 'Selezionare un paziente! ', QtWidgets.QMessageBox.Ok)
            return