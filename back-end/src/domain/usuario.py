class Usuario:
    def __init__(self, id: int = None, nome: str = None, senha: str = None):
        self.__id = id
        self.__nome = nome
        self.__senha = senha
       
    def getId(self):
        return self.__id

    def setId(self, id : str):
        self.__id = id

    def getNome(self):
        return self.__nome

    def setNome(self, nome : str):
        self.__nome = nome
    
    def getSenha(self):
        return self.__senha

    def setSenha(self, senha : str):
        self.__senha = senha
    
    def toString(self):
        return {
            "id"  : self.__id,
            "nome"  : self.__nome,
            "senha"   : self.__senha,
        }