import datetime

class Empresa:

    def __init__(self, id: int = None, preco: float = None , volume: int = None , data: datetime = None , porcentagemVariacao: float = None, variacao: float = None , id_empresa: int = None):
        self.__id = id
        self.__preco = preco
        self.__volume = volume
        self.__data = data
        self.__porcentagemVariacao = porcentagemVariacao
        self.__variacao = variacao
        self.__id_empresa = id_empresa

       
    def getId(self):
        return self.__id

    def setId(self, id : str):
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

    def getVaiacao(self):
        return self.__vairacao

    def setVaiacao(self, vairacao : float):
        self.__vairacao = vairacao

    def getIdEmpresa(self):
        return self.__idEmpresa

    def setIdEmpresa(self, idEmpresa : int):
        self.__idEmpresa = idEmpresa
    
    def toString(self):
        return {
            "id": self.__id,
            "preco": self.__preco,
            "volume": self.__volume,
            "data": self.__data,
            "porcentagemVariacao": self.__porcentagemVariacao,
            "variacao": self.__variacao,
            "id_empresa": self.__id_empresa
        }