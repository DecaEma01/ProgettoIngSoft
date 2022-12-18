import sys

from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QHBoxLayout,  QVBoxLayout
from Dipendenti.ViewsDipendenti.DipendentiRegistratiView import DipendentiRegistratiView
from Dipendenti.ViewsDipendenti.NuovoDipendenteView import NuovoDipendenteView


class GestioneDipendentiView(QWidget):

    def __init__(self, app, parent = None):
        super(GestioneDipendentiView, self).__init__(parent)
        self.app = app
        #self.bLogout = bLogout

        self.resize(900, 700)

        layoutVertMain = QVBoxLayout()
        layoutBottoniSwitch = QHBoxLayout()
        layoutBottoniSwitch.addWidget(self.generaBottone('INDIETRO', self.chiudiFinestra, False))
        layoutBottoniSwitch.addWidget(self.generaBottone('LOGOUT', self.logout, False))
        layoutVertMain.addLayout(layoutBottoniSwitch)

        gridLayot = QGridLayout()
        gridLayot.addWidget(self.generaBottone('Dipendenti Registrati', self.eseguiDipendentiRegistrati), 0, 0, 1, 3)
        gridLayot.addWidget(self.generaBottone('Nuovo Fisioterapista ', self.aggiungiFisioterapista), 1, 0)
        gridLayot.addWidget(self.generaBottone('Nuovo Medico', self.aggiungiMedico), 1, 1)
        gridLayot.addWidget(self.generaBottone('Nuovo Segretario', self.aggiungiSegretario), 1, 2)



        layoutVertMain.addLayout(gridLayot)
        self.setLayout(layoutVertMain)
        self.setWindowTitle('Amministratore - Gestione dipendenti')

    def generaBottone(self, titolo, onClick,expanding = True):
        button = QPushButton(titolo)
        if expanding:
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(onClick)
        return button

    def eseguiDipendentiRegistrati(self):
        self.vistaDip = DipendentiRegistratiView(self.app)
        self.vistaDip.show()

    def aggiungiFisioterapista(self):
        self.vistaCreaDipendente = NuovoDipendenteView('Fisioterapista',self.app)
        self.vistaCreaDipendente.show()

    def aggiungiMedico(self):
        self.vistaCreaDipendente = NuovoDipendenteView('Medico',self.app)
        self.vistaCreaDipendente.show()

    def aggiungiSegretario(self):
        self.vistaCreaDipendente = NuovoDipendenteView('Segretario',self.app)
        self.vistaCreaDipendente.show()

    def chiudiFinestra(self):
        self.close()

    def logout(self):
        sys.exit(self.app.exec_())
        #self.bLogout()
        #self.close()
