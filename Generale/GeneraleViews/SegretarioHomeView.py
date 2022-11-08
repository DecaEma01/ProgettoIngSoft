from PyQt5.QtWidgets import QWidget, QPushButton, QSizePolicy, QHBoxLayout, QVBoxLayout, QLineEdit, QLabel, QSpacerItem


class SegretarioHomeView(QWidget):

    def __init__(self, parent = None):
        super(SegretarioHomeView, self).__init__(parent)        # richiamiamo il costruttore di qWidget e li passiamo il parent none

        self.parametriAutentificazione = {}

        layoutVertMain = QVBoxLayout()

        layoutBottoneLogOut = QHBoxLayout()
        layoutVertMain.addWidget(self.generaBottone('Logout', self.chiudiFinestra, False))
        layoutVertMain.addLayout(layoutBottoneLogOut)

        layoutVertMain.addWidget(self.generaBottone('Gestione Prenotazioni', self.gestionePrenotazioni))
        layoutVertMain.addWidget(self.generaBottone('Gestione Clienti', self.amministrazioneClienti))

        self.setLayout(layoutVertMain)
        self.resize(900, 700)
        self.setWindowTitle('Amministratore - Gestione dipendenti')

    def generaBottone(self, titolo, onClick, expanding = True, width = None):
        button = QPushButton(titolo)
        if expanding:
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        if width:
            button.setFixedWidth(width)
        button.clicked.connect(onClick)
        return button

    def chiudiFinestra(self):
        self.close()

    def gestionePrenotazioni(self):
        return

    def amministrazioneClienti(self):
        return