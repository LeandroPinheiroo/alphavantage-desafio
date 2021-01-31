import asyncio
import asyncpg
from asyncpg.connection import Connection
from src.persistance import conexaoDB

async def init():
    print("Criando Banco de Dados.")
    try:
        conexao = await conexaoDB.getConexao()
        await tabelaUsuario(conexao)
        await tabelaEmpresa(conexao)
        await tabelaCotacao(conexao)
        empresasSalvas = await findQuantidadeEmpresas(conexao)
        if(empresasSalvas < 10):
            print("Inserindo maiores empresas brasileiras")
            await insertEmpresas(conexao)
        await conexao.close()
        print("Banco de dados criado!")
        return True
    except Exception as exceptMsg:
        print(str(exceptMsg))
        return False

async def tabelaUsuario(conexao : Connection):
    async with conexao.transaction():
        await conexao.execute(
            '''
                CREATE TABLE IF NOT EXISTS usuario(
                    id SERIAL PRIMARY KEY NOT NULL UNIQUE,
                    email character varying(150) NOT NULL,
                    senha character varying(255) NOT NULL,
                    nome character varying(150) NOT NULL
                )
            '''
        )

async def tabelaEmpresa(conexao : Connection):
    async with conexao.transaction():
        await conexao.execute(
            '''
                CREATE TABLE IF NOT EXISTS empresa(
                    id SERIAL PRIMARY KEY NOT NULL UNIQUE,
                    nome character varying(150) NOT NULL,
                    classificao_setorial character varying(10) NOT NULL,
                    ramo character varying(70),
                    classificacao int
                )
            '''
        )

async def tabelaCotacao(conexao : Connection):
    async with conexao.transaction():
        await conexao.execute(
            '''
                CREATE TABLE IF NOT EXISTS cotacao(
                    id SERIAL PRIMARY KEY NOT NULL UNIQUE,
                    preco float(4),
                    volume bigint,
                    data timestamp without time zone,
                    porcentagem_variacao character varying(10),
                    variacao float(3),
                    id_empresa bigint NOT NULL,
                    CONSTRAINT cotacao_fk FOREIGN KEY(id_empresa) REFERENCES empresa(id) ON DELETE CASCADE
                )
            '''
        )

async def findQuantidadeEmpresas(conexao : Connection):
    quantidade : int = await conexao.fetchval('''
        SELECT COUNT(*) from empresa
        '''
    )
    return quantidade

async def insertEmpresas(conexao : Connection):
    async with conexao.transaction():
        #apaga as empresas salvas na base
        await conexao.execute('''
            delete from empresa
            '''
        )
        
        await conexao.copy_records_to_table(
            "empresa", records = [
                (1, "Petrobras", "PBR", "Petróleo", 1),
                (2, "Itaú Unibanco Holding S.A", "ITUB", "Banco", 2),
                (3, "Banco Bradesco S.A", "BBD", "Banco", 3),
                (4, "JBS", "JBSS", "Carnes", 4),
                (5, "VALE", "VALE", "Mineração", 5),
                (6, "Suzano S.A", "SUZ", "Papel; ‎Celulose", 6),
                (7, "Braskem", "BAK", "Resinas termoplásticas", 7),
                (8, "CEMIG", "CIG", "Energia", 8),
                (9, "Ultrapar Participações", "UGP", "Pacombustíveis", 9),
                (10, "Companhia Brasileira de Distribuicao", "CBD", "Varejo", 10)
        ])
