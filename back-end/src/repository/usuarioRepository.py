import asyncio
import asyncpg
from asyncpg.connection import Connection
from src.persistance import conexaoDB
from src.domain.usuario import Usuario

async def insert(usuario : Usuario):
    conexao = await conexaoDB.getConexao()
    
    async with conexao.transaction():
        await conexao.execute('''
            INSERT INTO usuario (nome,email,senha) VALUES($1, $2, $3)
            ''',
            usuario.getNome(),
            usuario.getEmail(),
            usuario.getSenha()
        )
    await conexao.close()

async def findByEmail(email: str):
    conexao = await conexaoDB.getConexao()
    
    query = await conexao.fetch(
        '''
            select u from usuario u where u.email = $1;
        ''',
        email
    )
    usuario: Usuario = Usuario()
    
    if len(query) > 0:
        query = dict(query[0])
        u = dict(query['u'])
        usuario.setId(u['id'])
        usuario.setEmail(u['email'])
        usuario.setNome(u['nome'])
        usuario.setSenha(u['senha'])

    return usuario

    await conexao.close()