# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ModificaPrenotazioneView.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(974, 720)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayoutPrincipale = QtWidgets.QVBoxLayout()
        self.verticalLayoutPrincipale.setObjectName("verticalLayoutPrincipale")
        self.horizontalLayoutIndietroLogout = QtWidgets.QHBoxLayout()
        self.horizontalLayoutIndietroLogout.setObjectName("horizontalLayoutIndietroLogout")
        self.pushButtonIndietro = QtWidgets.QPushButton(Form)
        self.pushButtonIndietro.setObjectName("pushButtonIndietro")
        self.horizontalLayoutIndietroLogout.addWidget(self.pushButtonIndietro)
        self.pushButtonLogout = QtWidgets.QPushButton(Form)
        self.pushButtonLogout.setObjectName("pushButtonLogout")
        self.horizontalLayoutIndietroLogout.addWidget(self.pushButtonLogout)
        self.verticalLayoutPrincipale.addLayout(self.horizontalLayoutIndietroLogout)
        self.labelDettagliTrattamento = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.labelDettagliTrattamento.setFont(font)
        self.labelDettagliTrattamento.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDettagliTrattamento.setObjectName("labelDettagliTrattamento")
        self.verticalLayoutPrincipale.addWidget(self.labelDettagliTrattamento)
        self.verticalLayoutDatiTrattamento = QtWidgets.QVBoxLayout()
        self.verticalLayoutDatiTrattamento.setObjectName("verticalLayoutDatiTrattamento")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.labelTipologia = QtWidgets.QLabel(Form)
        self.labelTipologia.setMaximumSize(QtCore.QSize(135, 16777215))
        self.labelTipologia.setObjectName("labelTipologia")
        self.horizontalLayout_4.addWidget(self.labelTipologia)
        self.lineEditTipologia = QtWidgets.QLineEdit(Form)
        self.lineEditTipologia.setObjectName("lineEditTipologia")
        self.horizontalLayout_4.addWidget(self.lineEditTipologia)
        self.verticalLayoutDatiTrattamento.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.labelTrattamento = QtWidgets.QLabel(Form)
        self.labelTrattamento.setMaximumSize(QtCore.QSize(80, 16777215))
        self.labelTrattamento.setObjectName("labelTrattamento")
        self.horizontalLayout_8.addWidget(self.labelTrattamento)
        self.lineEditTrattamento = QtWidgets.QLineEdit(Form)
        self.lineEditTrattamento.setObjectName("lineEditTrattamento")
        self.horizontalLayout_8.addWidget(self.lineEditTrattamento)
        self.verticalLayoutDatiTrattamento.addLayout(self.horizontalLayout_8)
        self.horizontalLayoutNome = QtWidgets.QHBoxLayout()
        self.horizontalLayoutNome.setObjectName("horizontalLayoutNome")
        self.labelNome = QtWidgets.QLabel(Form)
        self.labelNome.setMaximumSize(QtCore.QSize(45, 16777215))
        self.labelNome.setObjectName("labelNome")
        self.horizontalLayoutNome.addWidget(self.labelNome)
        self.lineEditNome = QtWidgets.QLineEdit(Form)
        self.lineEditNome.setObjectName("lineEditNome")
        self.horizontalLayoutNome.addWidget(self.lineEditNome)
        self.verticalLayoutDatiTrattamento.addLayout(self.horizontalLayoutNome)
        self.horizontalLayoutClasse = QtWidgets.QHBoxLayout()
        self.horizontalLayoutClasse.setObjectName("horizontalLayoutClasse")
        self.labelCognome = QtWidgets.QLabel(Form)
        self.labelCognome.setMaximumSize(QtCore.QSize(65, 16777215))
        self.labelCognome.setObjectName("labelCognome")
        self.horizontalLayoutClasse.addWidget(self.labelCognome)
        self.lineEditCognome = QtWidgets.QLineEdit(Form)
        self.lineEditCognome.setObjectName("lineEditCognome")
        self.horizontalLayoutClasse.addWidget(self.lineEditCognome)
        self.verticalLayoutDatiTrattamento.addLayout(self.horizontalLayoutClasse)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelData = QtWidgets.QLabel(Form)
        self.labelData.setMaximumSize(QtCore.QSize(110, 16777215))
        self.labelData.setObjectName("labelData")
        self.horizontalLayout_2.addWidget(self.labelData)
        self.lineEditData = QtWidgets.QLineEdit(Form)
        self.lineEditData.setObjectName("lineEditData")
        self.horizontalLayout_2.addWidget(self.lineEditData)
        self.verticalLayoutDatiTrattamento.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelOrario = QtWidgets.QLabel(Form)
        self.labelOrario.setMaximumSize(QtCore.QSize(45, 16777215))
        self.labelOrario.setObjectName("labelOrario")
        self.horizontalLayout_3.addWidget(self.labelOrario)
        self.lineEditOrario = QtWidgets.QLineEdit(Form)
        self.lineEditOrario.setObjectName("lineEditOrario")
        self.horizontalLayout_3.addWidget(self.lineEditOrario)
        self.verticalLayoutDatiTrattamento.addLayout(self.horizontalLayout_3)
        self.horizontalLayoutCosto = QtWidgets.QHBoxLayout()
        self.horizontalLayoutCosto.setObjectName("horizontalLayoutCosto")
        self.labelCosto = QtWidgets.QLabel(Form)
        self.labelCosto.setMaximumSize(QtCore.QSize(45, 16777215))
        self.labelCosto.setObjectName("labelCosto")
        self.horizontalLayoutCosto.addWidget(self.labelCosto)
        self.lineEditCosto = QtWidgets.QLineEdit(Form)
        self.lineEditCosto.setObjectName("lineEditCosto")
        self.horizontalLayoutCosto.addWidget(self.lineEditCosto)
        self.labelEuro = QtWidgets.QLabel(Form)
        self.labelEuro.setObjectName("labelEuro")
        self.horizontalLayoutCosto.addWidget(self.labelEuro)
        self.verticalLayoutDatiTrattamento.addLayout(self.horizontalLayoutCosto)
        self.horizontalLayoutDurata = QtWidgets.QHBoxLayout()
        self.horizontalLayoutDurata.setObjectName("horizontalLayoutDurata")
        self.labelDurata = QtWidgets.QLabel(Form)
        self.labelDurata.setMaximumSize(QtCore.QSize(50, 16777215))
        self.labelDurata.setObjectName("labelDurata")
        self.horizontalLayoutDurata.addWidget(self.labelDurata)
        self.lineEditDurata = QtWidgets.QLineEdit(Form)
        self.lineEditDurata.setObjectName("lineEditDurata")
        self.horizontalLayoutDurata.addWidget(self.lineEditDurata)
        self.labelMinuti = QtWidgets.QLabel(Form)
        self.labelMinuti.setObjectName("labelMinuti")
        self.horizontalLayoutDurata.addWidget(self.labelMinuti)
        self.verticalLayoutDatiTrattamento.addLayout(self.horizontalLayoutDurata)
        self.verticalLayoutPrincipale.addLayout(self.verticalLayoutDatiTrattamento)
        self.radioButtonSedutaEffettuata = QtWidgets.QRadioButton(Form)
        self.radioButtonSedutaEffettuata.setObjectName("radioButtonSedutaEffettuata")
        self.verticalLayoutPrincipale.addWidget(self.radioButtonSedutaEffettuata)
        self.horizontalLayoutEliminaModificaTra = QtWidgets.QHBoxLayout()
        self.horizontalLayoutEliminaModificaTra.setObjectName("horizontalLayoutEliminaModificaTra")

        spacerItem = QtWidgets.QSpacerItem(40, 100, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayoutPrincipale.addItem(spacerItem)

        self.pushButtonModificaSalva = QtWidgets.QPushButton(Form)
        self.pushButtonModificaSalva.setObjectName("pushButtonModificaSalva")
        self.horizontalLayoutEliminaModificaTra.addWidget(self.pushButtonModificaSalva)
        self.verticalLayoutPrincipale.addLayout(self.horizontalLayoutEliminaModificaTra)
        self.verticalLayout.addLayout(self.verticalLayoutPrincipale)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Segretario - Modifica Prenotazione"))
        self.pushButtonIndietro.setText(_translate("Form", "INDIETRO"))
        self.pushButtonLogout.setText(_translate("Form", "LOGOUT"))
        self.labelDettagliTrattamento.setText(_translate("Form", "Dettagli prenotazione:"))
        self.labelTipologia.setText(_translate("Form", "Tipologia della seduta:"))
        self.labelTrattamento.setText(_translate("Form", "Trattamento:"))
        self.labelNome.setText(_translate("Form", "Nome:"))
        self.labelCognome.setText(_translate("Form", "Cognome:"))
        self.labelData.setText(_translate("Form", "Data della seduta:"))
        self.labelOrario.setText(_translate("Form", "Orario:"))
        self.labelCosto.setText(_translate("Form", "Costo:"))
        self.labelEuro.setText(_translate("Form", "€"))
        self.labelDurata.setText(_translate("Form", "Durata:"))
        self.labelMinuti.setText(_translate("Form", "minuti"))
        self.radioButtonSedutaEffettuata.setText(_translate("Form", "Seduta effettuata"))
        self.pushButtonModificaSalva.setText(_translate("Form", "Salva"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
