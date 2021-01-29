import configparser

def getHostAplicacao():
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config["application"]["host"]

def getPortoAplicacao():
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config["application"]["porto"]

def getChaveAplicacao():
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config["api"]["chave"]

def getDB():
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config["database"]["localizacao"]

def getDBUsuario():
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config["database"]["usuario"]

def getDBEsquema():
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config["database"]["nome"]

def getDBSenha():
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config["database"]["senha"]
