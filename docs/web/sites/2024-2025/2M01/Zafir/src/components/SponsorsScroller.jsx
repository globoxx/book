import { useEffect, useRef } from "react";
import gsap from "gsap";
import { Timeline } from "gsap/gsap-core";

function SponsorsScroller() {

    const requireImages = require.context('../assets/sponsors', false, /\.(webp)$/);
    const images = requireImages.keys().map(requireImages);

    const holder11 = useRef(null)
    const holder12 = useRef(null)
    const holder21 = useRef(null)
    const holder22 = useRef(null)

    useEffect(() => {
        const tl = gsap.timeline()


        tl.fromTo(holder11.current,
            {x: "-200%"},
            {x: "0%", duration: 100, repeat: -1, ease: "linear", delay: -100}, "<"
        )
        tl.fromTo(holder21.current,
            {x: "0"},
            {x: "-200%", duration: 100, repeat: -1, ease: "linear", delay: -100}, "<"
        )

        tl.fromTo(holder12.current, 
            {x: "-200%"}, 
            {x: "0%", duration: 100, repeat:  -1, ease: "linear", delay: -100}, "<50"
        )
        tl.fromTo(holder22.current,
            {x: "0"},
            {x: "-200%", duration: 100, repeat: -1, ease: "linear", delay: -100}, "<"
        )



    })

    return(
        <div className="sponsor-scroller-container">
            <div className="sponsor-scroller-1">

                <div className="sponsor-scroller-1-holder-1" ref={holder11}>
                    {images.slice(0,11).map((image, index) => (
                        <img key={index} src={image} className={`sponsor-img sponsor-img-${index}`}></img>
                    ))}
                </div>

                <div className="sponsor-scroller-1-holder-2" ref={holder12}>
                    {images.slice(0,11).map((image, index) => (
                        <img key={index} src={image} className={`sponsor-img sponsor-img-${index}`}></img>
                    ))}
                </div>

            </div>
            <div className="sponsor-scroller-2">

                <div className="sponsor-scroller-2-holder-1" ref={holder21}>
                    {images.slice(12,24).map((image, index) => (
                        <img key={index} src={image} className={`sponsor-img sponsor-img-${index}`}></img>
                    ))}
                </div>

                <div className="sponsor-scroller-2-holder-2" ref={holder22}>
                    {images.slice(12,24).map((image, index) => (
                        <img key={index} src={image} className={`sponsor-img sponsor-img-${index}`}></img>
                    ))}
                </div>

            </div>
        </div>
    )
}

export default SponsorsScroller