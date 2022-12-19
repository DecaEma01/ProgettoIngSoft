from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import os
from datetime import datetime
import threading


# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Dipendenti.ModelsDipendenti.SegretarioModel import SegretarioModel
from Generale.GeneraleViews.LoginView import LoginView
from Pazienti.ViewsPazienti.GestionePazientiView import GestionePazientiView
from Prenotazioni.ViewsPrenotazioni.GestionePrenotazioniView import GestionePrenotazioniView
from TrattamentiConsulenze.ViewsTrattCons.AggiungiTrattView import AggiungiTrattView
from TrattamentiConsulenze.ViewsTrattCons.GestioneConsView import GestioneConsView
from TrattamentiConsulenze.ControllersTrattCons.ConsulenzaController import ConsulenzaController
from TrattamentiConsulenze.ViewsTrattCons.GestioneTrattConsView import GestioneTrattConsView
from Pazienti.ViewsPazienti.GestionePazientiView import GestionePazientiView


from Pazienti.ModelsPazienti.PazienteModel import PazienteModel
from Pazienti.ModelsPazienti.ElencoPazientiModel import ElencoPazientiModel
from Generale.Backup.BackupModel import BackupModel

from datetime import time

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def backup():
    while (datetime.now().strftime("%H:%M:%S")=='21:59:59' or datetime.now().strftime("%H:%M:%S")=='22:00:00'):
        BackupModel.eseguiBackup(BackupModel)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    #x = threading.Thread(target=backup)
    #x.start()

    if os.path.isfile('Dati/Dipendenti.pickle') == False:
        dipendente1 = SegretarioModel('Giuseppe', 'Falcone', 'HGGIUH', '3285610013', 'spalato', '12', 'Pescara',
                                      'Abruzzo')

    app = QApplication(sys.argv)
    vistaLogin = LoginView(app)
    vistaLogin.show()
    sys.exit(app.exec())





"""
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = GestionePrenotazioniView()
    ui.setupUi(Form, app)
    Form.show()
    sys.exit(app.exec_())
"""

"""
    if os.path.isfile('Dati/Pazienti.pickle') == False:
        paz = PazienteModel('Nicholas', 'Bradach', 'BRDNHL', '345', 'SN', '26', 'MSV', 'Ancona', {})
    pazienti = ElencoPazientiModel.visualizzaElencoPazientiM(PazienteModel)

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = GestionePazientiView()
    ui.setupUi(Form, app)
    Form.show()
    sys.exit(app.exec_())
"""

"""
if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = GestionePazientiView()
    view.show()
    sys.exit(app.exec())
"""
"""
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = GestioneTrattConsView()
    ui.setupUi(Form,app)
    Form.show()
    sys.exit(app.exec_())
"""

"""
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = AggiungiTrattView()
    ui.setupUi(Form,app)
    Form.show()
    sys.exit(app.exec_())
"""

""" 
test gestisci consulenza

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = GestioneConsView()
    ui.setupUi(Form,app)
    Form.show()
    sys.exit(app.exec_())
"""




# See PyCharm help at https://www.jetbrains.com/help/pycharm/

