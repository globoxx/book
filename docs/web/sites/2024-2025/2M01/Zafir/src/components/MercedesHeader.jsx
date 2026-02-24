import { useLayoutEffect, useRef } from "react";
import gsap from "gsap";
import ScrollTrigger from "gsap/ScrollTrigger";

gsap.registerPlugin(ScrollTrigger)

function MercedesHeader() {
    const textRef = useRef(null);

    useLayoutEffect(() => {

      const tl = gsap.timeline({
        scrollTrigger: {
          trigger: "body",
          start: "top top",
          end: "+=300vh",
          scrub: 1,
        },
      });
  
      tl.fromTo(
        textRef.current,
        { y: 0 },
        { y: -100 }
      );

      return () => {
        tl.scrollTrigger.kill()
        tl.kill()
      }

    }, []);
  
    return (
      <div className="text-acc" ref={textRef}>
        LEWIS HAMILTON
      </div>
    );
}

export default MercedesHeader