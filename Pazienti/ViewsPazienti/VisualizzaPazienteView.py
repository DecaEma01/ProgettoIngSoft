from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGroupBox, QFormLayout, QMessageBox
from Pazienti.ViewsPazienti.ModificaPazienteView import ModificaPazienteView
from Pazienti.ControllersPazienti.PazienteController import PazienteController

class VisualizzaPazienteView(QWidget):
    def __init__(self, paziente, callback):

        super(VisualizzaPazienteView,self).__init__()

        path = 'Pazienti/ViewsPazienti/UI/visualizzaPaziente.ui'
        uic.loadUi(path,self)

        
        self.aggiornaListaPaz = callback
        self.paziente = paziente
        self.attributiPaziente = PazienteController.visualizzaPazienteC(self.paziente)
        prescrizioni = self.attributiPaziente['prescrizioni']
        
        self.logout = self.findChild(QPushButton, "logoutButton")
        self.indietro = self.findChild(QPushButton, "indietroButton")
        self.elimina = self.findChild(QPushButton, "eliminaButton")
        self.modifica = self.findChild(QPushButton, "modificaButton")

        self.nome = self.findChild(QLabel, "nomeLabel")
        self.nome.setText(self.attributiPaziente['nome'])
        self.cognome = self.findChild(QLabel, "cognomeLabel")
        self.cognome.setText(self.attributiPaziente['cognome'])
        self.codice = self.findChild(QLabel, "codiceLabel")
        self.codice.setText(self.attributiPaziente['codicefiscale'])
        self.residenza = self.findChild(QLabel, "residenzaLabel")
        self.residenza.setText(self.attributiPaziente['indirizzoResidenza'])
        self.cellulare = self.findChild(QLabel, "cellulareLabel")
        self.cellulare.setText(self.attributiPaziente['telefono'])
        self.prLayout = self.findChild(QFormLayout, "prescrizioniLayout")
        self.prGroup = self.findChild(QGroupBox, "groupBox")

        try:
            for key in prescrizioni:
                self.prLayout.addRow(QLabel(f'{key} - {prescrizioni[key]}'))
        except:
            pass
            
        self.logout.clicked.connect(exit)

        self.indietro.clicked.connect(self.close)
        
        self.elimina.clicked.connect(self.exElimina)
        
        self.modifica.clicked.connect(self.exModifica)
        
    def exModifica(self):
        self.modificaPaziente = ModificaPazienteView(self.paziente, callback=self.aggiornaListaPaz)
        self.modificaPaziente.show()
        self.close()
        
    def exElimina(self):
        msg = QMessageBox()
        msg.setText("Confermare la scelta?")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        risp = msg.exec_()
        if risp == QMessageBox.Ok:
            PazienteController.eliminaPazienteC(PazienteController, self.paziente)
            self.aggiornaListaPaz()
            self.close()