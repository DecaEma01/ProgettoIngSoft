import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QSizePolicy, QHBoxLayout, QVBoxLayout, QLineEdit, QLabel, QSpacerItem
from PyQt5 import QtCore, QtGui, QtWidgets

from Pazienti.ViewsPazienti.GestionePazientiView import GestionePazientiView
from Prenotazioni.ViewsPrenotazioni.GestionePrenotazioniView import GestionePrenotazioniView


class SegretarioHomeView(QWidget):

    def __init__(self,app,  parent = None):
        super(SegretarioHomeView, self).__init__(parent)

        self.parametriAutentificazione = {}

        layoutVertMain = QVBoxLayout()

        layoutBottoneLogOut = QHBoxLayout()
        layoutVertMain.addWidget(self.generaBottone('LOGOUT', lambda: self.chiudiApp(app), False))
        layoutVertMain.addLayout(layoutBottoneLogOut)

        layoutVertMain.addWidget(self.generaBottone('Gestione Prenotazioni', lambda: self.gestionePrenotazioni(app)))
        layoutVertMain.addWidget(self.generaBottone('Gestione Pazienti', lambda: self.gestionePazienti(app)))

        self.setLayout(layoutVertMain)
        self.resize(900, 700)
        self.setWindowTitle('Segretario - Home')

    def generaBottone(self, titolo, onClick, expanding = True, width = None):
        button = QPushButton(titolo)
        if expanding:
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        if width:
            button.setFixedWidth(width)
        button.clicked.connect(onClick)
        return button

    def chiudiApp(self, app):
        sys.exit(app.exec_())

    def gestionePrenotazioni(self,app):
        self.vistaGestionePrenotazioni = QtWidgets.QWidget()
        uivistaGestionePrenotazioni = GestionePrenotazioniView()
        uivistaGestionePrenotazioni.setupUi(self.vistaGestionePrenotazioni, app)
        self.vistaGestionePrenotazioni.show()

        #Form = QtWidgets.QWidget()
        #ui = GestionePrenotazioniView()
        #ui.setupUi(Form, app)
        #Form.show()

    def gestionePazienti(self,app):
        self.vistaGestionePrenotazioni = QtWidgets.QWidget()
        uivistaGestionePrenotazioni = GestionePazientiView()
        uivistaGestionePrenotazioni.setupUi(self.vistaGestionePrenotazioni, app)
        self.vistaGestionePrenotazioni.show()