from Generale.GeneraleModel.LoginModel import LoginModel

class LoginController():

    def verificaCredenziali(cls, login, password):
        return LoginModel.verificaCredenziali(LoginModel, login, password)

