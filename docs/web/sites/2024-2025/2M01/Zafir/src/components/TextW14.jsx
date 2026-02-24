import { useRef, useLayoutEffect } from "react";
import gsap from "gsap";
import ScrollTrigger from "gsap/ScrollTrigger";
import { useGSAP } from "@gsap/react"



function TextW14( { p0, p1 }) {

    let p0Ref = useRef(null)
    let p1Ref = useRef(null)

    useLayoutEffect(() => {

        const tl = gsap.timeline({
            scrollTrigger: {
              trigger: p0Ref.current,
              start: "bottom+=10% bottom",
            }
          });

        tl.set(p0Ref.current,
            {x: -50, opacity: 0, duration: 0}, 
        )
        tl.set(p1Ref.current,
            {x: -50, opacity: 0, duration: 0}
        )
        tl.to(p0Ref.current,
            {x: 0, opacity: 1, duration: 0.5}, "<"
        )
        tl.to(p1Ref.current,
            {x: 0, opacity: 1, duration: 0.5}, "<"
        )

        return () => {
            tl.scrollTrigger.kill()
            tl.kill()
        }

    }, [])

    return (
        <div>
            <p className='p0' ref={p0Ref} style={{x:-50, opacity:0}}>{p0}</p>
            <p className="p1" ref={p1Ref} style={{x:-50, opacity:0}}>{p1}</p>
        </div>
    )
}

export default TextW14