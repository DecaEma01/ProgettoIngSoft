import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QSizePolicy, QHBoxLayout, QVBoxLayout, QLineEdit, QLabel, QSpacerItem
from PyQt5 import QtCore, QtGui, QtWidgets

from Dipendenti.ViewsDipendenti.GestioneDipendentiView import GestioneDipendentiView
from TrattamentiConsulenze.ViewsTrattCons.GestioneTrattConsView import GestioneTrattConsView


class AmministratoreHomeView(QWidget):

    def __init__(self, app, parent = None):
        super(AmministratoreHomeView, self).__init__(parent)        # richiamiamo il costruttore di qWidget e li passiamo il parent none
        self.resize(900, 700)

        self.parametriAutentificazione = {}

        layoutVertMain = QVBoxLayout()

        layoutBottoneLogOut = QHBoxLayout()
        layoutVertMain.addWidget(self.generaBottone('LOGOUT', self.logOut, False))
        layoutVertMain.addLayout(layoutBottoneLogOut)

        layoutVertMain.addWidget(self.generaBottone('Gestione Trattamenti', lambda: self.gestioneTrattamenti(app)))
        layoutVertMain.addWidget(self.generaBottone('Gestione Dipendenti', self.gestioneDipendenti))

        self.setLayout(layoutVertMain)

        self.setWindowTitle('Amministratore - Gestione dipendenti')

    def generaBottone(self, titolo, onClick, expanding = True, width = None):
        button = QPushButton(titolo)
        if expanding:
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        if width:
            button.setFixedWidth(width)
        button.clicked.connect(onClick)
        return button

    def gestioneTrattamenti(self,app):
        Form = QtWidgets.QWidget()
        ui = GestioneTrattConsView()
        ui.setupUi(Form, app)
        Form.show()

    def gestioneDipendenti(self):
        self.vistaAmministrazioneDipendenti = GestioneDipendentiView(self.logOut)
        self.vistaAmministrazioneDipendenti.show()

    def logOut(self):
        self.close()
