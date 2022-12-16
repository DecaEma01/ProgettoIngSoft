import os.path, pickle

import unittest
from Pazienti.ModelsPazienti.PazienteModel import PazienteModel
from Pazienti.ModelsPazienti.ElencoPazientiModel import ElencoPazientiModel

class TestPaziente(unittest.TestCase):

    #tutti i metodi di test eliminano il paziente per cui il test viene effettuato in modo da lasciare invariato il relativo file pickle

    def test_Aggiungi_Paziente(self):
        
        self.paziente = PazienteModel("Test","Test","Test","1","Test","1","Test","Test",{})
        TestPaziente.paziente = self.paziente
        pazienti = None
        
        if os.path.isfile('Dati/Pazienti.pickle'):
            with open('Dati/Pazienti.pickle','rb') as f:
                pazienti = pickle.load(f)
                
            self.assertIsNotNone(pazienti)
            self.assertIn(self.paziente.codicePaziente, pazienti)

        PazienteModel.eliminaPazienteM(self.paziente)

    def test_modificaPaziente(self):
        self.paziente = PazienteModel("Test", "Test", "Test", "1", "Test", "1", "Test", "Test", {})
        pazienti = None
        
        if os.path.isfile('Dati/Pazienti.pickle'):
            with open('Dati/Pazienti.pickle','rb') as f:
                pazienti = pickle.load(f)
                
        self.assertIsNotNone(pazienti)
        self.assertIn(self.paziente.codicePaziente, pazienti)
        PazienteModel.modificaPazienteM(self.paziente,"Te","Te","Te","2","Te","2","Te","Te",{1:"Test"})
        
        if os.path.isfile('Dati/Pazienti.pickle'):
          with open('Dati/Pazienti.pickle','rb') as f:   
                pazienti = pickle.load(f)
                
        self.assertIsNotNone(pazienti)
        self.assertIn(self.paziente.codicePaziente, pazienti)

        PazienteModel.eliminaPazienteM(self.paziente)

    def test_rimuoviPaziente(self):
        self.paziente = PazienteModel("Test", "Test", "Test", "1", "Test", "1", "Test", "Test", {})
        pazienti = None
        
        if os.path.isfile('Dati/Pazienti.pickle'):
            with open('Dati/Pazienti.pickle','rb') as f:
                pazienti = pickle.load(f)
                
        self.assertIsNotNone(pazienti)
        self.assertIn(self.paziente.codicePaziente, pazienti)        
        PazienteModel.eliminaPazienteM(self.paziente)

        if os.path.isfile('Dati/Pazienti.pickle'):
            with open('Dati/Pazienti.pickle','rb') as f:
                pazienti = pickle.load(f)
                
        self.assertIsNotNone(pazienti)
        self.assertNotIn(self.paziente.codicePaziente, pazienti)


if __name__ == '__main__':
    unittest.main()