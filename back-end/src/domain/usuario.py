class Usuario:
    def __init__(self, id: int = None, nome: str = None, senha: str = None,email: str = None):
        self.__id = id
        self.__nome = nome
        self.__email = email
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

    def getEmail(self):
        return self.__email

    def setEmail(self, email : str):
        self.__email = email
    
    def toString(self):
        return {
            "id"  : self.__id,
            "nome"  : self.__nome,
            "email"  : self.__email,
            "senha"   : self.__senha,
        }