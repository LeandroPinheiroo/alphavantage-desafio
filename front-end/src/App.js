import React, { useRef } from 'react';
import classNames from 'classnames';
import { Redirect, Route } from 'react-router-dom';
import { CSSTransition } from 'react-transition-group';
import {useSelector} from 'react-redux';

import { AppTopbar } from './AppTopbar';
import { AppFooter } from './AppFooter';
import { AppMenu } from './AppMenu';
import { AppProfile } from './AppProfile';

import { Dashboard } from './components/Dashboard';
import { Login } from './pages/Login/Login'




import 'primereact/resources/themes/saga-blue/theme.css';
import 'primereact/resources/primereact.min.css';
import 'primeicons/primeicons.css';
import 'primeflex/primeflex.css';
import 'prismjs/themes/prism-coy.css';
import '@fullcalendar/core/main.css';
import '@fullcalendar/daygrid/main.css';
import '@fullcalendar/timegrid/main.css';
import './layout/layout.scss';
import './App.scss';
import { Empresa } from './components/Empresa';
import { Registrar } from './pages/usuario-novo';

const App = () => {

    const sidebar = useRef();
    


    const menu = [
        { label: 'Home', icon: 'pi pi-fw pi-home', to: '/' },
        {
            label: 'Cotação', icon: 'pi pi-fw pi-chart-bar',
            items: [
                { label: 'Empresas', icon: 'pi pi-fw pi-id-card', to: '/empresa' },
            ]
        },
        
    ];


    const isDesktop = () => {
        return window.innerWidth > 1024;
    }

    const isSidebarVisible = () => {
        if (isDesktop()) {
            return true;
        }

        return true;
    }

    const logo = 'assets/layout/images/ponto-tel.png';

    const wrapperClass = classNames('layout-wrapper', {
        'layout-static': true,
    });

    const sidebarClassName = classNames('layout-sidebar', {
        'layout-sidebar-light': true
    });

    return (
        <>
            {
                useSelector(state => state.user.usuarioLogado) === 1 &&
                <div className={wrapperClass}>
                    <AppTopbar />

                    <CSSTransition classNames="layout-sidebar" timeout={{ enter: 200, exit: 200 }} in={isSidebarVisible()} unmountOnExit>
                        <div ref={sidebar} className={sidebarClassName} >
                            <div className="layout-logo">
                                <img alt="Logo" src={logo} width='100'/>
                            </div>
                            <AppProfile />
                            <AppMenu model={menu} />
                        </div>
                    </CSSTransition>


                    <div className="layout-main">
                        <Route path="/" exact component={Dashboard} />
                        <Route path="/empresa" exact component={Empresa} />
                    </div>

                    <AppFooter />

                </div>
            }
            {useSelector(state => state.user.usuarioLogado) === 0 ? <Redirect to="/login"></Redirect> : null}
            {
                useSelector(state => state.user.usuarioLogado) === 0 &&
                <>
                    <Route path="/login" exact component={Login} />
                    <Route path="/registrar" exact component={Registrar} />
                </>
            }
        </>
    );

}

export default App;
