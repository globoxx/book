import { useLayoutEffect, useRef } from "react"
import gsap from "gsap"
import ScrollTrigger from "gsap/ScrollTrigger"
import TextPlugin from "gsap/TextPlugin"

gsap.registerPlugin(ScrollTrigger, TextPlugin)

function Exclamation() {

    const textRef = useRef(null)
    const iconContainerRef = useRef(null)
    const iconRef = useRef(null)

    useLayoutEffect(() => {

        const root = document.documentElement;
        const mainColor = getComputedStyle(root).getPropertyValue("--main-color").trim();
        const backgroundColor = getComputedStyle(root).getPropertyValue("--background-color").trim();
        console.log("-->" + mainColor)

        const tl = gsap.timeline({
            scrollTrigger: {
              trigger: ".update",
              start: "top-=25% top",
              end: "+=100%",
            }
        });

        /*Animation de l'intro de la section update*/

        /* setup des caractéristiques de bases */
        tl.set(iconRef.current, {fill: mainColor})
        .set(iconContainerRef.current, {backgroundColor: "transparent"})
        .set(iconContainerRef.current, {x: "-40vw"})
        .set(textRef.current, {text: "Lewis "})

        /* animation de la timeline avec l'icon le container de l'icon et le texte*/
        tl
        .to(iconRef.current, { rotate: "25deg", ease: "linear", duration: 0.025 })
        .to(iconRef.current, { rotate: "-25deg", ease: "linear", duration: 0.025 })
        .to(iconRef.current, { rotate: "0deg", ease: "elastic", duration: 0.175 })
        .to(iconContainerRef.current, {x: "0rem"})
        .to(iconRef.current, { fill: mainColor }, "<")
        .to(iconContainerRef.current, {backgroundColor: "transparent"}, "<")
        .to(iconContainerRef.current, {backgroundColor: mainColor, duration: 0.01})
        .to(iconRef.current, { fill: backgroundColor }, "<")
        .to(textRef.current, {text: "Lewis "},"<")
        .to(textRef.current, {text: "Lewis Updates"},"<0.1")

        return () => {
            tl.scrollTrigger.kill()
            tl.kill()
        }
    }, [])

    return(
        <div className='update-intro-wrapper'>
            <p className='update-title' ref={textRef}>Lewis</p>
            <div className='update-icon-container' ref={iconContainerRef}>
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#5f6368" className='update-icon' ref={iconRef}><path d="M480-120q-33 0-56.5-23.5T400-200q0-33 23.5-56.5T480-280q33 0 56.5 23.5T560-200q0 33-23.5 56.5T480-120Zm-80-240v-480h160v480H400Z"/></svg>
            </div>
        </div>
    )
}

export default Exclamation