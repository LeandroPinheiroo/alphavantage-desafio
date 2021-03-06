import datetime

class Cotacao:

    def __init__(self, id: int = None, preco: float = None , volume: int = None , data: datetime = None , porcentagemVariacao: float = None, variacao: float = None , idEmpresa: int = None):
        self.__id = id
        self.__preco = preco
        self.__volume = volume
        self.__data = data
        self.__porcentagemVariacao = porcentagemVariacao
        self.__variacao = variacao
        self.__idEmpresa = idEmpresa

       
    def getId(self):
        return self.__id

    def setId(self, id : int):
        self.__id = id

    def getPreco(self):
        return self.__preco

    def setPreco(self, preco : float):
        self.__preco = preco
    
    def getVolume(self):
        return self.__volume

    def setVolume(self, volume : int):
        self.__volume = volume

    def getData(self):
        return self.__data

    def setData(self, data : datetime = datetime.date.today()):
        self.__data = data

    def getPorcentagemVariacao(self):
        return self.__porcentagemVariacao

    def setPorcentagemVariacao(self, porcentagemVariacao : float):
        self.__porcentagemVariacao = porcentagemVariacao

    def getVariacao(self):
        return self.__variacao

    def setVariacao(self, variacao : float):
        self.__variacao = variacao

    def getIdEmpresa(self):
        return self.__idEmpresa

    def setIdEmpresa(self, idEmpresa : int):
        self.__idEmpresa = idEmpresa
    
    def toString(self):
        return {
            "id": self.__id,
            "preco": self.__preco,
            "volume": self.__volume,
            "data": str(self.__data),
            "porcentagemVariacao": self.__porcentagemVariacao,
            "variacao": self.__variacao,
            "id_empresa": self.__idEmpresa
        }