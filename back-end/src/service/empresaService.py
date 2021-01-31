import asyncio
import asyncpg
from sanic.response import json
import requests
from src.repository import empresaRepository
from src.repository import cotacaoRepository
from src.service.mapper.cotacaoMapper import CotacaoMapper
from src.service.mapper.intradayMapper import IntradayMapper
from src.util import dbUtil

async def buscaEmpresas():
    empresas = await empresaRepository.findEmpresas()
    return empresas

async def buscaIntraDay(simbolo: str):
    empresa = await empresaRepository.findBySimbolo(simbolo)
    if(empresa.getId() is None):
        return None

    parameters: str = ""
    timeSeries: str = "TIME_SERIES_INTRADAY" 
    simbolo: str = simbolo 
    interval: str = '1min'
    chave: str = dbUtil.getChaveAplicacao()
   
    
    parameters = "function=" + timeSeries
    parameters += "&symbol=" + simbolo
    parameters += "&interval=" + interval
    parameters += "&apikey=" + chave
    try:
        response = requests.get('https://www.alphavantage.co/query?' + parameters)
        jsonResponse : dict = response.json() 
        intradayList = IntradayMapper.toIntradayList(jsonResponse["Time Series (1min)"])
        return intradayList
    except:
        return None

async def buscaCotacao(simbolo: str):
    empresa = await empresaRepository.findBySimbolo(simbolo)
    if(empresa.getId() is None):
        return None

    parameters: str = ""
    globalQuote: str = "GLOBAL_QUOTE" 
    simbolo: str = simbolo 
    chave: str = dbUtil.getChaveAplicacao()
   
    
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
    