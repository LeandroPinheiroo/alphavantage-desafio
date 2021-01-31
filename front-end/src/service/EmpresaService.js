import axios from 'axios'

export class EmpresaService {

    getEmpresas() {
        return axios.get('http://127.0.0.1:8000/empresa/')
        .then(res => res.data);
    }

    getCotacao(sigla) {
        return axios.get('http://127.0.0.1:8000/empresa/'+sigla+'/cotacao')
        .then(res => res.data)
        .catch(() => "erro");
    }

    getIntraday(sigla) {
        return axios.get('http://127.0.0.1:8000/empresa/'+sigla+'/intraday')
        .then(res => res.data)
        .catch(() => "erro");
    }
}