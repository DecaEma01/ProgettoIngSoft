class GestioneFile():

    def gestionePazienti(cls,soggetto):
        pazienti = {}
        if os.path.isfile('Dati/Pazienti.pickle'):
            with open('Dati/Pazienti.pickle',rb) as file:
                pazienti = pickle.load(file)
        pazienti[soggetto.codicePaziente] = soggetto
        with open('Dati/Pazienti.pickle', wb) as file:
            pickle.dump(pazienti, file, pickle.HIGHEST_PROTOCOL)