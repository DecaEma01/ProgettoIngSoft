from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import os


from Pazienti.ViewsPazienti.GestionePazientiView import GestionePazientiView
from TrattamentiConsulenze.ViewsTrattCons.AggiungiTrattView import AggiungiTrattView
from TrattamentiConsulenze.ViewsTrattCons.GestioneConsView import GestioneConsView
from TrattamentiConsulenze.ControllersTrattCons.ConsulenzaController import ConsulenzaController
from TrattamentiConsulenze.ViewsTrattCons.GestioneTrattConsView import GestioneTrattConsView
from Pazienti.ViewsPazienti.GestionePazientiView import GestionePazientiView


# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from Pazienti.ModelsPazienti.PazienteModel import PazienteModel
from Pazienti.ModelsPazienti.ElencoPazientiModel import ElencoPazientiModel

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

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

