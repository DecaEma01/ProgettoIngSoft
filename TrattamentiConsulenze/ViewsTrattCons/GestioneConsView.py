# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GestioneConsView.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from TrattamentiConsulenze.ControllersTrattCons.ConsulenzaController import ConsulenzaController
#from TrattamentiConsulenze.ViewsTrattCons.GestioneTrattConsView import GestioneTrattConsView


class GestioneConsView(object):
    def setupUi(self, Form , app):
        Form.setObjectName("Form")
        Form.resize(900, 700)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayoutPrincipale = QtWidgets.QVBoxLayout()
        self.verticalLayoutPrincipale.setObjectName("verticalLayoutPrincipale")
        self.horizontalLayoutIndietroLogout = QtWidgets.QHBoxLayout()
        self.horizontalLayoutIndietroLogout.setObjectName("horizontalLayoutIndietroLogout")

        self.pushButtonIndietro = QtWidgets.QPushButton(Form)
        self.pushButtonIndietro.clicked.connect(lambda: self.chiudiFinestra(Form))
        self.pushButtonIndietro.setObjectName("pushButtonIndietro")

        self.horizontalLayoutIndietroLogout.addWidget(self.pushButtonIndietro)

        self.pushButtonLogout = QtWidgets.QPushButton(Form)
        self.pushButtonLogout.setObjectName("pushButtonLogout")
        self.pushButtonLogout.clicked.connect(lambda: self.chiudiApp(app))

        self.horizontalLayoutIndietroLogout.addWidget(self.pushButtonLogout)
        self.verticalLayoutPrincipale.addLayout(self.horizontalLayoutIndietroLogout)
        self.labelDettagliConsulenza = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.labelDettagliConsulenza.setFont(font)
        self.labelDettagliConsulenza.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDettagliConsulenza.setObjectName("labelDettagliTrattamento")
        self.verticalLayoutPrincipale.addWidget(self.labelDettagliConsulenza)
        self.verticalLayoutDatiTrattamento = QtWidgets.QVBoxLayout()
        self.verticalLayoutDatiTrattamento.setObjectName("verticalLayoutDatiTrattamento")
        self.horizontalLayoutClasse = QtWidgets.QHBoxLayout()
        self.horizontalLayoutClasse.setObjectName("horizontalLayoutClasse")
        self.labelGiorno = QtWidgets.QLabel(Form)
        self.labelGiorno.setMaximumSize(QtCore.QSize(135, 16777215))
        self.labelGiorno.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelGiorno.setObjectName("labelGiorno")
        self.horizontalLayoutClasse.addWidget(self.labelGiorno)

        self.comboBoxGiorno = QtWidgets.QComboBox(Form)
        self.comboBoxGiorno.setObjectName("comboBoxGiorno")
        self.comboBoxGiorno.addItems(["lunedi","martedi","mercoledi","giovedi","venerdi","sabato"])
        self.comboBoxGiorno.setCurrentText(ConsulenzaController().getConsulenza().giornoSettimana)

        self.horizontalLayoutClasse.addWidget(self.comboBoxGiorno)
        self.verticalLayoutDatiTrattamento.addLayout(self.horizontalLayoutClasse)
        self.horizontalLayoutCosto = QtWidgets.QHBoxLayout()
        self.horizontalLayoutCosto.setObjectName("horizontalLayoutCosto")
        self.labelCosto = QtWidgets.QLabel(Form)
        self.labelCosto.setObjectName("labelCosto")
        self.horizontalLayoutCosto.addWidget(self.labelCosto)

        self.lineEditCosto = QtWidgets.QLineEdit(Form)
        self.lineEditCosto.setObjectName("lineEditCosto")
        self.lineEditCosto.setText(ConsulenzaController().getConsulenza().costo)

        self.horizontalLayoutCosto.addWidget(self.lineEditCosto)
        self.labelEuro = QtWidgets.QLabel(Form)
        self.labelEuro.setObjectName("labelEuro")
        self.horizontalLayoutCosto.addWidget(self.labelEuro)
        self.verticalLayoutDatiTrattamento.addLayout(self.horizontalLayoutCosto)
        self.horizontalLayoutDurata = QtWidgets.QHBoxLayout()
        self.horizontalLayoutDurata.setObjectName("horizontalLayoutDurata")
        self.labelDurata = QtWidgets.QLabel(Form)
        self.labelDurata.setObjectName("labelDurata")
        self.horizontalLayoutDurata.addWidget(self.labelDurata)

        self.lineEditDurata = QtWidgets.QLineEdit(Form)
        self.lineEditDurata.setObjectName("lineEditDurata")
        self.lineEditDurata.setText(ConsulenzaController().getConsulenza().durata)

        self.horizontalLayoutDurata.addWidget(self.lineEditDurata)
        self.labelMinuti = QtWidgets.QLabel(Form)
        self.labelMinuti.setObjectName("labelMinuti")
        self.horizontalLayoutDurata.addWidget(self.labelMinuti)
        self.verticalLayoutDatiTrattamento.addLayout(self.horizontalLayoutDurata)
        self.verticalLayoutPrincipale.addLayout(self.verticalLayoutDatiTrattamento)
        spacerItem = QtWidgets.QSpacerItem(40, 380, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayoutPrincipale.addItem(spacerItem)

        self.pushButtonSalva = QtWidgets.QPushButton(Form)
        self.pushButtonSalva.setObjectName("pushButtonSalva")

        #salva i nuovi dati relativi alla consulenza e chiude la finestra
        self.pushButtonSalva.clicked.connect(lambda: self.inoltroFormConsulenza(Form))


        self.verticalLayoutPrincipale.addWidget(self.pushButtonSalva)
        self.verticalLayout.addLayout(self.verticalLayoutPrincipale)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Amministratore - gestisci consulenza medica"))
        self.pushButtonIndietro.setText(_translate("Form", "INDIETRO"))
        self.pushButtonLogout.setText(_translate("Form", "LOGOUT"))
        self.labelDettagliConsulenza.setText(_translate("Form", "Dettagli consulenza medica:"))
        self.labelGiorno.setText(_translate("Form", "Giorno della settimana:"))
        self.labelCosto.setText(_translate("Form", "Costo:"))
        self.labelEuro.setText(_translate("Form", "€"))
        self.labelDurata.setText(_translate("Form", "Durata:"))
        self.labelMinuti.setText(_translate("Form", "minuti"))
        self.pushButtonSalva.setText(_translate("Form", "Salva"))


    def inoltroFormConsulenza(self,Form):
        if ConsulenzaController().modificaConsulenza(str(self.comboBoxGiorno.currentText()),str(self.lineEditCosto.text()).strip(),str(self.lineEditDurata.text()).strip()):
            self.chiudiFinestra(Form) #chiudendosi la finestra viene mostrata nuovamente la finestra di gestione dei trattamenti che stava sotto
        else:
            errore = QMessageBox()
            errore.setWindowTitle("Errore di inserimento")
            errore.setText("Controlla che siano stati compilati tutti i campi e che nei campi 'costo' o 'durata' siano stati inseriti dei valori numerici.")
            errore.setIcon(QMessageBox.Warning)
            errore.setStandardButtons(QMessageBox.Ok)
            errore.exec_()


    def chiudiFinestra(self,Form):
        Form.close()

    def chiudiApp(self,app):
        sys.exit(app.exec_())





"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = GestioneConsView()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
"""