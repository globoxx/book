import { useRef, useState, useLayoutEffect, useContext, createContext, useEffect } from "react";
import gsap from "gsap";
import ScrollTrigger from "gsap/ScrollTrigger";

gsap.registerPlugin(ScrollTrigger)
const ScrollContext = createContext();

function Scroller() {
    const circleRef = useRef(null);
    const [stage, setStage] = useState(0)
    const {scrollStage, setScrollStage} = useContext(ScrollContext);

    useLayoutEffect(() => {

        const tl = gsap.timeline({
            scrollTrigger: {
                trigger: ".milestones-wrapper",
                start: "top top",
                end: "+=100%",
                pin: true,
                scrub: true,
                onUpdate: (self) => {
                    setStage(Math.round(self.progress*11))
                }
            }
        });

        let progress = Math.round((65/12) * (stage))
        setScrollStage(stage)


        tl.to(
            circleRef.current, 
            { y: `${progress}vh`, duration: 0}
        );

        return () => {
            tl.scrollTrigger.kill();
            tl.kill();
        };
    }, [stage]);

    function getStageClass(number) {

        if (stage === number) {
            return "active"
        }
        else return "unactive"
    }

    return (

        <div className='milestones-scroller-container'>
            <div className='milestones-scroller'>
                <div className='scircle' ref={circleRef}></div>
            </div>
            <div className='date-container'>
                <p className={getStageClass(0)}>1985</p>
                <p className={getStageClass(1)}>1993</p>
                <p className={getStageClass(2)}>1997</p>
                <p className={getStageClass(3)}>2006</p>
                <p className={getStageClass(4)}>2008</p>
                <p className={getStageClass(5)}>2013</p>
                <p className={getStageClass(6)}>2014</p>
                <p className={getStageClass(7)}>2018</p>
                <p className={getStageClass(8)}>2020</p>
                <p className={getStageClass(9)}>2021</p>
                <p className={getStageClass(10)}>2022</p>
                <p className={getStageClass(11)}>2024</p>
            </div>
        </div>
    );
}

function ImageShower() {

    const {scrollStage, setScrollStage} = useContext(ScrollContext)
    const imgRef = useRef(null)
    const paraRef = useRef(null)

    const images = [
        "//images.ctfassets.net/1fvlg6xqnm65/1yACcvtsT9KFKCaBm97vby/7b870c749e6cc64e10b482ee49a6d54a/baby-Lewis.jpg",
        "//images.ctfassets.net/1fvlg6xqnm65/7oV9PJJkmWsWMEqmkxOolQ/a249f010b6881427735fe44eb95cc821/Lewis-1993.jpg",
        "//images.ctfassets.net/1fvlg6xqnm65/7tExOvfMJchPhcl1SoU5eY/17af7cfab6e9255518de6fbdf36f19da/Lewis-1997.jpg",
        "//images.ctfassets.net/1fvlg6xqnm65/S1NEMf2rmG9N8bbCyAhHY/fd23aaa67a0d51a5fc84c2298aa0ddef/Lewis-2006.jpg",
        "//images.ctfassets.net/1fvlg6xqnm65/5JiPtGDhhcuwvVn65OUIy8/9d49df5ed8bdb4e458509bc57ee6de11/Lewis-2008.jpg",
        "//images.ctfassets.net/1fvlg6xqnm65/6tB5jjkKoWoz4eVVJrSjgB/bcd5067500d7797001a6fce0c1ae1e00/Lewis-2013.jpg",
        "//images.ctfassets.net/1fvlg6xqnm65/1LvwNWMoGKnuwBpoNb4PvY/72fdc751534bd828957ed1ce109826be/Lewis-2014.jpg",
        "//images.ctfassets.net/1fvlg6xqnm65/1EhTAHes2XKUQ8KrlNeyQ1/8f33617c0cd525fb4075f8ee78daa08e/Lewis-Fashion-2018.jpg",
        "//images.ctfassets.net/1fvlg6xqnm65/5ZUHk5E6i09V5WIrbgUkJb/ef54922769984be617311fbee4c27cbc/Lewis-2020.jpg",
        "//images.ctfassets.net/1fvlg6xqnm65/6mQaREakdGLhKlOrodPplh/6c9e9b0df1d9b9dc8f999fa1a2917c3d/Lewis-Mission-44.jpg",
        "//images.ctfassets.net/1fvlg6xqnm65/6hIok5lyCbJrskETwUGiZ3/19966dafce66907bc90b63a7af5761a5/Lewis-Citizenship.jpg",
        "//images.ctfassets.net/1fvlg6xqnm65/5Msywuu6FX9Dyk1dw8IGA2/61d3ad972dd846e4f4dee0ef058603a1/M448711.jpg"
    ]

    const paragraph = [
        "Lewis was born in Stevenage, Hertfordshire on the 7 January 1985 – to Anthony Hamilton and Carmen Larbalestier.",
        "After being bought his first go-kart by his Dad, Lewis starts karting competitively and collects multiple race wins across different British cadet races and championships.",
        "The early success catches the attention of those at the top of the sport, and the journey to Formula One takes another step forward as Lewis joins the McLaren Mercedes Young Driver Programme. On track, he wins the Super 1 National Championship in the more senior Formula Yamaha class.",
        "Fourteen podiums, five of them wins, see Lewis crowned GP2 champion at the first attempt. Standout performances include a drive through the field from P19 on lap one to P2 in Turkey, and a clean sweep at home at Silverstone. A fantastic season that earns him a seat in F1 for the following season. ",
        "A first F1 Drivers’ Championship is claimed in dramatic style at the final race of the year, to become one of the sport’s youngest champions. Five wins are enough to help seal glory, the highlight of which comes at Silverstone, as Lewis finishes nearly 70 seconds clear of the field in front of his home crowd. ",
        "Following six years at McLaren, Lewis moves to the Mercedes-AMG PETRONAS F1 Team – a move that is questioned up and down the paddock. He, alongside the Team, quickly get to work and score his first race win for the Team in Hungary. Five pole positions and a string of solid results help to secure P4 in the Drivers’ and P2 in the Constructors’ Championship.",
        "A season-long duel with teammate Nico Rosberg is decided in Abu Dhabi and ends in the capture of World Championship number two in the first season of the sport’s new hybrid era, as Mercedes also clinches its first Constructors’ Championship. Lewis also wins BBC Sports Personality of the Year for the first time too. ",
        "Off the track Lewis launches his first fashion line, Lewis x Tommy, with Tommy Hilfiger. On it, he becomes a five-time world champion, fending off the challenge of Ferrari and Sebastian Vettel. His win from 14th on the grid in Germany remains the furthest back he has ever won a Grand Prix from. The title drew him level with Juan Manuel Fangio for most F1 championships.",
        "Lewis writes further F1 history by equalling Michael Schumacher’s record of seven F1 titles and in the process breaks the record for most race wins in the sport at the Portuguese Grand Prix. In a year quite like any other in the world, he strengthens his stature as a voice for equality in the sport. At the end of the season, the Team launch its Accelerate 25 initiative aimed at increasing diversity and inclusion in motorsport.",
        "Continuing his push to change the motorsport landscape, Lewis sets up Mission44, the charitable Foundation aimed at transforming the lives of young people from underserved communities to ultimately help build a fairer society. At the end of the year, Lewis receives a knighthood. His mother Carmen attends the ceremony at Windsor Castle with her son, the fourth F1 driver in history to receive the prestigious accolade.",
        "One year on from his epic victory at Interlagos, Lewis attended a special ceremony at the Chamber of Deputies in Brasilia, where he receives honorary citizenship of Brasil. “I really want to dedicate today, this honour, to Ayrton Senna – to Ayrton’s family, to his friends and to his fans. I really do feel like I am one of you now,” said Lewis following the ceremony.",
        "Lewis wins an historic ninth British Grand Prix, marking his place in yet more history books. Conditions judged to perfection on track, strategy calls timed to perfection in the pit lane. Lewis’ record-breaking win at the British Grand Prix was achieved on pure pace and speed",
    ]


    useEffect(() => {
        imgRef.current.style.backgroundImage = `url(${images[scrollStage]})`
        paraRef.current.textContent = paragraph[scrollStage]


    },[scrollStage])

    return(
        <div className='milestones-div-shower'>
            <div className='milestones-div-container'>
                <div ref={imgRef} className="milestones-image"></div>
                <p ref={paraRef} className="milestones-para"></p>
            </div>
        </div>
    )
}

function MilestonesScroller () {
    const [scrollStage, setScrollStage] = useState(0);

    return(
        <ScrollContext.Provider value = { {scrollStage, setScrollStage} }>
            <div className='container-1'>
                <Scroller/>
                <ImageShower/>
            </div>
        </ScrollContext.Provider>
    )
}


export default MilestonesScroller