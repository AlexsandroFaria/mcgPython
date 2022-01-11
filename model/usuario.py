class Usuario:
    def __init__(self, id=None, nome=None, email=None, usuario=None, senha=None, acesso=None, lembrar_senha=None):
        self._id = id
        self._nome = nome
        self._email = email
        self._usuario = usuario
        self._senha = senha
        self._acesso = acesso
        self._lembrar_senha = lembrar_senha

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, valor):
        self._id = valor

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        self._email = valor

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, valor):
        self._usuario = valor

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, valor):
        self._senha = valor

    @property
    def acesso(self):
        return self._acesso

    @acesso.setter
    def acesso(self, valor):
        self._acesso = valor

    @property
    def lembrar_senha(self):
        return self._lembrar_senha

    @lembrar_senha.setter
    def lembrar_senha(self, valor):
        self._lembrar_senha = valor