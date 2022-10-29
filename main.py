from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

from TrattamentiConsulenze.ViewsTrattCons.AggiungiTrattView import AggiungiTrattView
from TrattamentiConsulenze.ViewsTrattCons.GestioneConsView import GestioneConsView
from TrattamentiConsulenze.ControllersTrattCons.ConsulenzaController import ConsulenzaController
from TrattamentiConsulenze.ViewsTrattCons.GestioneTrattConsView import GestioneTrattConsView

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = GestioneTrattConsView()
    ui.setupUi(Form,app)
    Form.show()
    sys.exit(app.exec_())

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

