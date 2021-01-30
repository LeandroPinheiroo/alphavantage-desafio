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
                    id bigint PRIMARY KEY NOT NULL UNIQUE,
                    email character varying(150) NOT NULL,
                    senha character varying(255) NOT NULL
                )
            '''
        )

async def tabelaEmpresa(conexao : Connection):
    async with conexao.transaction():
        await conexao.execute(
            '''
                CREATE TABLE IF NOT EXISTS empresa(
                    id bigint PRIMARY KEY NOT NULL UNIQUE,
                    nome character varying(150) NOT NULL,
                    classificao_setorial character varying(10) NOT NULL,
                    estado character varying(150),
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
                (1, "Oi", "OIBR-C", "Rio de Janeiro, Rio de Janeiro", "Telecomunicações", 10),
                (2, "Braskem", "BRKM5.SAO", "São Paulo, São Paulo", "Petroquímica", 9),
                (3, "Itaúsa", "ITSA4.SAO", "Brasil", "Finanças e indústria", 8),
                (4, "JBS", "JBSS3.SAO", "São Paulo, São Paulo", "Alimentício", 7),
                (5, "Eletrobras", "ELET6.SAO", "Rio de Janeiro, Rio de Janeiro", "Energia elétrica", 6),
                (6, "Banco do Brasil", "BBAS3.SAO", "Brasília, Distrito Federal", "Bancário", 5),
                (7, "Vale", "VALE3.SAO", "Rio de Janeiro, Rio de Janeiro", "Mineração", 4),
                (8, "Banco Bradesco", "BBDC4.SAO", "Osasco, São Paulo", "Bancário", 3),
                (9, "Itaú Unibanco", "ITUB4.SAO", "São Paulo, São Paulo", "Bancário", 2),
                (10, "Petrobras", "PETR4.SAO", "Rio de Janeiro, Rio de Janeiro", "Petróleo e gás", 1)
        ])
