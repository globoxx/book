import { useRef, useLayoutEffect } from "react";
import ScrollTrigger from "gsap/ScrollTrigger";
import gsap from "gsap";
import videoPub from "../assets/W14-pub.mp4"

gsap.registerPlugin(ScrollTrigger)

function W14() {
    let cacheRef = useRef(null)

    useLayoutEffect(() => {

        const tl = gsap.timeline({scrollTrigger: {
            trigger: ".W14-introduction",
            start: "top top",
            end: "+=100%",
            scrub: 1,
            pin: true,
        }})

        tl.fromTo(cacheRef.current, 
            { scale: "45", x: "-104vw" },
            { scale: "1", x: 0, duration: 20}
        );

        return () => {
            tl.scrollTrigger.kill()
            tl.kill()
        }

    }, []);

    return (
        <div className='W14-introduction'>
            <video className="W14-video" width="100%" height="100%" src={videoPub} autoPlay loop muted/>
            <div ref={cacheRef} className='cache'>
                <svg viewBox="0 0 100 100" preserveAspectRatio="xMidYMid slice">
                    <defs>
                        <mask id="W14-mask" x="0" y="0" width="100%" height="100%">
                            <rect x="0" y="0" width="100%" height="100%" fill="white"></rect>
                            <text x="50%" y="50%" fontSize="15" textAnchor="middle" dy=".35em" fill="black">W14</text>
                        </mask>
                    </defs>
                    <rect x="0" y="0" width="100%" height="100%" mask="url(#W14-mask)" id="sub"></rect>
                </svg>
            </div>
        </div>
    );
}

export default W14