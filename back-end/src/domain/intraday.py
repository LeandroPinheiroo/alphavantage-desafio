class Intraday:

    def __init__(self, data:str = None,fechamento:float = None):
        self.__data = data
        self.__fechamento = fechamento

       
    def getData(self):
        return self.__data

    def setData(self, data : int):
        self.__data = data

    def getFechamento(self):
        return self.__fechamento

    def setFechamento(self, fechamento : float):
        self.__fechamento = fechamento
    
    
    def toString(self):
        return {
            "data": self.__data,
            "fechamento": self.__fechamento
        }