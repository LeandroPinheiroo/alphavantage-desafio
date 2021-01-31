from src.domain.intraday import Intraday

class IntradayMapper:

    def toIntradayList(json:dict,):
        intradayList: list = list()
        for key in json:
            intraday: Intraday = Intraday()
            intraday.setData(key)
            intraday.setFechamento(json[key]['4. close'])
            intradayList.append(intraday)
        return intradayList