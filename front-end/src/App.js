import React, { useRef } from 'react';
import classNames from 'classnames';
import { Route } from 'react-router-dom';
import { CSSTransition } from 'react-transition-group';

import { AppTopbar } from './AppTopbar';
import { AppFooter } from './AppFooter';
import { AppMenu } from './AppMenu';
import { AppProfile } from './AppProfile';

import { Dashboard } from './components/Dashboard';




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

const App = () => {

    const sidebar = useRef();
    


    const menu = [
        { label: 'Home', icon: 'pi pi-fw pi-home', to: '/' },
        {
            label: 'Cotação', icon: 'pi pi-fw pi-chart-bar',
            items: [
                { label: 'Empresas', icon: 'pi pi-fw pi-id-card', to: '/cotacao-empresas' },
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
            </div>

            <AppFooter />

        </div>
    );

}

export default App;
