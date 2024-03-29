# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VisualizzaPrenotazioneView.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Prenotazioni.ControllersPrenotazioni.PrenotazioneController import PrenotazioneController
from Prenotazioni.ViewsPrenotazioni.ModificaPrenotazioneView import ModificaPrenotazioneView
from TrattamentiConsulenze.ControllersTrattCons.ConsulenzaController import ConsulenzaController


class VisualizzaPrenotazioneView(object):
    def __init__(self , prenotazione, aggiornaListaPrenotazioni):
        self.prenotazione = prenotazione
        self.aggiornaListaPrenotazioni = aggiornaListaPrenotazioni

    def setupUi(self, Form, app):
        Form.setObjectName("Form")
        Form.resize(900, 700)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayoutPrincipale = QtWidgets.QVBoxLayout()
        self.verticalLayoutPrincipale.setObjectName("verticalLayoutPrincipale")
        self.horizontalLayoutIndietroLogout = QtWidgets.QHBoxLayout()
        self.horizontalLayoutIndietroLogout.setObjectName("horizontalLayoutIndietroLogout")
        self.pushButtonIndietro = QtWidgets.QPushButton(Form)
        self.pushButtonIndietro.setObjectName("pushButtonIndietro")
        self.pushButtonIndietro.clicked.connect(lambda: self.chiudiFinestra(Form))

        self.horizontalLayoutIndietroLogout.addWidget(self.pushButtonIndietro)
        self.pushButtonLogout = QtWidgets.QPushButton(Form)
        self.pushButtonLogout.setObjectName("pushButtonLogout")
        self.pushButtonLogout.clicked.connect(lambda: self.chiudiApp(app))

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
        self.labelTipologiaValue = QtWidgets.QLabel(Form)
        self.labelTipologiaValue.setText(str(self.prenotazione.tipologia))
        self.labelTipologiaValue.setObjectName("labelTipologiaValue")
        self.horizontalLayout_4.addWidget(self.labelTipologiaValue)
        self.verticalLayoutDatiTrattamento.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")

        if self.prenotazione.trattamento:
            self.labelTrattamento = QtWidgets.QLabel(Form)
            self.labelTrattamento.setMaximumSize(QtCore.QSize(80, 16777215))
            self.labelTrattamento.setObjectName("labelTrattamento")
            self.horizontalLayout_8.addWidget(self.labelTrattamento)
            self.labelTrattamentoValue = QtWidgets.QLabel(Form)
            self.labelTrattamentoValue.setText(str(self.prenotazione.trattamento.nome)+" - "+str(self.prenotazione.trattamento.classe))
            self.labelTrattamentoValue.setObjectName("labelTrattamentoValue")
            self.horizontalLayout_8.addWidget(self.labelTrattamentoValue)
            self.verticalLayoutDatiTrattamento.addLayout(self.horizontalLayout_8)



        self.horizontalLayoutNome = QtWidgets.QHBoxLayout()
        self.horizontalLayoutNome.setObjectName("horizontalLayoutNome")
        self.labelNome = QtWidgets.QLabel(Form)
        self.labelNome.setMaximumSize(QtCore.QSize(45, 16777215))
        self.labelNome.setObjectName("labelNome")
        self.horizontalLayoutNome.addWidget(self.labelNome)
        self.labelNomeValue = QtWidgets.QLabel(Form)
        self.labelNomeValue.setText(str(self.prenotazione.paziente.nome))
        self.labelNomeValue.setObjectName("labelNomeValue")
        self.horizontalLayoutNome.addWidget(self.labelNomeValue)
        self.verticalLayoutDatiTrattamento.addLayout(self.horizontalLayoutNome)
        self.horizontalLayoutClasse = QtWidgets.QHBoxLayout()
        self.horizontalLayoutClasse.setObjectName("horizontalLayoutClasse")
        self.labelCognome = QtWidgets.QLabel(Form)
        self.labelCognome.setMaximumSize(QtCore.QSize(65, 16777215))
        self.labelCognome.setObjectName("labelCognome")
        self.horizontalLayoutClasse.addWidget(self.labelCognome)
        self.labelCognomeValue = QtWidgets.QLabel(Form)
        self.labelCognomeValue.setText(str(self.prenotazione.paziente.cognome))
        self.labelCognomeValue.setObjectName("labelCognomeValue")
        self.horizontalLayoutClasse.addWidget(self.labelCognomeValue)
        self.verticalLayoutDatiTrattamento.addLayout(self.horizontalLayoutClasse)

        self.horizontalLayoutCodiceFiscale = QtWidgets.QHBoxLayout()
        self.horizontalLayoutCodiceFiscale.setObjectName("horizontalLayoutCodiceFiscale")
        self.labelCodiceFiscale = QtWidgets.QLabel(Form)
        self.labelCodiceFiscale.setMaximumSize(QtCore.QSize(85, 16777215))
        self.labelCodiceFiscale.setObjectName("labelCodiceFiscale")
        self.horizontalLayoutCodiceFiscale.addWidget(self.labelCodiceFiscale)
        self.labelCodiceFiscaleValue = QtWidgets.QLabel(Form)
        self.labelCodiceFiscaleValue.setText(str(self.prenotazione.paziente.codicefiscale))
        self.labelCodiceFiscaleValue.setObjectName("labelCodiceFiscaleValue")
        self.horizontalLayoutCodiceFiscale.addWidget(self.labelCodiceFiscaleValue)
        self.verticalLayoutDatiTrattamento.addLayout(self.horizontalLayoutCodiceFiscale)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelData = QtWidgets.QLabel(Form)
        self.labelData.setMaximumSize(QtCore.QSize(110, 16777215))
        self.labelData.setObjectName("labelData")
        self.horizontalLayout_2.addWidget(self.labelData)
        self.labelDataValue = QtWidgets.QLabel(Form)
        self.labelDataValue.setText(str(self.prenotazione.data.toString('dd/MM/yyyy')))
        self.labelDataValue.setObjectName("labelDataValue")
        self.horizontalLayout_2.addWidget(self.labelDataValue)
        self.verticalLayoutDatiTrattamento.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelOrario = QtWidgets.QLabel(Form)
        self.labelOrario.setMaximumSize(QtCore.QSize(45, 16777215))
        self.labelOrario.setObjectName("labelOrario")
        self.horizontalLayout_3.addWidget(self.labelOrario)
        self.labelOrarioValue = QtWidgets.QLabel(Form)
        self.labelOrarioValue.setText(str(self.prenotazione.ora))
        self.labelOrarioValue.setObjectName("labelOrarioValue")
        self.horizontalLayout_3.addWidget(self.labelOrarioValue)
        self.verticalLayoutDatiTrattamento.addLayout(self.horizontalLayout_3)
        self.horizontalLayoutCosto = QtWidgets.QHBoxLayout()
        self.horizontalLayoutCosto.setObjectName("horizontalLayoutCosto")
        self.labelCosto = QtWidgets.QLabel(Form)
        self.labelCosto.setMaximumSize(QtCore.QSize(45, 16777215))
        self.labelCosto.setObjectName("labelCosto")
        self.horizontalLayoutCosto.addWidget(self.labelCosto)
        self.labelCostoValue = QtWidgets.QLabel(Form)
        self.labelCostoValue.setMaximumSize(QtCore.QSize(40, 16777215))
        self.labelCostoValue.setText("")
        self.labelCostoValue.setObjectName("labelCostoValue")
        self.horizontalLayoutCosto.addWidget(self.labelCostoValue)
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
        self.labelDurataValue = QtWidgets.QLabel(Form)
        self.labelDurataValue.setMaximumSize(QtCore.QSize(40, 16777215))
        self.labelDurataValue.setText("")
        self.labelDurataValue.setObjectName("labelDurataValue")
        self.horizontalLayoutDurata.addWidget(self.labelDurataValue)
        self.labelMinuti = QtWidgets.QLabel(Form)
        self.labelMinuti.setObjectName("labelMinuti")
        self.horizontalLayoutDurata.addWidget(self.labelMinuti)
        self.verticalLayoutDatiTrattamento.addLayout(self.horizontalLayoutDurata)
        self.verticalLayoutPrincipale.addLayout(self.verticalLayoutDatiTrattamento)
        """
        self.radioButtonSedutaEffettuata = QtWidgets.QRadioButton(Form)
        self.radioButtonSedutaEffettuata.setObjectName("radioButtonSedutaEffettuata")
        self.radioButtonSedutaEffettuata.setChecked(self.prenotazione.completata)
        self.verticalLayoutPrincipale.addWidget(self.radioButtonSedutaEffettuata)
        """
        self.horizontalLayoutSedutaCompletata = QtWidgets.QHBoxLayout()
        self.horizontalLayoutSedutaCompletata.setObjectName("horizontalLayoutSedutaCompletata")
        self.labelSedutaCompletata = QtWidgets.QLabel(Form)
        self.labelSedutaCompletata.setMaximumSize(QtCore.QSize(150, 16777215))
        self.labelSedutaCompletata.setObjectName("labelSedutaCompletata")
        self.horizontalLayoutSedutaCompletata.addWidget(self.labelSedutaCompletata)
        self.labelSedutaCompletataValue = QtWidgets.QLabel(Form)
        self.labelSedutaCompletataValue.setText("")
        self.labelSedutaCompletataValue.setObjectName("labelSedutaCompletataValue")
        self.horizontalLayoutSedutaCompletata.addWidget(self.labelSedutaCompletataValue)
        self.verticalLayoutDatiTrattamento.addLayout(self.horizontalLayoutSedutaCompletata)

        self.horizontalLayoutEliminaModificaTra = QtWidgets.QHBoxLayout()
        self.horizontalLayoutEliminaModificaTra.setObjectName("horizontalLayoutEliminaModificaTra")
        self.pushButtonEliminaPrenotazione = QtWidgets.QPushButton(Form)
        self.pushButtonEliminaPrenotazione.setObjectName("pushButtonEliminaPrenotazione")
        self.pushButtonEliminaPrenotazione.clicked.connect(lambda: self.eliminaPrenotazione(Form))

        self.horizontalLayoutEliminaModificaTra.addWidget(self.pushButtonEliminaPrenotazione)
        self.pushButtonModificaPrenotazione = QtWidgets.QPushButton(Form)
        self.pushButtonModificaPrenotazione.setObjectName("pushButtonModificaPrenotazione")
        self.pushButtonModificaPrenotazione.clicked.connect(lambda: self.modificaPrenotazione(Form, app))

        self.horizontalLayoutEliminaModificaTra.addWidget(self.pushButtonModificaPrenotazione)
        self.verticalLayoutPrincipale.addLayout(self.horizontalLayoutEliminaModificaTra)
        self.verticalLayout.addLayout(self.verticalLayoutPrincipale)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.caricaCostoDurataPrenotazione()
        self.setSedutaCompletata()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Segretario - Visualizza prenotazione"))
        self.pushButtonIndietro.setText(_translate("Form", "INDIETRO"))
        self.pushButtonLogout.setText(_translate("Form", "LOGOUT"))
        self.labelDettagliTrattamento.setText(_translate("Form", "Dettagli prenotazione:"))
        self.labelTipologia.setText(_translate("Form", "Tipologia della seduta:"))

        if self.prenotazione.trattamento:
            self.labelTrattamento.setText(_translate("Form", "Trattamento:"))

        self.labelNome.setText(_translate("Form", "Nome:"))
        self.labelCognome.setText(_translate("Form", "Cognome:"))
        self.labelCodiceFiscale.setText(_translate("Form", "Codice fiscale:"))
        self.labelData.setText(_translate("Form", "Data della seduta:"))
        self.labelOrario.setText(_translate("Form", "Orario:"))
        self.labelCosto.setText(_translate("Form", "Costo:"))
        self.labelEuro.setText(_translate("Form", "€"))
        self.labelDurata.setText(_translate("Form", "Durata:"))
        self.labelMinuti.setText(_translate("Form", "minuti"))
        #self.radioButtonSedutaEffettuata.setText(_translate("Form", "Seduta effettuata"))
        self.labelSedutaCompletata.setText(_translate("Form", "Stato della prenotazione:"))
        self.pushButtonEliminaPrenotazione.setText(_translate("Form", "Elimina prenotazione"))
        self.pushButtonModificaPrenotazione.setText(_translate("Form", "Modifica prenotazione"))

    def setSedutaCompletata(self):
        if self.prenotazione.completata:
            self.labelSedutaCompletataValue.setText("Seduta effettuta")
        else:
            self.labelSedutaCompletataValue.setText("Seduta non ancora effettuata")

    def eliminaPrenotazione(self, Form):
        popupConferma = QMessageBox()
        popupConferma.setIcon(QMessageBox.Warning)
        popupConferma.setText("Sei sicuro di voler eliminare la prenotazione visualizzata?")
        popupConferma.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        popupConferma.setWindowTitle("Conferma eliminazione trattamento")
        risposta = popupConferma.exec_()
        if risposta == QMessageBox.Ok:
            PrenotazioneController().eliminaPrenotazione(self.prenotazione)
            self.aggiornaListaPrenotazioni()
            self.chiudiFinestra(Form)

    def modificaPrenotazione(self, Form, app):
        self.vistaModificaPrenotazione = QtWidgets.QWidget()
        uivistaModificaPrenotazione = ModificaPrenotazioneView(self.prenotazione, self.aggiornaListaPrenotazioni)
        uivistaModificaPrenotazione.setupUi(self.vistaModificaPrenotazione, app)
        self.vistaModificaPrenotazione.show()
        self.chiudiFinestra(Form)

    def caricaCostoDurataPrenotazione(self):
        if self.prenotazione.trattamento:
            self.labelCostoValue.setText(str(self.prenotazione.trattamento.costo))
            self.labelDurataValue.setText(str(self.prenotazione.trattamento.durata))
        else:
            consulenza = ConsulenzaController().getConsulenza()
            self.labelCostoValue.setText(consulenza.costo)
            self.labelDurataValue.setText(consulenza.durata)


    def chiudiFinestra(self, Form):
        Form.close()

    def chiudiApp(self, app):
        sys.exit(app.exec_())

"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = VisualizzaPrenotazioneView()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
"""