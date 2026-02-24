import './Home.scss';
import Navbar from '../components/Navbar.jsx';
import W14Mask from "../assets/W14-mask.png"
import W14Background from "../assets/W14-background.jpg"
import ArrowSVG from '../assets/ArrowSVGDown.jsx';
import W14 from '../components/W14.jsx';
import MercedesHeader from '../components/MercedesHeader.jsx';
import MilestonesScroller from '../components/MilestonesScroller.jsx';
import Exclamation from '../components/Exclamation.jsx';
import SponsorsScroller from '../components/SponsorsScroller.jsx';
import FrameContainer from '../components/FrameContainer.jsx';
import W14Info from '../components/W14Info.jsx';
import TextContainer from '../components/TextContainer.jsx'
import { Link as LinkDOM} from 'react-router-dom';
import { Element } from 'react-scroll';
import ScrollTrigger from 'gsap/ScrollTrigger';

/*
import { Canvas } from "@react-three/fiber";
import { OrbitControls, useGLTF } from "@react-three/drei";
import * as THREE from "three";
*/

/* 
            {images.map((image, index) => {
                <div className={`milestones-image m-image${index}`}>{paragraph[index]}</div>
            })}



Syntaxe pour le nom des objets qui contiennent d'autres objets du plus global au moin global
root-{name} (global = ex:page) 
-> wrapper (large = ex:inner section) 
    -> container (medium = ex:subsection) 
        -> holder (small => ex:sectionTail) 

tip important que j'ai appris pour gsap qui modifis le DOM et éviter les erreurs:

si gsap est utilisé, apart le fait qu'il doit etre utiliser dans un hook comme useEffect, les animations gsap doivent obligatoirement être appelé
dans le hook useLayoutEffect et non useEffect, la différence entre les deux est le moment d'execution du script useEffect est executé après le rendu tandis que useLayoutEffect
est executé avant ce qui permet la dualité de react et gsap => donc pour toutes les fonctions qui affectent le DOM elles doivent être mises dans useLayoutEffect, pour
ne pas entrer en conflit avec react qui a déja render le DOM.

*/

function Home() {
    ScrollTrigger.refresh()
    return(
    <div className='home-root'>
        <Navbar/>
        <Element className='accueil' id='accueil'>
            <div className='accueil-holder'>
                <img src={W14Background} className='bg-acc'></img>
                <MercedesHeader/>
                <img src={W14Mask} className='bg-mask-acc'></img>
            </div>
        </Element>
        <Element className='milestones' id='milestones'>
            <div className='milestones-wrapper'>
                <div className='milestones-title'>Lewis' Milestones</div>
                <MilestonesScroller/>
            </div>
        </Element>
        <Element className='W14' id='W14'>
            <div className='W14-introduction-container'>
                <W14/>
                <TextContainer
                containerClass= "W14-introduction-text-container"
                head= "AMG F1 W14 E Performance"
                headClass= "W14-introduction-h"
                para= "La Mercedes-AMG F1 W14 E Performance incarne l’excellence technique et l’innovation de Mercedes en Formule 1. Conçue pour maximiser performance et efficacité, elle allie un moteur hybride de pointe à un design aérodynamique avancé, reflétant l’engagement de l’équipe envers la durabilité et la compétition au plus haut niveau."
                paraClass= "W14-introduction-p"
                /> 
            </div>
            <div className='W14-image-container'>
                <div className='W14-image-wrapper'>
                    <img src={W14Mask} alt='' className='W14-image'></img>
                </div>
                <W14Info/>
            </div>
        </Element>
        <Element className='update' id='update'>
            <Exclamation/>
            <div className='update-inner-wrapper'>
                <FrameContainer/>
                <div className='update-arrow-container'>
                    <ArrowSVG></ArrowSVG>
                </div>
            </div>
        </Element>
        <div className='layout-button-holder'>
            <LinkDOM to="/Layout" className='layout-button'>
                OUTILS UTILISÉS
            </LinkDOM>
        </div>
        <Element className='sponsor' id='sponsor'>
            <div className='sponsor-wrapper'>
                <SponsorsScroller/>
                <div className='sponsor-mask'></div>
            </div>
        </Element>
    </div>
    )
}

export default Home
