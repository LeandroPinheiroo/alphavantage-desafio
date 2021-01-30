from src.domain.cotacao import Cotacao

class Empresa:

    def __init__(self, id: int = None, nome: str = None, classificao_setorial: str = None, ramo: str = None, classificacao: int = None, cotacao:Cotacao = None):
        self.__id = id
        self.__nome = nome
        self.__classificao_setorial = classificao_setorial
        self.__ramo = ramo
        self.__classificacao = classificacao
        self.__cotacao = cotacao

       
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


    def getRamo(self):
        return self.__ramo

    def setRamo(self, ramo : str):
        self.__ramo = ramo


    def getClassificacao(self):
        return self.__classificacao

    def setClassificacao(self, classificacao : int):
        self.__classificacao = classificacao

    def getCotacao(self):
        return self.__cotacao

    def setCotacao(self, cotacao : Cotacao):
        self.__cotacao = cotacao
    
    def toString(self):
        if(self.__cotacao is not None):
            return {
                "id": self.getId(),
                "nome": self.getNome(),
                "classificao_setorial": self.getClassificacaoSetorial(),
                "ramo": self.getRamo(),
                "classificacao": self.getClassificacao(),
                "cotacao":self.__cotacao.toString()
            }
        return {
                "id": self.getId(),
                "nome": self.getNome(),
                "classificao_setorial": self.getClassificacaoSetorial(),
                "ramo": self.getRamo(),
                "classificacao": self.getClassificacao()
            }
