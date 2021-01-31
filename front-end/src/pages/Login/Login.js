import React,{useState,useRef} from 'react';
import { Link, Redirect} from 'react-router-dom';
import {useSelector, useDispatch} from 'react-redux';
import { Toast } from 'primereact/toast';

import './Login.css';
import logo from '../../images/ponto-tel.png';
import { UsuarioService } from '../../service/UsuarioService';



export const Login = () => {
    
    const toast = useRef(null);
    const [email, setEmail] = useState('');
    const [senha, setSenha] = useState('');

    const dispatch = useDispatch();
    const [showSpinner, setShowSpinner] = useState(false);

    const usuarioService = new UsuarioService();

    const Spinner = () => (
        <div className="spinner-border text-primary" role="status">
            <span className="sr-only">Loading...</span>
        </div>
    )


    function handleLogin() {
        setShowSpinner(true)
        usuarioService.login(email,senha).then(data => {
            dispatch({
                type:'LOG_IN',
                payload:{
                    usuarioEmail:email
                }
            })
            setShowSpinner(false)
        }).catch(erro => {
            toast.current.show({ severity: 'error', summary: 'Verifique suas credenciais',life: 2000 });
            setShowSpinner(false)
        });
       
    }

    return (
        <>
            <Toast ref={toast} />
            <div className="login-content d-flex align-items-center text-center">
                {useSelector(state => state.user.usuarioLogado) === 1 ? <Redirect to="/"></Redirect> : null}
                <form className="form-signin mx-auto">
                    <img className="mb-4" src={logo}  width="72" height="72" alt=""></img>
                    <h3 className="h3 mb-3 font-weight-bold text-white"> Login</h3>

                    <div className="mb-3">
                        <input type="email" className="form-control" id="inputEmail" aria-describedby="emailHelp" placeholder="E-mail"
                            onChange={e => setEmail(e.target.value)}/>
                        <div id="emailHelp" className="form-text text-white">Não compartilhe seu E-mail com ninguém</div>
                    </div>
                    <div className="mb-3">
                        <input type="password" className="form-control" id="inputPassowrd" placeholder="Senha"
                            onChange={e => setSenha(e.target.value)}/>
                    </div>
                    <div className="mb-3">
                        <button type="button" className="btn btn-lg btn-login btn-block" onClick={handleLogin}>Entrar</button>
                    </div>
                    <div className="opcoes-login text-white my-5">
                        <Link to = "/registrar" className="mx-2">Quero me cadastrar</Link>
                    </div>
                    { showSpinner ? <Spinner /> : null }
                </form>
                
            </div>
        </>
    
    );
}

