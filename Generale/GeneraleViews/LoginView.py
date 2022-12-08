from PyQt5 import QtCore

from Generale.GeneraleViews.SegretarioHomeView import SegretarioHomeView
from Generale.GeneraleViews.AmministratoreHomeView import AmministratoreHomeView
from Generale.GeneraleControllers.LoginController import LoginController

from PyQt5.QtWidgets import QWidget, QPushButton, QSizePolicy, QHBoxLayout, QVBoxLayout, QLineEdit, QLabel, QSpacerItem, QMessageBox


class LoginView(QWidget):

    def __init__(self, parent = None):
        super(LoginView, self).__init__(parent)        # richiamiamo il costruttore di qWidget e li passiamo il parent none
        self.resize(900, 700)

        self.parametriAutentificazione = {}

        layoutVertMain = QVBoxLayout()

        intestazione=QLabel("\n \n Benvenuto \n \n  Effettua il login")
        intestazione.setAlignment(QtCore.Qt.AlignCenter)
        fontNome = intestazione.font()
        fontNome.setPointSize(20)
        intestazione.setFont(fontNome)

        layoutVertMain.addWidget(intestazione)
        layoutVertMain.addItem(QSpacerItem(100, 75))


        layoutVertMain.addLayout(self.generaLinea("Username:", "login"))
        layoutVertMain.addLayout(self.generaLinea("Password:", "password", True))



        layoutBottoniSwitch = QHBoxLayout()
        layoutBottoniSwitch.addWidget(self.generaBottone('Entra', self.accesso, False, 400))
        layoutBottoniSwitch.addWidget(self.generaBottone('Esci', self.chiudiFinestra, False, 400))
        layoutVertMain.addLayout(layoutBottoniSwitch)
        layoutVertMain.addItem(QSpacerItem(100, 75))

        self.setLayout(layoutVertMain)
        self.setWindowTitle('Login')

    def generaBottone(self, titolo, onClick, expanding = True, width = None):
        button = QPushButton(titolo)
        if expanding:
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        if width:
            button.setFixedWidth(width)
        button.clicked.connect(onClick)
        return button

    def generaLinea(self, nomeLabel, label, echoMode = False):  # da aggiungere la var placeholder
        layoutOriz = QHBoxLayout()
        layoutOriz.addItem(QSpacerItem(75, 50))
        nLabel = QLabel(nomeLabel)
        nLabel.setFixedWidth(100)
        layoutOriz.addWidget(nLabel)
        testo = QLineEdit()
        if echoMode:
            testo.setEchoMode(QLineEdit.Password)
        layoutOriz.addWidget(testo)
        layoutOriz.addItem(QSpacerItem(75, 50))
        self.parametriAutentificazione[label] = testo

        return layoutOriz

    def verificaCredenziali(self):
        utente = LoginController.verificaCredenziali(LoginController, self.parametriAutentificazione['login'].text(), self.parametriAutentificazione['password'].text())

        try:
            if not utente :
                raise Exception()
        except:
            QMessageBox.critical(self, 'Errore', 'I campi Username e Password sono incompleti o errati', QMessageBox.Ok)
            return

        return utente

    def accesso(self):
        utente = self.verificaCredenziali()

        if utente == None:
            return

        self.parametriAutentificazione['login'].setText('')
        self.parametriAutentificazione['password'].setText('')

        if utente['ruolo'] == 'Amministratore':
            self.vistaAmministratore = AmministratoreHomeView()
            self.vistaAmministratore.show()

        elif utente['ruolo'] == 'Segretario':
            self.vistaSegretario = SegretarioHomeView()
            self.vistaSegretario.show()


    def chiudiFinestra(self):
        self.close()
