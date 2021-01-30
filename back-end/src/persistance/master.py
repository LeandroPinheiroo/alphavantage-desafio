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
                    senha character varying(255) NOT NULL
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
                (1, "SID NACIONAL", "CSNA3.SA", "Siderúrgica", 10),
                (2, "WEG", "WEGE3.SA", "Eletrônicos", 9),
                (3, "PETRORIO", "PRIO3.SA", "Petróleoa", 8),
                (4, "MAGAZINE LUIZA", "MGLU3.SA", "Varejo", 7),
                (5, "BRADESPAR", "BRAP4.SA", "Financeiro e Outros", 6),
                (6, "VALE", "VALE3.SA", "Mineração", 5),
                (7, "USIMINAS", "USIM5.SA", "Mineração, Siderúrgica", 4),
                (8, "B3", "B3SA3.SA", "Financeiro", 3),
                (9, "SUZANO PAPEL", "SUZB3.SA", "Papel; ‎Celulose", 2),
                (10, "LOCALIZA", "RENT3.SA", "Automóveis", 1)
        ])
