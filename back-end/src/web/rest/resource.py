from sanic import Sanic
from sanic.response import json
from sanic_cors import CORS, cross_origin
import asyncio
import asyncpg
import aiohttp
import requests
from marshmallow import Schema, fields, ValidationError, EXCLUDE

from src.service import empresaService
from src.repository import empresaRepository
from src.util.intervaloBovespa import tempo
from src.util import dbUtil


app = Sanic(__name__)
CORS(app)

@app.route("/empresa", methods=["GET"])
async def buscaEmpresas(request):
    try:
        empresas = await empresaService.buscaEmpresas()
        return json(
            {"empresas" : [empresa.toString() for empresa in empresas]}, 
            status = 200,
        )
    except Exception as exceptMsg:
        return json(
                {"erro" : str(exceptMsg)}, 
                status = 400,
        )

@app.route("/empresa/<simbolo>/cotacao", methods=["GET"])
async def buscaCotacao(request, simbolo : str):
    empresa = await empresaService.buscaCotacao(simbolo)
    if(empresa is None):
        return json({"erros": "Simbolo inválido "+simbolo},status=400)
    try :
        return json(
            {"empresa" : empresa.toString()},
            status = 200
        )
    except Exception as exceptMsg:
        return json(
            {"erros": str(exceptMsg)},
            status=400
        )

def criaAplicacao():
    return app