from sanic import Sanic
from sanic.response import json
from sanic_cors import CORS, cross_origin
import asyncio
import asyncpg
import aiohttp
import requests
from marshmallow import Schema, fields, ValidationError, EXCLUDE

from src.domain.usuario import Usuario
from src.service import usuarioService
from src.service.mapper.usuarioMapper import UsuarioMapper
from src.domain.empresa import Empresa
from src.service import empresaService
from src.repository import empresaRepository
from src.util.intervaloBovespa import tempo
from src.util import dbUtil


app = Sanic(__name__)
CORS(app)

#Rotas de empresa 
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
    try :
        empresa: Empresa = await empresaService.buscaCotacao(simbolo)
        if(empresa is None):
            return json({"erros": "Simbolo inválido "+simbolo},status=400)
        return json(
            {"empresa" : empresa.toString()},
            status = 200
        )
    except Exception as exceptMsg:
        return json(
            {"erros": str(exceptMsg)},
            status=400
        )

#Rotas de usuario
@app.route("/login", methods=["POST"])
async def login(request):
    try:
        usuario:Usuario = UsuarioMapper.toLogin(request.json)
        print(usuario.toString)
        usuarioLogin:Usuario = await usuarioService.login(usuario.getEmail(),usuario.getSenha())
        if usuarioLogin is None:
            return json({"erros": "Credenciais Inválidas "},status=400)
        return json(
            {"usuario" : usuarioLogin.toString()}, 
            status = 200,
        )
    except Exception as exceptMsg:
        return json(
                {"erro" : str(exceptMsg)}, 
                status = 400,
        )

@app.route("/registra", methods=["POST"])
async def login(request):
    try:
        usuarioSalvo:Usuario = await usuarioService.registra(UsuarioMapper.toUsuario(request.json))
        if usuarioSalvo is None:
            return json({"erros": "E-mail já utilizado"},status=400)
        return json(
            {"usuario" : usuarioSalvo.toString()}, 
            status = 200,
        )
    except Exception as exceptMsg:
        return json(
                {"erro" : str(exceptMsg)}, 
                status = 400,
        )


def criaAplicacao():
    return app