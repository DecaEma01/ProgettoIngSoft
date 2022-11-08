from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QSizePolicy

from Pazienti.ViewsPazienti.NuovoPazienteView import NuovoPazienteView
from Pazienti.ViewsPazienti.PazientiRegistratiView import PazientiRegistratiView

class GestionePazientiView(QWidget):
    def __init__(self, parent = None):
        super(GestionePazientiView,self).__init__(parent)
        path = 'Pazienti/ViewsPazienti/UI/gestionePazienti.ui'
        uic.loadUi(path,self)

        self.logout = self.findChild(QPushButton, "logoutButton")
        self.registro = self.findChild(QPushButton, "registroButton")
        self.nuovo = self.findChild(QPushButton, "nuovoButton")

        self.logout.clicked.connect(exit)

        self.nuovo.clicked.connect(self.exNuovo)
        
        self.registro.clicked.connect(self.exRegistro)
    
    def exRegistro(self):
        self.viewPaz = PazientiRegistratiView(self.logout)
        self.viewPaz.show()
        
    def exNuovo(self):
        self.viewNuovo = NuovoPazienteView()
        self.viewNuovo.show()