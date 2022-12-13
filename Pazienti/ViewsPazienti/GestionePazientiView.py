from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from Pazienti.ViewsPazienti.NuovoPazienteView import NuovoPazienteView
from Pazienti.ViewsPazienti.PazientiRegistratiView import PazientiRegistratiView

class GestionePazientiView(object):
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
        
        # PUSH BUTTON
        
        self.indietroButton = QtWidgets.QPushButton(Form)
        self.indietroButton.setObjectName("indietroButton")
        self.gridLayout.addWidget(self.indietroButton, 0, 0, 1, 1)
        self.indietroButton.clicked.connect(Form.close)
        
        self.logoutButton = QtWidgets.QPushButton(Form)
        self.logoutButton.setObjectName("logoutButton")
        self.gridLayout.addWidget(self.logoutButton, 0, 1, 1, 1)
        self.logoutButton.clicked.connect(exit)
        
        self.registroButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.registroButton.sizePolicy().hasHeightForWidth())
        self.registroButton.setSizePolicy(sizePolicy)
        self.registroButton.setObjectName("registroButton")
        self.gridLayout.addWidget(self.registroButton, 1, 0, 1, 2)
        self.registroButton.clicked.connect(lambda: self.exRegistro(app))

        self.nuovoButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nuovoButton.sizePolicy().hasHeightForWidth())
        self.nuovoButton.setSizePolicy(sizePolicy)
        self.nuovoButton.setObjectName("nuovoButton")
        self.gridLayout.addWidget(self.nuovoButton, 2, 0, 1, 2)
        self.nuovoButton.clicked.connect(lambda: self.exNuovo(app))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Segretario - Gestione pazienti"))
        self.indietroButton.setText(_translate("Form", "INDIETRO"))
        self.logoutButton.setText(_translate("Form", "LOGOUT"))
        self.registroButton.setText(_translate("Form", "Registro pazienti"))
        self.nuovoButton.setText(_translate("Form", "Nuovo paziente"))
        
    def exRegistro(self, app):
        self.viewRegistro = QtWidgets.QWidget()
        uiviewRegistro = PazientiRegistratiView()
        uiviewRegistro.setupUi(self.viewRegistro, app)
        self.viewRegistro.show()
        
    def exNuovo(self, app):
        self.viewNuovo = QtWidgets.QWidget()
        uiviewNuovo = NuovoPazienteView()
        uiviewNuovo.setupUi(self.viewNuovo, app)
        self.viewNuovo.show()
