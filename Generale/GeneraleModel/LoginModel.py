import json

class LoginModel():

    def verificaCredenziali(cls, login, password):
        f = open('Dati/autentificazione.json')
        data = json.load(f)['utenti']
        f.close()

        for utente in data:

            if login == utente['login'] and password == utente['password']:
                return utente

        return False


