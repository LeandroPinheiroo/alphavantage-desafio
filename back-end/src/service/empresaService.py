import asyncio
import asyncpg
from sanic.response import json
import requests
from src.repository import empresaRepository
from src.repository import cotacaoRepository
from src.service.mapper.cotacaoMapper import CotacaoMapper
from src.util import dbUtil

async def buscaEmpresas():
    empresas = await empresaRepository.findEmpresas()
    return empresas

async def buscaCotacao(simbolo: str):
    empresa = await empresaRepository.findBySimbolo(simbolo)
    if(empresa.getId() is None):
        return None

    parameters: str = ""
    globalQuote: str = "GLOBAL_QUOTE" #parâmetro para cotação de uma empresa pelo alpha vantage
    simbolo: str = simbolo #símbolo da empresa a ser consultada
    chave: str = dbUtil.getChaveAplicacao()
   
    
    #montando url para chamar a api do alpha vantage
    parameters = "function=" + globalQuote
    parameters += "&symbol=" + simbolo
    parameters += "&apikey=" + chave
    try:
        response = requests.get('https://www.alphavantage.co/query?' + parameters)
        jsonResponse : dict = response.json() #em python, ao desserializar o json do response o objeto é do tipo dict
        cotacao = CotacaoMapper.toCotacao(jsonResponse["Global Quote"])
        cotacao.setIdEmpresa(empresa.getId())
        await cotacaoRepository.insert(cotacao)
        empresa.setCotacao(cotacao)
        return empresa
    except:
        return None
    