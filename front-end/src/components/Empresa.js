import React, { useState, useEffect, useRef } from 'react';
import { Toast } from 'primereact/toast';

import {EmpresaService} from '../service/EmpresaService'
import {InputText} from 'primereact/inputtext';
import { Button } from 'primereact/button';
import Chart from "react-google-charts";

import "./style.css"

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
    const [intraday, setIntraDay] = useState([]);
    
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
        onBuscaIntraDay(simbolo);
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
                setClassificacao(data.empresa.classificacao);
            }else{
                toast.current.show({ severity: 'error', summary: 'Falha ao buscar cotação: '+empresa,life: 3000 });
            }
        });
    };

    const onBuscaIntraDay = (simbolo) => {
    
        toast.current.show({ severity: 'info', summary: 'Buscando intraday: ' + simbolo,life: 2000 });
        empresaService.getIntraday(simbolo).then(data => {
            if(data.intraday){
                let intraAux = []
                let aux = ['Data/Hora','Valor Fechamento'];
                intraAux.push(aux);
                data.intraday.map((item) => {
                    aux = [item.data,parseFloat(item.fechamento)];
                    intraAux.push(aux);
                });
                setIntraDay(intraAux);
            
            }else{
                toast.current.show({ severity: 'error', summary: 'Falha ao buscar intraday: '+empresa,life: 3000 });
            }
        });
    };

    return (
        <>
            <Toast ref={toast} />
            <div className="card">
                <h1>10 Maiores empresas segundo Forbes</h1>
                <div className="p-grid p-fluid p-dir-row">
                    {
                    empresas.map((emp) => {
                        return (
                            <div className="p-field p-col-12 p-md-2" key = {emp.id}>
                                    <Button key = {emp.id} label={emp.classificao_setorial} value={emp.classificao_setorial} className="p-mr-2 p-mb-2 btn" onClick={() => onEmpresaSelect(emp.classificao_setorial)}></Button>
                            </div>
                        );
                    })}
                    
                </div>
                
            </div>
        
            { nome !== "" &&
                <div className="card">
                    <h1>Empresa Selecionada: {nome}, Classificação: {classificacao}</h1>
                    <div className="p-grid p-fluid p-dir-row">
                        <div className="p-field p-col-12 p-md-3">
                                <label htmlFor="firstname1">Empresa</label>
                                <InputText id="firstname1" type="text"  value={nome} readOnly={true}/>
                        </div>
                        <div className="p-field p-col-12 p-md-3">
                                <label htmlFor="firstname1">Símbolo Bolsa</label>
                                <InputText id="firstname1" type="text"  value={classificao_setorial} readOnly={true}/>
                        </div>
                        <div className="p-field p-col-12 p-md-6 ">
                                <label htmlFor="lastname1">Ramo</label>
                                <InputText id="lastname1" type="text"  value={ramo} readOnly={true}/>
                        </div>
                    </div>
                    <div className="p-grid p-fluid p-dir-row">
                        <div className="p-field p-col-12 p-md-3">
                                <label htmlFor="firstname1">Preço</label>
                                <InputText id="firstname1" type="text"  value={preco} readOnly={true}/>
                        </div>
                        <div className="p-field p-col-12 p-md-3">
                                <label htmlFor="firstname1">Volume</label>
                                <InputText id="firstname1" type="text" value={volume} readOnly={true}/>
                        </div>
                        <div className="p-field p-col-12 p-md-3">
                                <label htmlFor="lastname1">Variação</label>
                                <InputText id="lastname1" type="text" value={variacao} readOnly={true}/>
                        </div>
                        <div className="p-field p-col-12 p-md-3">
                                <label htmlFor="lastname1">Porcentagem Variação</label>
                                <InputText id="lastname1" type="text" value={porcentagemVariacao} readOnly={true}/>
                        </div>
                    </div>
                    <Chart
                        width={'100%'}
                        height={'100vh'}
                        chartType="AreaChart"
                        loader={<div>Carregando</div>}
                        data={intraday}
                        options={{
                        title: 'Intra Day',
                        hAxis: { title: 'Year', titleTextStyle: { color: '#333' } },
                        vAxis: { minValue: 0 },
                        // For the legend to fit, we make the chart area smaller
                        chartArea: { width: '50%', height: '70%' },
                        // lineWidth: 25
                        }}
                    />
                </div>
            }
        </>
    );
}
