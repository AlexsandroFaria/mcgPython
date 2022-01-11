class Classe:
    def __init__(self, id_classe=None, nome_classe=None, referencia=None):
        self._id_classe = id_classe
        self._nome_classe = nome_classe
        self._referencia = referencia

    @property
    def id_classe(self):
        return self._id_classe

    @id_classe.setter
    def id_classe(self, valor):
        self._id_classe = valor

    @property
    def nome_classe(self):
        return self._nome_classe

    @nome_classe.setter
    def nome_classe(self, valor):
        self._nome_classe = valor

    @property
    def referencia(self):
        return self._referencia

    @referencia.setter
    def referencia(self, valor):
        self._referencia = valor