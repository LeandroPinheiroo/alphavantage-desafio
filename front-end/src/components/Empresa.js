import React, { useState, useEffect, useRef } from 'react';
import { Toast } from 'primereact/toast';

import {EmpresaService} from '../service/EmpresaService'
import { Dropdown } from 'primereact/dropdown';
import { Column } from 'primereact/column';

export const Empresa = () => {

    const toast = useRef(null);
    const [empresas, setEmpresas] = useState(null);
    
    const [empresa, setEmpresa] = useState(null);

    useEffect(() => {
        const empresaService = new EmpresaService();
        empresaService.getEmpresas().then(data => {
            setEmpresas(data.empresas);
            toast.current.show({ severity: 'success', summary: 'Empresas buscadas',life: 3000 });
        });

    }, []);

    const onEmpresaSelect = (e) => {
        setEmpresa(e.classificao_setorial);
    };
   
    const templateEmpresas = (option) => {
        
        return (
            <div >
                <span>{option.nome} - {option.classificao_setorial}</span>
            </div>
        );
        
    };

    return (
        <>
            <Toast ref={toast} />
            <div className="p-grid p-dir-col p-fluid dashboard">
                <div className="card">
                <h5>Advanced with Templating, Filtering and Clear Icon</h5>
                    <Dropdown value={empresa} options={empresas} onChange={onEmpresaSelect} itemTemplate={templateEmpresas}  style={{width: '100%'}}
                        filter={true} filterPlaceholder="Selecione uma empresa" filterBy="nome,classificao_setorial" showClear={true}/>
                </div>
            </div>
        </>
    );
}
