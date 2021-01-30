import asyncio
import asyncpg
from asyncpg.connection import Connection
from src.persistance import conexaoDB
from src.domain.cotacao import Cotacao


async def findByEmpresaId(empresaId : int):
    try:
        conexao = await conexaoDB.getConexao()
        
        query = await conexao.fetch(
            '''
                select c from cotacao c where c.id_empresa = $1;
            ''',empresaId
        )
        
        cotacao:Cotacao = Cotacao()
        for item in query:
            item = dict(item)
            if item is not None:
                #cotacao
                c = dict(item['c'])
                cotacao.setId(int(c['id']))
                cotacao.setPreco(c['preco'])
                cotacao.setVolume(c['volume'])
                cotacao.setData(c['data'])
                cotacao.setPorcentagemVariacao(c['porcentagem_variacao'])
                cotacao.setVariacao(c['variacao'])
                cotacao.setIdEmpresa(c['id_empresa'])

        await conexao.close()
        return cotacao
    except exceptMsg:
        print("Erro ao buscar cotacao pela empresa de id = ",empresaId)

async def insert(cotacao : Cotacao):
    cotacaoSalva = await findByEmpresaId(cotacao.getIdEmpresa())
    conexao = await conexaoDB.getConexao()
    if cotacaoSalva.getId() is None:
        async with conexao.transaction():
            await conexao.execute('''INSERT INTO cotacao (preco,volume,porcentagem_variacao,variacao,id_empresa) VALUES($1, $2, $3, $4, $5)''',
                cotacao.getPreco(),
                cotacao.getVolume(),
                cotacao.getPorcentagemVariacao(),
                cotacao.getVariacao(),
                cotacao.getIdEmpresa()
            )
    else:
        async with conexao.transaction():
            await conexao.execute('''UPDATE cotacao SET preco = $1, volume = $2, porcentagem_variacao = $3, variacao = $4, id_empresa = $5 WHERE id = $6''',
                cotacao.getPreco(),
                cotacao.getVolume(),
                cotacao.getPorcentagemVariacao(),
                cotacao.getVariacao(),
                cotacao.getIdEmpresa(),
                cotacao.getId()
            )
    await conexao.close()