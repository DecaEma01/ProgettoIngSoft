# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NuovaPrenotazione1View.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMessageBox

from Pazienti.ControllersPazienti.ElencoPazientiController import ElencoPazientiController
from Prenotazioni.ViewsPrenotazioni.NuovaPrenotazione2View import NuovaPrenotazione2View


class NuovaPrenotazione1View(object):
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
        self.labelDomandaSceglPaziente = QtWidgets.QLabel(Form)
        self.labelDomandaSceglPaziente.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono Light")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.labelDomandaSceglPaziente.setFont(font)
        self.labelDomandaSceglPaziente.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDomandaSceglPaziente.setObjectName("labelDomandaSceglPaziente")
        self.verticalLayoutPrincipale.addWidget(self.labelDomandaSceglPaziente)
        self.gridLayoutRicerca = QtWidgets.QGridLayout()
        self.gridLayoutRicerca.setObjectName("gridLayoutRicerca")
        self.lineEditRicercaCodiceFiscale = QtWidgets.QLineEdit(Form)
        self.lineEditRicercaCodiceFiscale.setObjectName("lineEditRicercaCodiceFiscale")
        self.gridLayoutRicerca.addWidget(self.lineEditRicercaCodiceFiscale, 3, 1, 1, 1)
        self.labelRicercaCognome = QtWidgets.QLabel(Form)
        self.labelRicercaCognome.setObjectName("labelRicercaCognome")
        self.gridLayoutRicerca.addWidget(self.labelRicercaCognome, 2, 0, 1, 1)
        self.labelRicercaNome = QtWidgets.QLabel(Form)
        self.labelRicercaNome.setObjectName("labelRicercaNome")
        self.gridLayoutRicerca.addWidget(self.labelRicercaNome, 1, 0, 1, 1)
        self.pushButtonRicerca = QtWidgets.QPushButton(Form)
        self.pushButtonRicerca.clicked.connect(self.ricercaPaziente)

        self.pushButtonRicerca.setObjectName("pushButtonRicerca")
        self.gridLayoutRicerca.addWidget(self.pushButtonRicerca, 7, 0, 1, 2)
        self.lineEditRicercaNome = QtWidgets.QLineEdit(Form)
        self.lineEditRicercaNome.setObjectName("lineEditRicercaNome")
        self.gridLayoutRicerca.addWidget(self.lineEditRicercaNome, 1, 1, 1, 1)
        self.lineEditRicercaCognome = QtWidgets.QLineEdit(Form)
        self.lineEditRicercaCognome.setObjectName("lineEditRicercaCognome")
        self.gridLayoutRicerca.addWidget(self.lineEditRicercaCognome, 2, 1, 1, 1)
        self.labelRicercaCodiceFiscale = QtWidgets.QLabel(Form)
        self.labelRicercaCodiceFiscale.setObjectName("labelRicercaCodiceFiscale")
        self.gridLayoutRicerca.addWidget(self.labelRicercaCodiceFiscale, 3, 0, 1, 1)
        self.verticalLayoutPrincipale.addLayout(self.gridLayoutRicerca)
        self.listViewPrenotazioni = QtWidgets.QListView(Form)
        self.listViewPrenotazioni.setObjectName("listViewPrenotazioni")
        self.verticalLayoutPrincipale.addWidget(self.listViewPrenotazioni)
        self.verticalLayoutVisualizzaPrenotazione = QtWidgets.QVBoxLayout()
        self.verticalLayoutVisualizzaPrenotazione.setObjectName("verticalLayoutVisualizzaPrenotazione")
        self.pushButtonSelezionaPaziente = QtWidgets.QPushButton(Form)
        self.pushButtonSelezionaPaziente.setObjectName("pushButtonSelezionaPaziente")
        self.pushButtonSelezionaPaziente.clicked.connect(lambda: self.selezionaPaziente(app))

        self.verticalLayoutVisualizzaPrenotazione.addWidget(self.pushButtonSelezionaPaziente)
        self.verticalLayoutPrincipale.addLayout(self.verticalLayoutVisualizzaPrenotazione)
        self.verticalLayout.addLayout(self.verticalLayoutPrincipale)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.visualizzaListaPazienti()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Segretario - Nuova prenotazione - Seleziona un paziente"))
        self.pushButtonIndietro.setText(_translate("Form", "INDIETRO"))
        self.pushButtonLogout.setText(_translate("Form", "LOGOUT"))
        self.labelDomandaSceglPaziente.setText(_translate("Form", "Per quale paziente vuoi registrare una nuova prenotazione?"))
        self.labelRicercaCognome.setText(_translate("Form", "Ricerca per cognome paziente:"))
        self.labelRicercaNome.setText(_translate("Form", "Ricerca per nome paziente: "))
        self.pushButtonRicerca.setText(_translate("Form", "Ricerca"))
        self.labelRicercaCodiceFiscale.setText(_translate("Form", "Ricerca per codice fiscale paziente:"))
        self.pushButtonSelezionaPaziente.setText(_translate("Form", "Seleziona paziente"))

    def chiudiFinestra(self,Form):
        Form.close()

    def chiudiApp(self,app):
        sys.exit(app.exec_())

    def visualizzaListaPazienti(self):
        self.pazienti = []
        self.pazienti.extend(ElencoPazientiController.listaPazientiC(ElencoPazientiController).values())

        listview_model = QStandardItemModel(self.listViewPrenotazioni)
        for paziente in self.pazienti:
            item = QStandardItem()
            etichetta = f" {paziente.nome} {paziente.cognome} | {paziente.codicefiscale} - {paziente.codicePaziente}"
            item.setText(etichetta)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(16)
            item.setFont(font)
            listview_model.appendRow(item)
        self.listViewPrenotazioni.setModel(listview_model)

    def ricercaPaziente(self):
        self.parametriRicerca = {'codicefiscale': self.lineEditRicercaCodiceFiscale, 'nome': self.lineEditRicercaNome, 'cognome': self.lineEditRicercaCognome}
        parametriRicercaNonVuoti = {}

        for chiave in self.parametriRicerca:
            if self.parametriRicerca[chiave].text() != '':
                parametriRicercaNonVuoti[chiave] = self.parametriRicerca[chiave].text()

        pazientiTrovati = ElencoPazientiController.ricercaPazienteC(ElencoPazientiController, **parametriRicercaNonVuoti).values()
        listviewModel = QStandardItemModel(self.listViewPrenotazioni)

        for paziente in pazientiTrovati:
            item = QStandardItem()
            etichetta = f" {paziente.nome} {paziente.cognome} | {paziente.codicefiscale} - {paziente.codicePaziente}"
            item.setText(etichetta)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(16)
            item.setFont(font)
            listviewModel.appendRow(item)
        self.listViewPrenotazioni.setModel(listviewModel)

    def selezionaPaziente(self, app):
        try:
            pazienteSelezionato = self.listViewPrenotazioni.selectedIndexes()[0].data()
            codicePaziente = int(pazienteSelezionato.split("-")[1].strip())
            paziente = ElencoPazientiController.ricercaPazienteC(ElencoPazientiController, codicePaziente=codicePaziente)[codicePaziente]

            self.vistaNuovaPrenotazione2 = QtWidgets.QWidget()
            uiNuovaPrenotazione2 = NuovaPrenotazione2View(paziente)
            uiNuovaPrenotazione2.setupUi(self.vistaNuovaPrenotazione2,app)
            self.vistaNuovaPrenotazione2.show()

        except IndexError:
            errore = QMessageBox()
            errore.setWindowTitle("Nessun paziente selezionato")
            errore.setText("Controlla di aver selezionato uno dei trattamenti , poi fai clic sul bottone seleziona paziente.")
            errore.setIcon(QMessageBox.Warning)
            errore.setStandardButtons(QMessageBox.Ok)
            errore.exec_()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = NuovaPrenotazione1View()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())