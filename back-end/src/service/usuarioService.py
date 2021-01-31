import asyncio
import asyncpg
from sanic.response import json
import requests
from src.repository import usuarioRepository
from src.domain.usuario import Usuario
from src.util import dbUtil
import bcrypt

async def buscaUsuarioEmail(email:str):
    return await usuarioRepository.findByEmail(email)

async def login(email:str, senha:str):
    usuario: Usuario = await buscaUsuarioEmail(email)
    if usuario.getId() is None:
        return None
    if bcrypt.checkpw(senha.encode('utf8'), usuario.getSenha().encode('utf8')):
        return usuario
    return None

async def registra(usuario: Usuario):
    usuarioSalvo:Usuario = await buscaUsuarioEmail(usuario.getEmail())
    print(usuario.getId())
    if(usuarioSalvo.getId() is not None):
        return None
    senhaCript = bcrypt.hashpw(usuario.getSenha().encode('utf8'), bcrypt.gensalt())
    usuario.setSenha(str(senhaCript.decode("utf-8")))
    await usuarioRepository.insert(usuario)
    return usuario