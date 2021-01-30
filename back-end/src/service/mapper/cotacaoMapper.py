from src.domain.cotacao import Cotacao

class CotacaoMapper:

    def toCotacao(json:dict):
        cotacao:Cotacao = Cotacao()
        cotacao.setPreco(float(json["05. price"]))
        cotacao.setVolume(int(json["06. volume"])) 
        cotacao.setVariacao(float(json["09. change"]))
        cotacao.setPorcentagemVariacao(json["10. change percent"])
        cotacao.setData()
        return cotacao