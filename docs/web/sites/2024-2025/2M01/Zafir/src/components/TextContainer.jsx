import { useRef, useLayoutEffect } from "react"
import gsap from "gsap"
import ScrollTrigger from "gsap/ScrollTrigger"
gsap.registerPlugin(ScrollTrigger)

function TextContainer( { containerClass, head, headClass, para, paraClass }) {
    const textContainerRef = useRef(null)
    
    useLayoutEffect( () => {

        const tl = gsap.timeline({scrollTrigger: {
            trigger: textContainerRef.current,
            start: "bottom bottom",
            end: "bottom 70%",
            scrub: 1,
        }})

        tl.fromTo(textContainerRef.current, 
            {opacity: 0, y: 50}, 
            {opacity: 1, y: 0})

        return () => {
            tl.scrollTrigger.kill()
            tl.kill()
        }
    }, [])

    return (
        <div className={`text-container ${containerClass}`} ref={textContainerRef}>
            <p className={`head ${headClass}`}>
                {head}
            </p>
            <p className='para'>
                {para}
            </p>
        </div>
    )
}
export default TextContainer