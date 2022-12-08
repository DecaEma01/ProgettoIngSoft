from datetime import datetime
import shutil

class BackupModel():

    backupDone = False

    def eseguiBackup(cls):

        now = datetime.now()
        current_time = now.strftime("%M:%S")

        if cls.backupDone == False and current_time == '32:00':
            print('backup ...')
            try:
                shutil.copy2('Dati/Dipendenti.pickle', 'Backup/autentificazione.json')
                shutil.copy2('Dati/Consulenza.pickle', 'Backup/Consulenza.pickle')
                shutil.copy2('Dati/Dipendenti.pickle', 'Backup/Dipendenti.pickle')
                shutil.copy2('Dati/Pazienti.pickle', 'Backup/Pazienti.pickle')
                shutil.copy2('Dati/Trattamentu.pickle', 'Backup/Trattamenti.pickle')
                shutil.copy2('Dati/Prenotazioni.pickle', 'Backup/Prenotazioni.pickle')
                print('backup eseguito')
                cls.backupDone = True
            except IndexError:
                print("Errore di backup ...")


        if current_time == '32:01':
            cls.backupDone = False

