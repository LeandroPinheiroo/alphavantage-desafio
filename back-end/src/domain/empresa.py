class Empresa:

    def __init__(self, id: int = None, nome: str = None, classificao_setorial: str = None, estado: str = None, ramo: str = None, classificacao: int = None):
        self.__id = id
        self.__nome = nome
        self.__classificao_setorial = classificao_setorial
        self.__estado = estado
        self.__ramo = ramo
        self.__classificacao = classificacao

       
    def getId(self):
        return self.__id

    def setId(self, id : str):
        self.__id = id

    def getNome(self):
        return self.__nome

    def setNome(self, nome : str):
        self.__nome = nome
    
    def getClassificacaoSetorial(self):
        return self.__classificao_setorial

    def setClassificacaoSetorial(self, classificao_setorial : str):
        self.__classificao_setorial = classificao_setorial

    def getEstado(self):
        return self.__estado

    def setEstado(self, estado : str):
        self.__estado = estado

    def getRamo(self):
        return self.__ramo

    def setRamo(self, ramo : str):
        self.__ramo = ramo

    def getRamo(self):
        return self.__ramo

    def setRamo(self, ramo : str):
        self.__ramo = ramo

    def getClassificacao(self):
        return self.__classificacao

    def setClassificacao(self, classificacao : int):
        self.__classificacao = classificacao
    
    def toString(self):
        return {
            "id": self.__id,
            "nome": self.__nome,
            "classificao_setorial": self.__classificao_setorial,
            "estado": self.__estado,
            "ramo": self.__ramo,
            "classificacao": self.__classificacao,
        }