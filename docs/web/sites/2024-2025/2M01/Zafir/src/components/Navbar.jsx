import { useState, useRef, useLayoutEffect } from 'react';
import { Link } from 'react-scroll';
import { Link as LinkDOM } from 'react-router-dom';

function Navbar() {
    const [isVisible, setIsVisible] = useState(true);
    const lastScroll = useRef(0);
    const mousePosition = useRef({ x: 0, y: 0 });

    useLayoutEffect(() => {
        const handleScroll = () => {
            const currentScroll = window.pageYOffset;

            if (currentScroll < lastScroll.current) {
                setIsVisible(true);
            } else if (currentScroll > lastScroll.current) {
                setIsVisible(false);
            }
            lastScroll.current = currentScroll;
        };
        const handleMouseMove = (e) => {
            mousePosition.current = { x: e.clientX, y: e.clientY };
            if (mousePosition.current.y < 100) {
                setIsVisible(true);
            } else {
                setIsVisible(false);
            }
        };

        window.addEventListener('scroll', handleScroll);
        window.addEventListener('mousemove', handleMouseMove);

        return () => {
            window.removeEventListener('scroll', handleScroll);
            window.removeEventListener('mousemove', handleMouseMove);
        };
    }, []);

    return (
        <nav className={`navbar ${isVisible ? 'visible' : 'unvisible'}`}>
            <div className='brand'>
                <LinkDOM className='brand-name' to="/">MERCEDES</LinkDOM>
            </div>
            <div className="buttons">
                <Link smooth={true} to="accueil" className='button' data-text="ACCUEIL">ACCUEIL</Link>
                <Link smooth={true} to="milestones" className='button' data-text="MILESTONES">MILESTONES</Link>
                <Link smooth={true} to="W14" className='button' data-text="W14">W14</Link>
                <Link smooth={true} to="update" className='button' data-text="UPDATE">UPDATE</Link>
                <Link smooth={true} to="sponsor" className='button' data-text="SPONSOR">SPONSOR</Link>
            </div>
        </nav>
    );
}

export default Navbar;