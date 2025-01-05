import './Layout.scss'
import Navbar from '../components/Navbar';
import { Link as LinkDOM } from 'react-router-dom';

function Layout() {
    return (
        <div className='layout-root'>
            <div className='layout-wrapper'>
            <Navbar/>
                <ul className='Layout'>
                    <li className='brick brick-React'>
                        <div>React : Une bibliothèque JavaScript populaire permettant de créer des interfaces utilisateur dynamiques et performantes. (Très utile)</div>
                    </li>
                    <li className='brick brick-Youtube'>
                        <div>YouTube : Une plateforme incontournable pour se former et découvrir des outils utiles pour le développement web.</div>
                    </li>
                    <li className='brick brick-GSAP'>
                        <div>GSAP : Une bibliothèque JavaScript puissante pour créer des animations fluides, interactives et complexes.</div>
                    </li>
                    <li className='brick brick-JSX'>
                        <div>JSX : Une syntaxe proche du HTML utilisée avec React pour décrire des interfaces utilisateur, en combinant HTML et XML de manière efficace.</div>
                    </li>
                    <li className='brick brick-SCSS'>
                        <div>SCSS : Un préprocesseur CSS qui enrichit les styles avec des fonctionnalités avancées comme les variables, les mixins et l'imbrication de règles, rendant le code plus lisible et maintenable.</div>
                    </li>
                    <li className='brick brick-Emmet'>
                        <div>Emmet : Un outil indispensable pour accélérer l'écriture de HTML et CSS grâce à des raccourcis (snippets) efficaces.</div>
                    </li>
                    <li className='brick brick-ChatGPT'>
                        <div>ChatGPT : Un assistant puissant pour poser des questions et apprendre rapidement de nouveaux concepts en programmation et au-delà.</div>
                    </li>
                    <li className='brick brick-HTMLCSSJS'>
                        <div>HTML, CSS, JS : Les trois technologies fondamentales du développement web frontend, utilisées pour structurer, styliser et rendre interactif un site web.</div>
                    </li>
                </ul>
                <LinkDOM to="/" className='home-button-return'>
                    RETOURNER HOME
                </LinkDOM>
            </div>
        </div>
    );
}

export default Layout