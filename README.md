## Desenvolvimento de uma API para consultar valores da Bovespa

## Requisitos Computacionais

- Back-end

- [python 3.7]
- [Sanic Frameworkk]
- [Asyncpg]
- [Asyncio]
- [Requests]
- [PostgreSQL]

- Front-end

- [ReactJs]
- [PrimeReact (Sigma)]
- [Bootstrap]
- [Yarn]


## Execução

Para a execução da aplicação será necessário que o usuário tenha os requisitos computacionais devidamente instalados em seu computador

## BackEnd

Com os requisitos computacionais instalados basta executar o comando **python3 main.py** assim a API irá iniciar no endereço **http://127.0.0.1:8000/**


## Descrição dos EndPoints

Os endpoints da API desenvolvidas foram feitos utilizando o padrão Rest com o intuito de facilitar a utilização da API e assim tornar seu uso mais dinâmico e simples.

**Rotas de usuários**
- Rota POST, utilizada para efetuar login na aplicação, para isso é necessário passar no Body da requisição um JSON conforme a seguir:
```
/login 
{
    "email": Email_Usuario_Salvo,
    "senha": Senha_Usuario_Salvo
}
```
- Rota POST, utilizada para que seja possivel registrar um usuário, para isso é necessário passar no Body da requisição um JSON conforme a seguir:
```
/registra 

{
    "nome": Nome_Usuario,
    "email": Email_Usuario,
    "senha": Senha_Usuario
}
```

**Rotas de cotações**

- Rota GET, lista as 10 maiores empresas definidas pela Forbes em 2020, onde o Retorno é uma lista de empresas no formato a seguir:
```
/empresa 
[
    {
        "id": <VALOR>,
        "nome": <VALOR>,
        "classificao_setorial": <VALOR>,
        "ramo": <VALOR>,
        "classificacao": <VALOR>,
        "cotacao": <VALOR>
    }
]
```

- Rota GET, retorna o intraDay da empresa passada na rota, o retorno da API é um Json da seguinte forma:
```
/empresa/<simbolo>/intraday
[
    {
        "data": <VALOR> //Data - hora do dado retornado  
        "fechamento": <VALOR> //Valor do fechamento
    }
]
```

- Rota GET, retorna o valor da cotação da empresa passada na rota, o retorno da API é um Json da seguinte forma:
```
/empresa/<simbolo>/cotacao
[
    {
        "id": <Valor>,
        "nome": <Valor>,
        "classificao_setorial": <Valor>,
        "ramo": <Valor>,
        "classificacao": <Valor>,
        "cotacao": {
            "id": <Valor>,
            "preco": <Valor>,
            "volume": <Valor>,
            "data": <Valor>,
            "porcentagemVariacao": <Valor>,
            "variacao": <Valor>,
            "id_empresa": <Valor>
        }
    }
]
```