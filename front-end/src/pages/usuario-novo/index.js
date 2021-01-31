import React,{useState,useRef} from 'react';
import {useDispatch} from 'react-redux';

import { Toast } from 'primereact/toast';

import './usuario-novo.css';
import logo from '../../images/ponto-tel.png';
import { Redirect } from 'react-router-dom';
import { UsuarioService } from '../../service/UsuarioService';



export const Registrar = () => {

    const toast = useRef(null);
    const [nome, setNome] = useState('');
    const [email, setEmail] = useState('');
    const [senha, setSenha] = useState('');
    const [carregando, setCarregando] = useState(false);
    const [showSpinner, setShowSpinner] = useState(false);
    
    const dispatch = useDispatch();

    const usuarioService = new UsuarioService();

    function handleNewUser() {
        if(!email || !senha || !nome || email === '' || senha ==='' || nome ===''){
            toast.current.show({ severity: 'error', summary: 'Preencha todos os campos',life: 2000 });
            return;
        }

        setCarregando(true);

        usuarioService.regisrar(email,senha,nome).then(data => {
            dispatch({
                type:'LOG_IN',
                payload:{
                    usuarioEmail:email
                }
            });
            setShowSpinner(false)
            return <Redirect to="/" />;
        }).catch(erro => {
            toast.current.show({ severity: 'error', summary: 'Erro ao se cadastrar'+erro,life: 2000 });
            setShowSpinner(false)
        });
        
        
        
    }

    const Spinner = () => (
        <div className="spinner-border text-primary" role="status">
            <span className="sr-only">Loading...</span>
        </div>
    )

    return (
        <>
            <Toast ref={toast} />
            <div className="cadastro-content d-flex align-items-center text-center">
                <form className="form-signin mx-auto">
                    <img className="mb-4" src={logo}  width="72" height="72" alt=""></img>
                    <h3 className="h3 mb-3 font-weight-bold text-white"> Cadastro de Usuário</h3>
                    <div className="mb-3">
                        <input type="text" className="form-control" id="inputNome" placeholder="Nome"
                            onChange={e => setNome(e.target.value)}/>
                    </div>
                    <div className="mb-3">
                        <input type="email" className="form-control" id="inputEmail" placeholder="E-mail"
                            onChange={e => setEmail(e.target.value)}/>
                    </div>
                    <div className="mb-3">
                        <input type="password" className="form-control" id="inputPassowrd" placeholder="Senha"
                            onChange={e => setSenha(e.target.value)}/>
                    </div>
                    <div className="mb-3">
                        {
                            carregando ?
                                <div className="spinner-border text-danger" role="status">
                                    <span className="sr-only"></span>
                                </div>
                            :
                                <button type="button" className="btn btn-lg btn-cadastro btn-block" onClick={handleNewUser}>Cadastrar</button>
                        }
                    </div>
                    { showSpinner ? <Spinner /> : null }
                </form>
                
            </div>
        </>
    
    );
}