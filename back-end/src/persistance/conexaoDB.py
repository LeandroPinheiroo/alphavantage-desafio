import asyncpg
from asyncpg.connection import Connection
from src.util import dbUtil

async def getConexao():
    try:
        configuracaoDB = await asyncpg.connect('postgresql://' + dbUtil.getDBUsuario() + "@" + dbUtil.getDB() + "/" + dbUtil.getDBEsquema(), password=dbUtil.getDBSenha())
        return configuracaoDB
    except Exception as e:
        print("Erro ao conectar com o DB: "+str(e))
        raise Exception