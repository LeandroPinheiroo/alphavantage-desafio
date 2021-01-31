from src.domain.usuario import Usuario

class UsuarioMapper:

    def toUsuario(json:dict):
        usuario:Usuario = Usuario()
        usuario.setNome(json['nome'])
        usuario.setEmail(json['email'])
        usuario.setSenha(json['senha'])
        return usuario
    
    def toLogin(json:dict):
        usuario:Usuario = Usuario()
        usuario.setEmail(json['email'])
        usuario.setSenha(json['senha'])
        return usuario