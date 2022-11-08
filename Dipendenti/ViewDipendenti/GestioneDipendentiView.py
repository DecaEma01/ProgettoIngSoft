from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QHBoxLayout,  QVBoxLayout
from Amministratore.Dipendenti.ViewDipendenti.DipendentiRegistratiView import DipendentiRegistratiView
from Amministratore.Dipendenti.ViewDipendenti.NuovoDipendenteView import NuovoDipendenteView

class GestioneDipendentiView(QWidget):

    def __init__(self, bLogout, parent = None):
        super(GestioneDipendentiView, self).__init__(parent)        # richiamiamo il costruttore di qWidget e li passiamo il parent none

        self.bLogout = bLogout

        self.resize(900, 700)

        layoutVertMain = QVBoxLayout()
        layoutBottoniSwitch = QHBoxLayout()
        layoutBottoniSwitch.addWidget(self.generaBottone('Indietro', self.chiudiFinestra, False))
        layoutBottoniSwitch.addWidget(self.generaBottone('Logout', self.logout, False))
        layoutVertMain.addLayout(layoutBottoniSwitch)

        gridLayot = QGridLayout()
        gridLayot.addWidget(self.generaBottone('Dipendenti Registrati', self.eseguiDipendentiRegistrati), 0, 0, 1, 3)
        gridLayot.addWidget(self.generaBottone('Nuovo Fisioterapista ', self.aggiungiFisioterapista), 1, 0)
        gridLayot.addWidget(self.generaBottone('Nuovo Medico', self.aggiungiMedico), 1, 1)
        gridLayot.addWidget(self.generaBottone('Nuovo Segretario', self.aggiungiSegretario), 1, 2)
        #gridLayot.addWidget(self.generaBottone('Gestione Trattamenti', self.eseguiGestioneTrattamenti), 2, 0, 1, 3)

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
        self.vistaDip = DipendentiRegistratiView(self.logout)
        self.vistaDip.show()

    def aggiungiFisioterapista(self):
        self.vistaCreaDipendente = NuovoDipendenteView('Fisioterapista')
        self.vistaCreaDipendente.show()

    def aggiungiMedico(self):
        self.vistaCreaDipendente = NuovoDipendenteView('Medico')
        self.vistaCreaDipendente.show()

    def aggiungiSegretario(self):
        self.vistaCreaDipendente = NuovoDipendenteView('Segretario')
        self.vistaCreaDipendente.show()

    def chiudiFinestra(self):
        self.close()

    def logout(self):
        self.bLogout()
        self.close()
        pass#semplice chiusura della finestra da passare come attributo al costruttore di VistaDipendenti registrati