# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GestioneTrattConsView.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GestioneTrattConsView(object):
    def setupUi(self, GestioneTrattConsView):
        GestioneTrattConsView.setObjectName("GestioneTrattConsView")
        GestioneTrattConsView.resize(900, 700)
        self.verticalLayout = QtWidgets.QVBoxLayout(GestioneTrattConsView)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayoutPrincipale = QtWidgets.QVBoxLayout()
        self.verticalLayoutPrincipale.setObjectName("verticalLayoutPrincipale")
        self.horizontalLayoutIndietroLogout = QtWidgets.QHBoxLayout()
        self.horizontalLayoutIndietroLogout.setObjectName("horizontalLayoutIndietroLogout")
        self.pushButtonIndietro = QtWidgets.QPushButton(GestioneTrattConsView)
        self.pushButtonIndietro.setObjectName("pushButtonIndietro")
        self.horizontalLayoutIndietroLogout.addWidget(self.pushButtonIndietro)
        self.pushButtonLogout = QtWidgets.QPushButton(GestioneTrattConsView)
        self.pushButtonLogout.setObjectName("pushButtonLogout")
        self.horizontalLayoutIndietroLogout.addWidget(self.pushButtonLogout)
        self.verticalLayoutPrincipale.addLayout(self.horizontalLayoutIndietroLogout)
        self.gridLayoutRicerca = QtWidgets.QGridLayout()
        self.gridLayoutRicerca.setObjectName("gridLayoutRicerca")
        self.labelRicercaTraNome = QtWidgets.QLabel(GestioneTrattConsView)
        self.labelRicercaTraNome.setObjectName("labelRicercaTraNome")
        self.gridLayoutRicerca.addWidget(self.labelRicercaTraNome, 2, 0, 1, 1)
        self.comboBoxClasseTra = QtWidgets.QComboBox(GestioneTrattConsView)
        self.comboBoxClasseTra.setObjectName("comboBoxClasseTra")
        self.gridLayoutRicerca.addWidget(self.comboBoxClasseTra, 1, 1, 1, 1)
        self.labelRicercaTraClasse = QtWidgets.QLabel(GestioneTrattConsView)
        self.labelRicercaTraClasse.setObjectName("labelRicercaTraClasse")
        self.gridLayoutRicerca.addWidget(self.labelRicercaTraClasse, 1, 0, 1, 1)
        self.lineEditNomeTra = QtWidgets.QLineEdit(GestioneTrattConsView)
        self.lineEditNomeTra.setObjectName("lineEditNomeTra")
        self.gridLayoutRicerca.addWidget(self.lineEditNomeTra, 2, 1, 1, 1)
        self.pushButtonRicerca = QtWidgets.QPushButton(GestioneTrattConsView)
        self.pushButtonRicerca.setObjectName("pushButtonRicerca")
        self.gridLayoutRicerca.addWidget(self.pushButtonRicerca, 9, 0, 1, 2)
        self.verticalLayoutPrincipale.addLayout(self.gridLayoutRicerca)
        self.listViewTrattamenti = QtWidgets.QListView(GestioneTrattConsView)
        self.listViewTrattamenti.setObjectName("listViewTrattamenti")
        self.verticalLayoutPrincipale.addWidget(self.listViewTrattamenti)
        self.verticalLayoutNuovoTraGestisciCons = QtWidgets.QVBoxLayout()
        self.verticalLayoutNuovoTraGestisciCons.setObjectName("verticalLayoutNuovoTraGestisciCons")
        self.pushButtonNuovoTra = QtWidgets.QPushButton(GestioneTrattConsView)
        self.pushButtonNuovoTra.setObjectName("pushButtonNuovoTra")
        self.verticalLayoutNuovoTraGestisciCons.addWidget(self.pushButtonNuovoTra)
        self.pushButtonGestisciCons = QtWidgets.QPushButton(GestioneTrattConsView)
        self.pushButtonGestisciCons.setObjectName("pushButtonGestisciCons")
        self.verticalLayoutNuovoTraGestisciCons.addWidget(self.pushButtonGestisciCons)
        self.verticalLayoutPrincipale.addLayout(self.verticalLayoutNuovoTraGestisciCons)
        self.verticalLayout.addLayout(self.verticalLayoutPrincipale)

        self.retranslateUi(GestioneTrattConsView)
        QtCore.QMetaObject.connectSlotsByName(GestioneTrattConsView)

    def retranslateUi(self, GestioneTrattConsView):
        _translate = QtCore.QCoreApplication.translate
        GestioneTrattConsView.setWindowTitle(_translate("GestioneTrattConsView", "Amministratore"))
        self.pushButtonIndietro.setText(_translate("GestioneTrattConsView", "INDIETRO"))
        self.pushButtonLogout.setText(_translate("GestioneTrattConsView", "LOGOUT"))
        self.labelRicercaTraNome.setText(_translate("GestioneTrattConsView", "Ricerca per nome trattamento: "))
        self.labelRicercaTraClasse.setText(_translate("GestioneTrattConsView", "Ricerca per classe trattamento:"))
        self.pushButtonRicerca.setText(_translate("GestioneTrattConsView", "Ricerca"))
        self.pushButtonNuovoTra.setText(_translate("GestioneTrattConsView", "Nuovo Trattamento Fisioterapico"))
        self.pushButtonGestisciCons.setText(_translate("GestioneTrattConsView", "Gestisci Consulenza medica"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GestioneTrattConsView = QtWidgets.QWidget()
    ui = Ui_GestioneTrattConsView()
    ui.setupUi(GestioneTrattConsView)
    GestioneTrattConsView.show()
    sys.exit(app.exec_())
