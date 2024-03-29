# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NuovaPrenotazione3View.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Prenotazioni.ControllersPrenotazioni.PrenotazioneController import PrenotazioneController
#from Prenotazioni.ViewsPrenotazioni.GestionePrenotazioniView import GestionePrenotazioniView
from Prenotazioni.ViewsPrenotazioni.PrenotazioniRegistrateView import PrenotazioniRegistrateView
from TrattamentiConsulenze.ControllersTrattCons.ConsulenzaController import ConsulenzaController
from TrattamentiConsulenze.ControllersTrattCons.ElencoTrattamentiController import ElencoTrattamentiController


class NuovaPrenotazione3View(object):
    def __init__(self, paziente, tipoPrenotazione): #se tipoPrenotazione è true allora si vuole prenotare una seduta di Trattamento fisioterapico , se False di Consulenza medica
        self.paziente = paziente
        self.tipoPrenotazione = tipoPrenotazione
        if tipoPrenotazione:
            self.tipologiaSeduta = "Seduta di trattamento fisioterapico"
        else:
            self.tipologiaSeduta = "Seduta di consulenza medica"

    def setupUi(self, Form, app, istanzaP2View, istanzaP1View, istanzaGestioneView):
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
        self.horizontalLayoutIndietroLogout.addWidget(self.pushButtonIndietro)
        self.pushButtonIndietro.clicked.connect(lambda: self.chiudiFinestra(Form))

        self.pushButtonLogout = QtWidgets.QPushButton(Form)
        self.pushButtonLogout.setObjectName("pushButtonLogout")
        self.pushButtonLogout.clicked.connect(lambda: self.chiudiApp(app))

        self.horizontalLayoutIndietroLogout.addWidget(self.pushButtonLogout)
        self.verticalLayoutPrincipale.addLayout(self.horizontalLayoutIndietroLogout)
        self.labelDettagliPrenotazione = QtWidgets.QLabel(Form)
        self.labelDettagliPrenotazione.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.labelDettagliPrenotazione.setFont(font)
        self.labelDettagliPrenotazione.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDettagliPrenotazione.setObjectName("labelDettagliPrenotazione")
        self.verticalLayoutPrincipale.addWidget(self.labelDettagliPrenotazione)
        self.verticalLayoutDatiPrenotazione = QtWidgets.QVBoxLayout()
        self.verticalLayoutDatiPrenotazione.setObjectName("verticalLayoutDatiPrenotazione")
        self.horizontalLayoutTipologia = QtWidgets.QHBoxLayout()
        self.horizontalLayoutTipologia.setObjectName("horizontalLayoutTipologia")
        self.labelTipologia = QtWidgets.QLabel(Form)
        self.labelTipologia.setMaximumSize(QtCore.QSize(135, 16777215))
        self.labelTipologia.setObjectName("labelTipologia")
        self.horizontalLayoutTipologia.addWidget(self.labelTipologia)
        self.labelTipologiaValue = QtWidgets.QLabel(Form)
        self.labelTipologiaValue.setText(str(self.tipologiaSeduta))

        self.labelTipologiaValue.setObjectName("labelTipologiaValue")
        self.horizontalLayoutTipologia.addWidget(self.labelTipologiaValue)
        self.verticalLayoutDatiPrenotazione.addLayout(self.horizontalLayoutTipologia)
        self.horizontalLayoutNome = QtWidgets.QHBoxLayout()
        self.horizontalLayoutNome.setObjectName("horizontalLayoutNome")
        self.labelNome = QtWidgets.QLabel(Form)
        self.labelNome.setMaximumSize(QtCore.QSize(45, 16777215))
        self.labelNome.setObjectName("labelNome")
        self.horizontalLayoutNome.addWidget(self.labelNome)
        self.labelNomeValue = QtWidgets.QLabel(Form)
        self.labelNomeValue.setText(str(self.paziente.nome))
        self.labelNomeValue.setObjectName("labelNomeValue")
        self.horizontalLayoutNome.addWidget(self.labelNomeValue)
        self.verticalLayoutDatiPrenotazione.addLayout(self.horizontalLayoutNome)
        self.horizontalLayoutCognome = QtWidgets.QHBoxLayout()
        self.horizontalLayoutCognome.setObjectName("horizontalLayoutCognome")
        self.labelCognome = QtWidgets.QLabel(Form)
        self.labelCognome.setMaximumSize(QtCore.QSize(65, 16777215))
        self.labelCognome.setObjectName("labelCognome")
        self.horizontalLayoutCognome.addWidget(self.labelCognome)
        self.labelCognomeValue = QtWidgets.QLabel(Form)
        self.labelCognomeValue.setText(str(self.paziente.cognome))
        self.labelCognomeValue.setObjectName("labelCognomeValue")
        self.horizontalLayoutCognome.addWidget(self.labelCognomeValue)
        self.verticalLayoutDatiPrenotazione.addLayout(self.horizontalLayoutCognome)

        if self.tipoPrenotazione:
            self.horizontalLayoutTrattamento = QtWidgets.QHBoxLayout()
            self.horizontalLayoutTrattamento.setObjectName("horizontalLayoutTrattamento")
            self.labelTrattamento = QtWidgets.QLabel(Form)
            self.labelTrattamento.setMaximumSize(QtCore.QSize(80, 16777215))
            self.labelTrattamento.setObjectName("labelTrattamento")
            self.horizontalLayoutTrattamento.addWidget(self.labelTrattamento)
            self.comboBoxTrattamento = QtWidgets.QComboBox(Form)
            self.comboBoxTrattamento.setMinimumSize(QtCore.QSize(0, 30))
            self.comboBoxTrattamento.setObjectName("comboBoxTrattamento")
            self.comboBoxTrattamento.addItems(self.getListaInfoTrattamenti())
            self.comboBoxTrattamento.activated.connect(self.aggiornaCostoDurataTrattamento)

            self.horizontalLayoutTrattamento.addWidget(self.comboBoxTrattamento)
            self.verticalLayoutDatiPrenotazione.addLayout(self.horizontalLayoutTrattamento)


        spacerItem = QtWidgets.QSpacerItem(40, 25, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayoutDatiPrenotazione.addItem(spacerItem)
        self.horizontalLayoutData = QtWidgets.QHBoxLayout()
        self.horizontalLayoutData.setObjectName("horizontalLayoutData")
        self.labelData = QtWidgets.QLabel(Form)
        self.labelData.setMaximumSize(QtCore.QSize(110, 16777215))
        self.labelData.setObjectName("labelData")
        self.horizontalLayoutData.addWidget(self.labelData)
        self.dateEditDataSeduta = QtWidgets.QDateEdit(Form)
        self.dateEditDataSeduta.setDateTime(QtCore.QDateTime.currentDateTime())

        self.dateEditDataSeduta.setMinimumSize(QtCore.QSize(0, 30))
        self.dateEditDataSeduta.setObjectName("dateEditDataSeduta")
        self.horizontalLayoutData.addWidget(self.dateEditDataSeduta)
        self.verticalLayoutDatiPrenotazione.addLayout(self.horizontalLayoutData)
        spacerItem1 = QtWidgets.QSpacerItem(40, 25, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayoutDatiPrenotazione.addItem(spacerItem1)
        self.horizontalLayoutOrario = QtWidgets.QHBoxLayout()
        self.horizontalLayoutOrario.setObjectName("horizontalLayoutOrario")
        self.labelOrario = QtWidgets.QLabel(Form)
        self.labelOrario.setMaximumSize(QtCore.QSize(45, 16777215))
        self.labelOrario.setObjectName("labelOrario")
        self.horizontalLayoutOrario.addWidget(self.labelOrario)
        self.comboBoxOrario = QtWidgets.QComboBox(Form)
        self.comboBoxOrario.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBoxOrario.setObjectName("comboBoxOrario")
        self.comboBoxOrario.addItems(["8:00","9:00", "10:00", "11:00", "12:00",
                                    "14:00", "15:00","16:00","17:00", "18:00"])

        self.horizontalLayoutOrario.addWidget(self.comboBoxOrario)
        self.verticalLayoutDatiPrenotazione.addLayout(self.horizontalLayoutOrario)
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
        self.verticalLayoutDatiPrenotazione.addLayout(self.horizontalLayoutCosto)
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
        self.verticalLayoutDatiPrenotazione.addLayout(self.horizontalLayoutDurata)
        self.verticalLayoutPrincipale.addLayout(self.verticalLayoutDatiPrenotazione)
        self.horizontalLayoutSalvaPrenotazione = QtWidgets.QHBoxLayout()
        self.horizontalLayoutSalvaPrenotazione.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayoutSalvaPrenotazione.setContentsMargins(-1, -1, 11, -1)
        self.horizontalLayoutSalvaPrenotazione.setObjectName("horizontalLayoutSalvaPrenotazione")
        self.pushButtonSalvaPrenotazione = QtWidgets.QPushButton(Form)
        self.pushButtonSalvaPrenotazione.setObjectName("pushButtonSalvaPrenotazione")
        self.pushButtonSalvaPrenotazione.clicked.connect(lambda: self.salvaPrenotazione(Form, istanzaP2View, istanzaP1View, istanzaGestioneView))

        self.horizontalLayoutSalvaPrenotazione.addWidget(self.pushButtonSalvaPrenotazione)
        self.verticalLayoutPrincipale.addLayout(self.horizontalLayoutSalvaPrenotazione)
        self.verticalLayout.addLayout(self.verticalLayoutPrincipale)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        if self.tipoPrenotazione:
            self.aggiornaCostoDurataTrattamento()
        else:
            self.aggiornaCostoDurataConsulenza()


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Segretario - Nuova prenotazione - riepilogo prenotazione"))
        self.pushButtonIndietro.setText(_translate("Form", "INDIETRO"))
        self.pushButtonLogout.setText(_translate("Form", "LOGOUT"))
        self.labelDettagliPrenotazione.setText(_translate("Form", "Dettagli prenotazione:"))
        self.labelTipologia.setText(_translate("Form", "Tipologia della seduta:"))
        self.labelNome.setText(_translate("Form", "Nome:"))
        self.labelCognome.setText(_translate("Form", "Cognome:"))

        if self.tipoPrenotazione:
            self.labelTrattamento.setText(_translate("Form", "Trattamento:"))

        self.labelData.setText(_translate("Form", "Data della seduta:"))
        self.labelOrario.setText(_translate("Form", "Orario:"))
        self.labelCosto.setText(_translate("Form", "Costo:"))
        self.labelEuro.setText(_translate("Form", "€"))
        self.labelDurata.setText(_translate("Form", "Durata:"))
        self.labelMinuti.setText(_translate("Form", "minuti"))
        self.pushButtonSalvaPrenotazione.setText(_translate("Form", "Salva prenotazione"))

    def chiudiFinestra(self,Form):
        Form.close()

    def chiudiApp(self,app):
        sys.exit(app.exec_())

    def salvaPrenotazione(self, Form, istanzaP2View, istanzaP1View, istanzaGestioneView):
        if self.tipoPrenotazione:
            trattamento = self.getTrattamentoSelezionatoCombo()
        else:
            trattamento = None

        if ((not trattamento) and self.controllaGiornoConsuleza()) or trattamento:
            data = self.getDataInserita()
            orario = self.comboBoxOrario.currentText()
            paziente = self.paziente

            PrenotazioneController().aggiungiPrenotazione(data, orario, paziente, trattamento)

            Form.close()
            istanzaP2View.close()
            istanzaP1View.close()




    def getListaInfoTrattamenti(self):
        trattamenti = ElencoTrattamentiController().getElencoTrattamenti()
        arrayComboBoxTrattamenti=[]
        for trattamento in trattamenti.values():
            etichetta = f"{trattamento.nome} : {trattamento.classe} - {trattamento.codiceTrattamento}"
            arrayComboBoxTrattamenti.append(etichetta)
        return arrayComboBoxTrattamenti

    def getDataInserita(self):
        dataInserita = self.dateEditDataSeduta.dateTime().date()
        return dataInserita

    def controllaGiornoConsuleza(self):
        dataInserita = self.getDataInserita()
        giornoSettimanaInserito = dataInserita.dayOfWeek()

        consulenza = ConsulenzaController().getConsulenza()
        giornoConsulenza = consulenza.giornoSettimana

        if giornoSettimanaInserito >= 1 and giornoSettimanaInserito <=6:
            numeroGiornoConsulenza = self.convertiGiornoSettimanaNumero(giornoConsulenza)
        else:
            numeroGiornoConsulenza = -1

        if numeroGiornoConsulenza == giornoSettimanaInserito :
            return True

        if numeroGiornoConsulenza == -1:
            errore = QMessageBox()
            errore.setWindowTitle("Errore di inserimento")
            errore.setText(
                "Hai inserito una data corrispondente ad una domenica. Di domenica il centro è chiuso. Inserisci un'altra data")
            errore.setIcon(QMessageBox.Warning)
            errore.setStandardButtons(QMessageBox.Ok)
            errore.exec_()
            return False
        elif numeroGiornoConsulenza != giornoSettimanaInserito :
            errore = QMessageBox()
            errore.setWindowTitle("Errore di inserimento")
            errore.setText(
                f"Hai inserito una data corrispondente ad un giorno della settimana ,"
                f" il {self.convertiNumeroSettimanaGiorno(dataInserita.dayOfWeek())},"
                f" che non coincide con quello attualmente previsto per le consulenze, il {giornoConsulenza},"
                f" inserisci quindi una data corrispondente ad un {giornoConsulenza} .")
            errore.setIcon(QMessageBox.Warning)
            errore.setStandardButtons(QMessageBox.Ok)
            errore.exec_()
            return False

    def convertiGiornoSettimanaNumero(self, giorno):
        # è necessario ottenere il numero del giorno della settimana per confrontarlo col giorno della data inserita["lunedi","martedi","mercoledi","giovedi","venerdi","sabato"]
        if giorno == "lunedi":
            numeroGiorno = 1
        if giorno == "martedi":
            numeroGiorno = 2
        if giorno == "mercoledi":
            numeroGiorno = 3
        if giorno == "giovedi":
            numeroGiorno = 4
        if giorno == "venerdi":
            numeroGiorno = 5
        if giorno == "sabato":
            numeroGiorno = 6
        return numeroGiorno

    def convertiNumeroSettimanaGiorno(self, numeroGiorno):
        if numeroGiorno == 1:
            giorno = "lunedi"
        if numeroGiorno == 2:
            giorno = "martedi"
        if numeroGiorno == 3:
            giorno = "mercoledi"
        if numeroGiorno == 4:
            giorno = "giovedi"
        if numeroGiorno == 5:
            giorno = "venerdi"
        if numeroGiorno == 6:
            giorno = "sabato"
        return giorno

    def getTrattamentoSelezionatoCombo(self):
        etichettaTrattamento = self.comboBoxTrattamento.currentText()
        codiceTrattamento = int(etichettaTrattamento.split("-")[1].strip())
        dictParametri = {}
        dictParametri["codiceTrattamento"] = codiceTrattamento
        trattamentoRisultato = ElencoTrattamentiController().ricercaTrattamento(dictParametri)[codiceTrattamento]
        return trattamentoRisultato

    def aggiornaCostoDurataTrattamento(self):
        trattamentoSelezionato = self.getTrattamentoSelezionatoCombo()
        self.labelCostoValue.setText(trattamentoSelezionato.costo)
        self.labelDurataValue.setText(trattamentoSelezionato.durata)

    def aggiornaCostoDurataConsulenza(self):
        consulenza = ConsulenzaController().getConsulenza()
        self.labelCostoValue.setText(consulenza.costo)
        self.labelDurataValue.setText(consulenza.durata)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = NuovaPrenotazione3View()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())