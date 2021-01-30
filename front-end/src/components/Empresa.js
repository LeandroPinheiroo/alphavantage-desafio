import React, { useState, useEffect, useRef } from 'react';
import { Toast } from 'primereact/toast';

import {EmpresaService} from '../service/EmpresaService'
import { Dropdown } from 'primereact/dropdown';
import {InputText} from 'primereact/inputtext';
import { Button } from 'primereact/button';

export const Empresa = () => {

    const toast = useRef(null);
    const [empresas, setEmpresas] = useState([]);
    const [nome, setNome] = useState("");
    const [classificao_setorial, setClassificao_setorial] = useState("");
    const [ramo, setRamo] = useState("");
    const [preco, setPreco] = useState("");
    const [volume, setVolume] = useState("");
    const [variacao, setVariacao] = useState("");
    const [porcentagemVariacao, setPorcentagemVariacao] = useState("");
    const [classificacao, setClassificacao] = useState("");

    
    const [empresa, setEmpresa] = useState(null);

    const empresaService = new EmpresaService();

    useEffect(() => {
        toast.current.show({ severity: 'info', summary: 'Buscando Empresas',life: 1000 });
        empresaService.getEmpresas().then(data => {
            setEmpresas(data.empresas);
            toast.current.show({ severity: 'success', summary: 'Empresas buscadas',life: 3000 });
        });

    }, []);

    const onEmpresaSelect = (simbolo) => {
        setEmpresa(simbolo);
        onBuscaCotacao(simbolo);
    };

    const onBuscaCotacao = (simbolo) => {
    
        toast.current.show({ severity: 'info', summary: 'Buscando Cotacao: ' + simbolo,life: 2000 });
        empresaService.getCotacao(simbolo).then(data => {
            if(data.empresa){
                setNome(data.empresa.nome);
                setClassificao_setorial(data.empresa.classificao_setorial);
                setRamo(data.empresa.ramo);
                setPreco("R$"+data.empresa.cotacao.preco);
                setVolume(data.empresa.cotacao.volume);
                setVariacao(data.empresa.cotacao.variacao);
                setPorcentagemVariacao(data.empresa.cotacao.porcentagemVariacao);
            }else{
                toast.current.show({ severity: 'error', summary: 'Falha ao buscar cotação: '+simbolo,life: 3000 });
            }
        });
    };

    return (
        <>
            <Toast ref={toast} />
            <div className="card">
                <h1>Top 10 Empresas</h1>
                <div className="p-grid p-fluid p-dir-row">
                    {
                    empresas.map((emp) => {
                        return (
                            <div className="p-field p-col-2" key = {emp.id}>
                                    <Button key = {emp.id} label={emp.classificao_setorial} value={emp.classificao_setorial} className="p-mr-2 p-mb-2" onClick={() => onEmpresaSelect(emp.classificao_setorial)}></Button>
                            </div>
                        );
                    })}
                    
                </div>
                
            </div>
        
            { empresa !== null &&<div className="card">
                <h1>Empresa Selecionada: {nome}</h1>
                <div className="p-grid p-fluid p-dir-row">
                    <div className="p-field p-col-3">
                            <label htmlFor="firstname1">Empresa</label>
                            <InputText id="firstname1" type="text"  value={nome} readOnly={true}/>
                    </div>
                    <div className="p-field p-col-3">
                            <label htmlFor="firstname1">Símbolo Bolsa</label>
                            <InputText id="firstname1" type="text"  value={classificao_setorial} readOnly={true}/>
                    </div>
                    <div className="p-field p-col-6">
                            <label htmlFor="lastname1">Ramo</label>
                            <InputText id="lastname1" type="text"  value={ramo} readOnly={true}/>
                    </div>
                </div>
                <div className="p-grid p-fluid p-dir-row">
                    <div className="p-field p-col-3">
                            <label htmlFor="firstname1">Preço</label>
                            <InputText id="firstname1" type="text"  value={preco} readOnly={true}/>
                    </div>
                    <div className="p-field p-col-3">
                            <label htmlFor="firstname1">Volume</label>
                            <InputText id="firstname1" type="text" value={volume} readOnly={true}/>
                    </div>
                    <div className="p-field p-col-3">
                            <label htmlFor="lastname1">Variação</label>
                            <InputText id="lastname1" type="text" value={variacao} readOnly={true}/>
                    </div>
                    <div className="p-field p-col-3">
                            <label htmlFor="lastname1">Porcentagem Variação</label>
                            <InputText id="lastname1" type="text" value={porcentagemVariacao} readOnly={true}/>
                    </div>
                </div>
            </div>}
        </>
    );
}
