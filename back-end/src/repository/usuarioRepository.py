import asyncio
import asyncpg
from asyncpg.connection import Connection
from src.persistance import conexaoDB
from src.domain.usuario import Usuario

async def insert(usuario : Usuario):
    conexao = await conexaoDB.getConexao()
    
    async with conexao.transaction():
        await conexao.execute('''
            INSERT INTO usuario VALUES($1, $2)
            ''',
            usuario.getNome,
            usuario.getSenha
        )
    await conexao.close()

async def findByNomeSenha(nome: str, senha: str):
    conexao = await conexaoDB.getConexao()
    
    query = await conexao.fetch(
        '''
            select u from usuario u where u.nome = $1 and u.senha = $2;
        ''',
        nome,
        senha
    )
    usuario = Usuario()
    query = dict(query)
    if query is not None:
        usuario.setId = query['id']
        usuario.setNome = query['nome']
        usuario.setSenha = query['senha']

    await conexao.close()