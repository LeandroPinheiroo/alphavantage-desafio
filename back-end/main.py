import asyncio
from src.persistance import master
from src.util import dbUtil
from src.web.rest import resource as aplicacao

if __name__ == "__main__":
    if asyncio.run(master.init()):
        print("Pronto para iniciar")
        app = aplicacao.criaAplicacao()
        host = dbUtil.getHostAplicacao()
        port = dbUtil.getPortoAplicacao()
        app.run(host=host, debug=False, port=port)
    else:
        print("Ocorreu um erro ao criar o BD.")