import { useState, useLayoutEffect } from "react";
import mercedes from '../assets/mercedes.png'

function MenuText() {
    const [text, setText] = useState("The extraordinary course of the life of");
    
    const [splitText, setSplitText] = useState([]);

  
    useLayoutEffect(() => {
      setSplitText(text.split(""));
  
    }, []); // Dépend de `text`, pas de `position`
  
    return (
      <div className="text">
        <div className="top-line">
          {splitText.map((letter, index) => (
            <div
              key={index}
              className="floating-letter"
              style={letter === " " ? { visibility: "hidden" } : {}}
            >
              {letter === " " ? "\u00A0" : letter}
            </div>
          ))}
        </div>
        <div className="down-line">
          <span className="name">Sir. Lewis Hamilton</span>
          <img src={mercedes} className="mercedes" alt="mercedes" />
        </div>
      </div>
    );
}

export default MenuText