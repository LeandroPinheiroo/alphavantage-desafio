import axios from 'axios'

export class EmpresaService {

    getEmpresas() {
        return axios.get('http://127.0.0.1:8000/empresa/')
        .then(res => res.data);
    }
}