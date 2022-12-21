import sched

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import os
from datetime import datetime
import threading

from Generale.GeneraleViews.LoginView import LoginView
from Generale.Backup.BackupModel import BackupModel

import time

def backupGiornaliero():

    dataOggi=datetime.today().strftime('%Y-%m-%d')
    orarioBackup = " 22:00:00"
    dataOrarioBackup = str(dataOggi+orarioBackup)
    datatimeBackup = datetime.strptime(dataOrarioBackup, '%Y-%m-%d %H:%M:%S')

    if datetime.now() < datatimeBackup:
        unixDataBackup = time.mktime(datatimeBackup.timetuple())
    else:
        unixDataBackup = time.mktime(datatimeBackup.timetuple())+ float(86400)

    print("unix timestamp dell'orario di backup di oggi "+str(unixDataBackup))

    # Set up scheduler
    s = sched.scheduler(time.time, time.sleep)
    # Schedule when you want the action to occur
    s.enterabs(unixDataBackup, 0, BackupModel().eseguiBackup)
    # Block until the action has been run
    s.run()

    print("fatto backup")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    x = threading.Thread(target=backupGiornaliero)
    x.start()

    app = QApplication(sys.argv)
    vistaLogin = LoginView(app)
    vistaLogin.show()
    sys.exit(app.exec())



