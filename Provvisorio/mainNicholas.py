from Pazienti.ModelsPazienti.PazienteModel import PazienteModel
from Pazienti.ModelsPazienti.ElencoPazientiModel import ElencoPazientiModel

import os, sys
from PyQt5.QtWidgets import QApplication

from Pazienti.ViewsPazienti.GestionePazientiView import GestionePazientiView

if __name__ == '__main__':

    if os.path.isfile('Dati/Pazienti.pickle') == False:
        paz = PazienteModel('Nicholas','Bradach','BRDNHL','345','SN','26','MSV','Ancona', {})
    pazienti = ElencoPazientiModel.visualizzaElencoPazientiM(PazienteModel)
    
    app = QApplication(sys.argv)
    view = GestionePazientiView()
    view.show()
    sys.exit(app.exec())