import ArrowSVG from "../assets/ArrowSVGDown"
import TextW14 from "./TextW14"

function W14Info() {
    return (
        <ul className='W14-features-container'>
        <li className="W14-feature">
            <div className='first-feature-container'>
                <a href="https://www.mercedesamgf1.com/car/2023-car">
                    <ArrowSVG/>
                </a>
                <TextW14 
                p0="EN SAVOIR PLUS"
                p1="MERCEDES W14"
                />
            </div>
        </li>
        <li className="W14-feature">
            <TextW14 
            p0="PUISSANCE (combinée ICE + EE)"
            p1="1000 CH"
            />
        </li>
        <li className="W14-feature">
            <TextW14 
            p0="VITESSE MAX"
            p1="350 KM/H"
            />
        </li>
        <li className="W14-feature">
            <TextW14 
            p0="0 À 100 KM/H"
            p1="2,5 S"
            />
        </li>
        <li className="W14-feature">
            <TextW14 
            p0="MOTEUR"
            p1="HYBRIDE V6 TURBO 1,6 L"
            />
        </li>
        <li className="W14-feature">
            <TextW14 
                p0="CONDUCTEUR"
                p1="LEWIS HAMILTON"
            />
        </li>
    </ul>
    )
}

export default W14Info