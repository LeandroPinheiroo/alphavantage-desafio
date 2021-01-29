import asyncio
from src.persistance import master
from src.util import dbUtil

if __name__ == "__main__":
    if asyncio.run(master.init()):
        print("Pronto para iniciar")
    else:
        print("Ocorreu um erro ao criar o BD.")