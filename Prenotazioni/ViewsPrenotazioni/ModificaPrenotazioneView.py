# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ModificaPrenotazioneView.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Prenotazioni.ControllersPrenotazioni.PrenotazioneController import PrenotazioneController
from TrattamentiConsulenze.ControllersTrattCons.ConsulenzaController import ConsulenzaController
from TrattamentiConsulenze.ControllersTrattCons.ElencoTrattamentiController import ElencoTrattamentiController


class ModificaPrenotazioneView(object):
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

        self.labelDettagliPrenotazione = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.labelDettagliPrenotazione.setFont(font)
        self.labelDettagliPrenotazione.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDettagliPrenotazione.setObjectName("labelDettagliPrenotazione")
        self.verticalLayoutPrincipale.addWidget(self.labelDettagliPrenotazione)
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

            self.comboBoxTrattamento = QtWidgets.QComboBox(Form)
            self.comboBoxTrattamento.setObjectName("comboBoxTrattamento")
            self.comboBoxTrattamento.addItems(self.getListaInfoTrattamenti())
            self.comboBoxTrattamento.activated.connect(self.aggiornaCostoDurataTrattamento)

            self.horizontalLayout_8.addWidget(self.comboBoxTrattamento)
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
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelData = QtWidgets.QLabel(Form)
        self.labelData.setMaximumSize(QtCore.QSize(110, 16777215))
        self.labelData.setObjectName("labelData")
        self.horizontalLayout_2.addWidget(self.labelData)
        self.dateEditDataSeduta = QtWidgets.QDateEdit(Form)
        self.dateEditDataSeduta.setObjectName("dateEditDataSeduta")
        self.dateEditDataSeduta.setDate(self.prenotazione.data)
        self.horizontalLayout_2.addWidget(self.dateEditDataSeduta)
        self.verticalLayoutDatiTrattamento.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        spacerItem = QtWidgets.QSpacerItem(40, 25, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayoutPrincipale.addItem(spacerItem)

        self.labelOrario = QtWidgets.QLabel(Form)
        self.labelOrario.setMaximumSize(QtCore.QSize(45, 16777215))
        self.labelOrario.setObjectName("labelOrario")
        self.horizontalLayout_3.addWidget(self.labelOrario)
        self.comboBoxOrario = QtWidgets.QComboBox(Form)
        self.comboBoxOrario.setObjectName("comboBoxOrario")
        self.comboBoxOrario.addItems(["8:00", "9:00", "10:00", "11:00", "12:00",
                                      "14:00", "15:00", "16:00", "17:00", "18:00"])
        self.comboBoxOrario.setCurrentText(self.prenotazione.ora)

        self.horizontalLayout_3.addWidget(self.comboBoxOrario)
        self.verticalLayoutDatiTrattamento.addLayout(self.horizontalLayout_3)
        self.horizontalLayoutCosto = QtWidgets.QHBoxLayout()
        self.horizontalLayoutCosto.setObjectName("horizontalLayoutCosto")
        self.labelCosto = QtWidgets.QLabel(Form)
        self.labelCosto.setMaximumSize(QtCore.QSize(45, 16777215))
        self.labelCosto.setObjectName("labelCosto")
        self.horizontalLayoutCosto.addWidget(self.labelCosto)
        self.labelCostoValue = QtWidgets.QLabel(Form)
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
        self.labelDurataValue.setText("")
        self.labelDurataValue.setObjectName("labelDurataValue")
        self.horizontalLayoutDurata.addWidget(self.labelDurataValue)
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
        self.pushButtonModificaSalva = QtWidgets.QPushButton(Form)
        self.pushButtonModificaSalva.setObjectName("pushButtonModificaSalva")
        self.pushButtonModificaSalva.clicked.connect(lambda: self.salvaModificaPrenotazione(Form))

        self.horizontalLayoutEliminaModificaTra.addWidget(self.pushButtonModificaSalva)
        self.verticalLayoutPrincipale.addLayout(self.horizontalLayoutEliminaModificaTra)
        self.verticalLayout.addLayout(self.verticalLayoutPrincipale)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.caricaCostoDurataPrenotazione()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Segretario - Modifica Prenotazione"))
        self.pushButtonIndietro.setText(_translate("Form", "INDIETRO"))
        self.pushButtonLogout.setText(_translate("Form", "LOGOUT"))
        self.labelDettagliPrenotazione.setText(_translate("Form", "Dettagli prenotazione:"))
        self.labelTipologia.setText(_translate("Form", "Tipologia della seduta:"))

        if self.prenotazione.trattamento:
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

    def getListaInfoTrattamenti(self):
        trattamenti = ElencoTrattamentiController().getElencoTrattamenti()
        arrayComboBoxTrattamenti=[]
        for trattamento in trattamenti.values():
            etichetta = f"{trattamento.nome} : {trattamento.classe} - {trattamento.codiceTrattamento}"
            arrayComboBoxTrattamenti.append(etichetta)
        return arrayComboBoxTrattamenti

    def salvaModificaPrenotazione(self, Form):
        sedutaEffettuata = self.getRadioSedutaEffettuata()

        if self.prenotazione.trattamento:
            trattamento = self.getTrattamentoSelezionatoCombo()
        else:
            trattamento = None

        PrenotazioneController().modificaPrenotazione(self.prenotazione, self.dateEditDataSeduta.date(), self.comboBoxOrario.currentText(),
                                                      sedutaEffettuata, trattamento)

        self.chiudiFinestra(Form) #chiudendosi la finestra viene mostrata nuovamente la finestra della lista delle prenotazioni che stava sotto
        self.aggiornaListaPrenotazioni() #la finestra della lista delle prenotazioni si deve aggiornare per far comparire il trattamento appena aggiunto

        """
        if self.tipoPrenotazione:
            trattamento = self.getTrattamentoSelezionatoCombo()
        else:
            trattamento = None

        if self.controllaGiornoConsuleza():
            data = self.getDataInserita()
            orario = self.comboBoxOrario.currentText()
            paziente = self.paziente
        """

    def caricaCostoDurataPrenotazione(self):
        if self.prenotazione.trattamento:
            self.labelCostoValue.setText(str(self.prenotazione.trattamento.costo))
            self.labelDurataValue.setText(str(self.prenotazione.trattamento.durata))
        else:
            consulenza = ConsulenzaController().getConsulenza()
            self.labelCostoValue.setText(consulenza.costo)
            self.labelDurataValue.setText(consulenza.durata)

    def getTrattamentoSelezionatoCombo(self):
        etichettaTrattamento = self.comboBoxTrattamento.currentText()
        codiceTrattamento = int(etichettaTrattamento.split("-")[1].strip())
        dictParametri = {}
        dictParametri["codiceTrattamento"] = codiceTrattamento
        trattamentoRisultato = ElencoTrattamentiController().ricercaTrattamento(dictParametri)[codiceTrattamento]
        return trattamentoRisultato

    def getRadioSedutaEffettuata(self):
        if self.radioButtonSedutaEffettuata.isChecked() == True:
            return True
        else:
            return False

    def aggiornaCostoDurataTrattamento(self):
        trattamentoSelezionato = self.getTrattamentoSelezionatoCombo()
        self.labelCostoValue.setText(trattamentoSelezionato.costo)
        self.labelDurataValue.setText(trattamentoSelezionato.durata)

    def chiudiFinestra(self, Form):
        Form.close()

    def chiudiApp(self, app):
        sys.exit(app.exec_())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = ModificaPrenotazioneView()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
