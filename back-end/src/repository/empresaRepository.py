import asyncio
import asyncpg
from asyncpg.connection import Connection
from src.persistance import conexaoDB
from src.domain.empresa import Empresa
from src.domain.cotacao import Cotacao


async def findEmpresas():
    try:
        conexao = await conexaoDB.getConexao()
        query = list(await conexao.fetch(
            '''
                select e from empresa e order by e.classificacao;
            '''
        ))
        empresas: list = []
        for item in query:
            item = dict(item)
            if item is not None:
                empresa:Empresa = Empresa()
                #empresa
                e = dict(item['e'])
                empresa.setId(e['id'])
                empresa.setNome(e['nome'])
                empresa.setClassificacaoSetorial(e['classificao_setorial'])
                empresa.setEstado(e['estado'])
                empresa.setRamo(e['ramo'])
                empresa.setClassificacao(e['classificacao'])
                empresas.append(empresa)
        await conexao.close()
        return empresas
    except:
        print("Erro ao buscar empresas", str(exceptMsg))

async def findBySimbolo(simbolo: str):
    try:
        conexao = await conexaoDB.getConexao()
        
        query = await conexao.fetch(
            '''
                select e from empresa e where e.classificao_setorial = $1;
            ''',simbolo
        )
        empresa:Empresa = Empresa()
        for item in query:
            item = dict(item)
            if item is not None:
                #empresa
                e = dict(item['e'])
                empresa.setId(e['id'])
                empresa.setNome(e['nome'])
                empresa.setClassificacaoSetorial(e['classificao_setorial'])
                empresa.setEstado(e['estado'])
                empresa.setRamo(e['ramo'])
                empresa.setClassificacao(e['classificacao'])

        await conexao.close()
        return empresa
    except:
        print("Erro ao buscar empresa pelo simbolo = ",simbolo, str(exceptMsg))