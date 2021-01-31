import axios from 'axios'

export class UsuarioService {

    login(email,senha) {
        return axios.post('http://127.0.0.1:8000/login/',{
            email: email,
            senha: senha
          })
        .then(res => res.data);
    }

    regisrar(email,senha,nome) {
        return axios.post('http://127.0.0.1:8000/registra/',{
            email: email,
            senha: senha,
            nome: nome
          })
        .then(res => res.data);
    }

}