from datetime import datetime
import shutil

class BackupModel():
    def __init__(self):
        pass
        #self.backupDone = False

    def eseguiBackup(self):

        #now = datetime.now()
        #current_time = now.strftime("%H:%M:%S")
        #if self.backupDone == False and current_time == '22:00:00':
        try:
            shutil.copy2('Dati/Dipendenti.pickle', 'DataBackup/autentificazione.json')
            shutil.copy2('Dati/Consulenza.pickle', 'DataBackup/Consulenza.pickle')
            shutil.copy2('Dati/Dipendenti.pickle', 'DataBackup/Dipendenti.pickle')
            shutil.copy2('Dati/Pazienti.pickle', 'DataBackup/Pazienti.pickle')
            shutil.copy2('Dati/Trattamenti.pickle', 'DataBackup/Trattamenti.pickle')
            shutil.copy2('Dati/Prenotazioni.pickle', 'DataBackup/Prenotazioni.pickle')
            print('backup eseguito')
            #self.backupDone = True
        except IndexError:
            print("Errore di backup ...")



        #if current_time == '22:00:01':
        #if current_time == '22:55:01':
        #    self.backupDone = False

