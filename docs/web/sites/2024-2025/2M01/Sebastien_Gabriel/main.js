//pour la documentation JS, la majorite vient de https://www.w3schools.com/js/default.asp ou de https://stackoverflow.com/ pour certaines parties plus specifiques (celle-là sont citées)

//theme de couleur des plateaux

let boardThemes = new Array
let throughTheme = 0;

class boardTheme{
    constructor(whiteColor, blackColor, moveColor){
        this.whiteColor = whiteColor
        this.blackColor = blackColor
        this.moveColor = moveColor
    }

    initColor(){
        let whiteCells = document.getElementsByClassName("whiteCell")
        let blackCells = document.getElementsByClassName("blackCell")
        for(let whiteI of whiteCells){
            whiteI.style.backgroundColor = this.whiteColor
        }
        for(let blackI of blackCells){
            blackI.style.backgroundColor = this.blackColor
        }
    }
}

function createBoard(whiteColor, blackColor, moveColor){
    boardThemes[boardThemes.length] = new boardTheme(whiteColor, blackColor, moveColor)
}

function cycleThemes(){
    throughTheme++
    boardThemes[throughTheme % boardThemes.length].initColor()
}

createBoard("#eeeed2", "#769656", "#FF4D4D")
createBoard("#FFFFFF", "#5BCEFA", "#F5A9B8")
createBoard("#fed700", "#21b0fe", "#fe218b") //les couleurs ont été trouvées sur https://colorkit.co/palettes/3-colors/ sauf la premiere qui est celle de base de https://chess.com
createBoard("#84ffc9", "#aab2ff", "#eca0ff")
createBoard("#9cf4d0", "#f4a4ea", "#71db39")
createBoard("#0CCFDF", "#6B48FF", "#FF5AA2")

//fonction pour faciliter la conversion position sur l'echequier et leur cordonée (x, y) ex. e4 -> (5, 4)

function posToName(xpos, ypos){
    var lettreCase = String.fromCharCode(xpos+96)
    if(ypos % 8 != 0){
        var numbreCase = ypos % 8
    }else{
        var numbreCase = 8
    }
    return(lettreCase + numbreCase)
}

function nameToxpos(name){
    return(name.charCodeAt(0)-96)
}

function nameToypos(name){
    return(Number(name.charAt(1)))
}

//fonction qui cherche des checks et des checkmates/stalemate

function isThereEnd(color, arg){ //changer y a des bugs
    let legalMovesTotal = []
    for(i in pieces){
        if(pieces[i].color == color){
            let legalMovePiece = pieces[i].getLegalMove()
            legalMovesTotal = legalMovesTotal.concat(legalMovePiece)
        }  
    }
    if(legalMovesTotal.length == 0){
        if(isKingChecked(color, pieces)){
            if(arg == "checkmate"){
                return(true)
            }   
        }
        else if(arg == "stalemate"){
            return(true)
        }
    }
    else{
        return(false)
    }
}

function isKingChecked(color, piecesOnboard){
    let isChecked = false
    for(let k in piecesOnboard){
        if(piecesOnboard[k].name == "king" && piecesOnboard[k].color == color){
            roiTarget = piecesOnboard[k]
        }
    }
    caseRoiTarget = posToName(roiTarget.xpos, roiTarget.ypos)
    for(k in piecesOnboard){
        if(piecesOnboard[k].color != color){
            if(piecesOnboard[k].trouverCasePossible().includes(caseRoiTarget)){
                isChecked = true
            }
        }
    }
    return(isChecked)
}

//classe d'objet pièce avec une méthode qui trouve les coups possibles d'une piece, une qui permet de determiner si un coup est legal ou non, et une derniere pour la promotion d'un pion

class piece{
    constructor(xpos, ypos, color, symbol, name){
        this.xpos = xpos
        this.ypos = ypos
        this.color = color
        this.symbol = symbol
        this.name = name
        this.casePos = posToName(xpos, ypos)
        this.hasNotMoved = true
    }

    trouverCasePossible(){
        var xPosPossible = this.xpos
        var yPosPossible = this.ypos
        let casePossible = new Array;
        var bloque = false;
        if(this.name == "knight"){
            for(i = 1; i <= 2; i++){
                xPosPossible = this.xpos + 2
                yPosPossible = this.ypos + (-1) ** i
                if(xPosPossible <= 8 && xPosPossible >= 1 && yPosPossible <= 8 && yPosPossible >= 1 && (cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation.length == 0 || cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation[0].color != this.color)){
                    casePossible.push(posToName(xPosPossible, yPosPossible))
                }  
            }
            for(i = 1; i <= 2; i++){
                xPosPossible = this.xpos - 2
                yPosPossible = this.ypos + (-1) ** i
                if(xPosPossible <= 8 && xPosPossible >= 1 && yPosPossible <= 8 && yPosPossible >= 1 && (cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation.length == 0 || cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation[0].color != this.color)){
                    casePossible.push(posToName(xPosPossible, yPosPossible))
                }  
            }
            for(i = 1; i <= 2; i++){
                yPosPossible = this.ypos + 2
                xPosPossible = this.xpos + (-1) ** i
                if(xPosPossible <= 8 && xPosPossible >= 1 && yPosPossible <= 8 && yPosPossible >= 1 && (cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation.length == 0 || cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation[0].color != this.color)){
                    casePossible.push(posToName(xPosPossible, yPosPossible))
                }  
            }
            for(i = 1; i <= 2; i++){
                yPosPossible = this.ypos - 2
                xPosPossible = this.xpos + (-1) ** i
                if(xPosPossible <= 8 && xPosPossible >= 1){
                    if(xPosPossible <= 8 && xPosPossible >= 1 && yPosPossible <= 8 && yPosPossible >= 1 && (cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation.length == 0 || cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation[0].color != this.color)){
                        casePossible.push(posToName(xPosPossible, yPosPossible))
                    } 
                }
            }
        }
        
        if(this.name == "rook"){
            i = 1
            while(bloque != true && xPosPossible <= 8 && xPosPossible >= 1 && yPosPossible <= 8 && yPosPossible >= 1){
                xPosPossible = this.xpos + i
                yPosPossible = this.ypos
                if(xPosPossible <= 8 && xPosPossible >= 1 && yPosPossible <= 8 && yPosPossible >= 1 && (cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation.length == 0 || cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation[0].color != this.color)){
                    casePossible.push(posToName(xPosPossible, yPosPossible))
                }
                if(xPosPossible <= 8 && xPosPossible >= 1){
                    if(cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation.length != 0){
                        bloque = true
                    }
                }
                i++
            }
            xPosPossible = this.xpos
            yPosPossible = this.ypos
            bloque = false
            i = 1
            while(bloque != true && xPosPossible <= 8 && xPosPossible >= 1 && yPosPossible <= 8 && yPosPossible >= 1){
                xPosPossible = this.xpos - i
                yPosPossible = this.ypos
                if(xPosPossible <= 8 && xPosPossible >= 1 && yPosPossible <= 8 && yPosPossible >= 1 && (cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation.length == 0 || cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation[0].color != this.color)){
                    casePossible.push(posToName(xPosPossible, yPosPossible))
                }
                if(xPosPossible <= 8 && xPosPossible >= 1){
                    if(cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation.length != 0){
                        bloque = true
                    }
                }
                i++
            }
            bloque = false
            i = 1
            xPosPossible = this.xpos
            yPosPossible = this.ypos
            while(bloque != true && yPosPossible <= 8 && yPosPossible >= 1 && xPosPossible <= 8 && xPosPossible >= 1){
                xPosPossible = this.xpos
                yPosPossible = this.ypos + i
                if(xPosPossible <= 8 && xPosPossible >= 1 && yPosPossible <= 8 && yPosPossible >= 1 && (cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation.length == 0 || cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation[0].color != this.color)){
                    casePossible.push(posToName(xPosPossible, yPosPossible))
                }
                if(yPosPossible <= 8 && yPosPossible >= 1){
                    if(cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation.length != 0){
                        bloque = true
                    }
                }
                i++
            }
            bloque = false
            i = 1
            xPosPossible = this.xpos
            yPosPossible = this.ypos
            while(bloque != true && yPosPossible <= 8 && yPosPossible >= 1 && xPosPossible <= 8 && xPosPossible >= 1){
                xPosPossible = this.xpos
                yPosPossible = this.ypos - i
                if(xPosPossible <= 8 && xPosPossible >= 1 && yPosPossible <= 8 && yPosPossible >= 1 && (cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation.length == 0 || cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation[0].color != this.color)){
                    casePossible.push(posToName(xPosPossible, yPosPossible))
                }
                if(yPosPossible <= 8 && yPosPossible >= 1){
                    if(cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation.length != 0){
                        bloque = true
                    }
                }
                i++
            }
        }
        
        if(this.name == "bishop"){
            i = 1
            while(bloque != true && xPosPossible <= 8 && xPosPossible >= 1 && yPosPossible <= 8 && yPosPossible >= 1){
                xPosPossible = this.xpos + i
                yPosPossible = this.ypos + i
                if(xPosPossible <= 8 && xPosPossible >= 1 && yPosPossible <= 8 && yPosPossible >= 1 && (cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation.length == 0 || cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation[0].color != this.color)){
                    casePossible.push(posToName(xPosPossible, yPosPossible))
                }
                if(xPosPossible <= 8 && xPosPossible >= 1 && yPosPossible <= 8 && yPosPossible >= 1){
                    if(cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation.length != 0){
                        bloque = true
                    }
                }
                i++
            }
            xPosPossible = this.xpos
            yPosPossible = this.ypos
            bloque = false
            i = 1
            while(bloque != true && xPosPossible <= 8 && xPosPossible >= 1 && yPosPossible <= 8 && yPosPossible >= 1){
                xPosPossible = this.xpos + i
                yPosPossible = this.ypos - i
                if(xPosPossible <= 8 && xPosPossible >= 1 && yPosPossible <= 8 && yPosPossible >= 1 && (cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation.length == 0 || cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation[0].color != this.color)){
                    casePossible.push(posToName(xPosPossible, yPosPossible))
                }
                if(xPosPossible <= 8 && xPosPossible >= 1 && yPosPossible <= 8 && yPosPossible >= 1){
                    if(cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation.length != 0){
                        bloque = true
                    }
                }
                i++
            }
            bloque = false
            i = 1
            xPosPossible = this.xpos
            yPosPossible = this.ypos
            while(bloque != true && yPosPossible <= 8 && yPosPossible >= 1 && xPosPossible <= 8 && xPosPossible >= 1){
                xPosPossible = this.xpos - i
                yPosPossible = this.ypos + i
                if(xPosPossible <= 8 && xPosPossible >= 1 && yPosPossible <= 8 && yPosPossible >= 1 && (cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation.length == 0 || cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation[0].color != this.color)){
                    casePossible.push(posToName(xPosPossible, yPosPossible))
                }
                if(xPosPossible <= 8 && xPosPossible >= 1 && yPosPossible <= 8 && yPosPossible >= 1){
                    if(cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation.length != 0){
                        bloque = true
                    }
                }
                i++
            }
            bloque = false
            i = 1
            xPosPossible = this.xpos
            yPosPossible = this.ypos
            while(bloque != true && yPosPossible <= 8 && yPosPossible >= 1 && xPosPossible <= 8 && xPosPossible >= 1){
                xPosPossible = this.xpos - i
                yPosPossible = this.ypos - i
                if(xPosPossible <= 8 && xPosPossible >= 1 && yPosPossible <= 8 && yPosPossible >= 1 && (cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation.length == 0 || cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation[0].color != this.color)){
                    casePossible.push(posToName(xPosPossible, yPosPossible))
                }
                if(xPosPossible <= 8 && xPosPossible >= 1 && yPosPossible <= 8 && yPosPossible >= 1){
                    if(cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation.length != 0){
                        bloque = true
                    }
                }
                i++
            }
        }
        
        if(this.name == "queen"){
            i = 1
            while(bloque != true && xPosPossible <= 8 && xPosPossible >= 1 && yPosPossible <= 8 && yPosPossible >= 1){
                xPosPossible = this.xpos + i
                yPosPossible = this.ypos
                if(xPosPossible <= 8 && xPosPossible >= 1 && yPosPossible <= 8 && yPosPossible >= 1 && (cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation.length == 0 || cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation[0].color != this.color)){
                    casePossible.push(posToName(xPosPossible, yPosPossible))
                }
                if(xPosPossible <= 8 && xPosPossible >= 1){
                    if(cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation.length != 0){
                        bloque = true
                    }
                }
                i++
            }
            xPosPossible = this.xpos
            yPosPossible = this.ypos
            bloque = false
            i = 1
            while(bloque != true && xPosPossible <= 8 && xPosPossible >= 1 && yPosPossible <= 8 && yPosPossible >= 1){
                xPosPossible = this.xpos - i
                yPosPossible = this.ypos
                if(xPosPossible <= 8 && xPosPossible >= 1 && yPosPossible <= 8 && yPosPossible >= 1 && (cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation.length == 0 || cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation[0].color != this.color)){
                    casePossible.push(posToName(xPosPossible, yPosPossible))
                }
                if(xPosPossible <= 8 && xPosPossible >= 1){
                    if(cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation.length != 0){
                        bloque = true
                    }
                }
                i++
            }
            bloque = false
            i = 1
            xPosPossible = this.xpos
            yPosPossible = this.ypos
            while(bloque != true && yPosPossible <= 8 && yPosPossible >= 1 && xPosPossible <= 8 && xPosPossible >= 1){
                xPosPossible = this.xpos
                yPosPossible = this.ypos + i
                if(xPosPossible <= 8 && xPosPossible >= 1 && yPosPossible <= 8 && yPosPossible >= 1 && (cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation.length == 0 || cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation[0].color != this.color)){
                    casePossible.push(posToName(xPosPossible, yPosPossible))
                }
                if(yPosPossible <= 8 && yPosPossible >= 1){
                    if(cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation.length != 0){
                        bloque = true
                    }
                }
                i++
            }
            bloque = false
            i = 1
            xPosPossible = this.xpos
            yPosPossible = this.ypos
            while(bloque != true && yPosPossible <= 8 && yPosPossible >= 1 && xPosPossible <= 8 && xPosPossible >= 1){
                xPosPossible = this.xpos
                yPosPossible = this.ypos - i
                if(xPosPossible <= 8 && xPosPossible >= 1 && yPosPossible <= 8 && yPosPossible >= 1 && (cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation.length == 0 || cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation[0].color != this.color)){
                    casePossible.push(posToName(xPosPossible, yPosPossible))
                }
                if(yPosPossible <= 8 && yPosPossible >= 1){
                    if(cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation.length != 0){
                        bloque = true
                    }
                }
                i++
            }
            bloque = false
            xPosPossible = this.xpos
            yPosPossible = this.ypos
            i = 1
            while(bloque != true && xPosPossible <= 8 && xPosPossible >= 1 && yPosPossible <= 8 && yPosPossible >= 1){
                xPosPossible = this.xpos + i
                yPosPossible = this.ypos + i
                if(xPosPossible <= 8 && xPosPossible >= 1 && yPosPossible <= 8 && yPosPossible >= 1 && (cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation.length == 0 || cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation[0].color != this.color)){
                    casePossible.push(posToName(xPosPossible, yPosPossible))
                }
                if(xPosPossible <= 8 && xPosPossible >= 1 && yPosPossible <= 8 && yPosPossible >= 1){
                    if(cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation.length != 0){
                        bloque = true
                    }
                }
                i++
            }
            xPosPossible = this.xpos
            yPosPossible = this.ypos
            bloque = false
            i = 1
            while(bloque != true && xPosPossible <= 8 && xPosPossible >= 1 && yPosPossible <= 8 && yPosPossible >= 1){
                xPosPossible = this.xpos + i
                yPosPossible = this.ypos - i
                if(xPosPossible <= 8 && xPosPossible >= 1 && yPosPossible <= 8 && yPosPossible >= 1 && (cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation.length == 0 || cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation[0].color != this.color)){
                    casePossible.push(posToName(xPosPossible, yPosPossible))
                }
                if(xPosPossible <= 8 && xPosPossible >= 1 && yPosPossible <= 8 && yPosPossible >= 1){
                    if(cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation.length != 0){
                        bloque = true
                    }
                }
                i++
            }
            bloque = false
            i = 1
            xPosPossible = this.xpos
            yPosPossible = this.ypos
            while(bloque != true && yPosPossible <= 8 && yPosPossible >= 1 && xPosPossible <= 8 && xPosPossible >= 1){
                xPosPossible = this.xpos - i
                yPosPossible = this.ypos + i
                if(xPosPossible <= 8 && xPosPossible >= 1 && yPosPossible <= 8 && yPosPossible >= 1 && (cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation.length == 0 || cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation[0].color != this.color)){
                    casePossible.push(posToName(xPosPossible, yPosPossible))
                }
                if(xPosPossible <= 8 && xPosPossible >= 1 && yPosPossible <= 8 && yPosPossible >= 1){
                    if(cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation.length != 0){
                        bloque = true
                    }
                }
                i++
            }
            bloque = false
            i = 1
            xPosPossible = this.xpos
            yPosPossible = this.ypos
            while(bloque != true && yPosPossible <= 8 && yPosPossible >= 1 && xPosPossible <= 8 && xPosPossible >= 1){
                xPosPossible = this.xpos - i
                yPosPossible = this.ypos - i
                if(xPosPossible <= 8 && xPosPossible >= 1 && yPosPossible <= 8 && yPosPossible >= 1 && (cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation.length == 0 || cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation[0].color != this.color)){
                    casePossible.push(posToName(xPosPossible, yPosPossible))
                }
                if(xPosPossible <= 8 && xPosPossible >= 1 && yPosPossible <= 8 && yPosPossible >= 1){
                    if(cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation.length != 0){
                        bloque = true
                    }
                }
                i++
            } 
        }
        if(this.name == "pawn"){
            if(this.color == "white"){
                if(this.ypos == 2){
                    for(i = 1; i <= 2; i++){
                        if(cases[caseNameStringList.indexOf(posToName(this.xpos, this.ypos + i))].utilisation.length == 0){
                            casePossible.push(posToName(this.xpos, this.ypos + i))
                        }
                    }
                }
                else if(this.ypos != 2 && cases[caseNameStringList.indexOf(posToName(this.xpos, this.ypos + 1))].utilisation.length == 0 && this.ypos < 8){
                    casePossible.push(posToName(this.xpos, this.ypos + 1))
                }
                if(this.xpos > 1){
                    if(cases[caseNameStringList.indexOf(posToName(this.xpos - 1, this.ypos + 1))].utilisation.length != 0){
                        if(cases[caseNameStringList.indexOf(posToName(this.xpos - 1, this.ypos + 1))].utilisation[0].color == "black"){
                            casePossible.push(posToName(this.xpos - 1, this.ypos + 1))
                        }
                    }
                }
                if(this.xpos < 8){
                    if(cases[caseNameStringList.indexOf(posToName(this.xpos + 1, this.ypos + 1))].utilisation.length != 0){
                        if(cases[caseNameStringList.indexOf(posToName(this.xpos + 1, this.ypos + 1))].utilisation[0].color == "black"){
                            casePossible.push(posToName(this.xpos + 1, this.ypos + 1))
                        }
                    }
                }
                     
            }
            if(this.color == "black"){
                if(this.ypos == 7){
                    for(i = 1; i <= 2; i++){
                        if(cases[caseNameStringList.indexOf(posToName(this.xpos, this.ypos - i))].utilisation.length == 0){
                            casePossible.push(posToName(this.xpos, this.ypos - i))
                        }
                    }
                }
                else if(this.ypos != 7 && cases[caseNameStringList.indexOf(posToName(this.xpos, this.ypos - 1))].utilisation.length == 0 && this.ypos < 8){
                    casePossible.push(posToName(this.xpos, this.ypos - 1))
                }
                if(this.xpos > 1){
                    if(cases[caseNameStringList.indexOf(posToName(this.xpos - 1, this.ypos - 1))].utilisation.length != 0){
                        if(cases[caseNameStringList.indexOf(posToName(this.xpos - 1, this.ypos - 1))].utilisation[0].color == "white"){
                            casePossible.push(posToName(this.xpos - 1, this.ypos - 1))
                        }
                    }
                }
                if(this.xpos < 8){
                    if(cases[caseNameStringList.indexOf(posToName(this.xpos + 1, this.ypos - 1))].utilisation.length != 0){
                        if(cases[caseNameStringList.indexOf(posToName(this.xpos + 1, this.ypos - 1))].utilisation[0].color == "white"){
                            casePossible.push(posToName(this.xpos + 1, this.ypos - 1))
                        }
                    }
                }           
            }
            
            
        }
        if(this.name == "king"){
            xPosPossible = this.xpos - 1
            yPosPossible = this.ypos
            if(xPosPossible > 1 && (cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation.length == 0 || cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation[0].color != this.color)){
                casePossible.push(posToName(xPosPossible, yPosPossible))
            }
            xPosPossible = this.xpos - 1
            yPosPossible = this.ypos + 1
            if(xPosPossible > 1 && yPosPossible < 8 && (cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation.length == 0 || cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation[0].color != this.color)){
                casePossible.push(posToName(xPosPossible, yPosPossible))
            }
            xPosPossible = this.xpos - 1
            yPosPossible = this.ypos - 1
            if(xPosPossible > 1 && yPosPossible > 1 && (cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation.length == 0 || cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation[0].color != this.color)){
                casePossible.push(posToName(xPosPossible, yPosPossible))
            }
            xPosPossible = this.xpos + 1
            yPosPossible = this.ypos
            if(xPosPossible < 8 && (cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation.length == 0 || cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation[0].color != this.color)){
                casePossible.push(posToName(xPosPossible, yPosPossible))
            }
            xPosPossible = this.xpos + 1
            yPosPossible = this.ypos - 1
            if(xPosPossible < 8 && yPosPossible > 1 && (cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation.length == 0 || cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation[0].color != this.color)){
                casePossible.push(posToName(xPosPossible, yPosPossible))
            }
            xPosPossible = this.xpos + 1
            yPosPossible = this.ypos + 1
            if(xPosPossible < 8 && yPosPossible < 8 && (cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation.length == 0 || cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation[0].color != this.color)){
                casePossible.push(posToName(xPosPossible, yPosPossible))
            }
            xPosPossible = this.xpos
            yPosPossible = this.ypos + 1
            if(yPosPossible < 8 && (cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation.length == 0 || cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation[0].color != this.color)){
                casePossible.push(posToName(xPosPossible, yPosPossible))
            }
            xPosPossible = this.xpos
            yPosPossible = this.ypos - 1
            if(yPosPossible > 1 && (cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation.length == 0 || cases[caseNameStringList.indexOf(posToName(xPosPossible, yPosPossible))].utilisation[0].color != this.color)){
                casePossible.push(posToName(xPosPossible, yPosPossible))
            }
            if(cases[caseNameStringList.indexOf(posToName(8, this.ypos))].utilisation.length != 0){
                if(this.hasNotMoved && (cases[caseNameStringList.indexOf(posToName(8, this.ypos))].utilisation[0].hasNotMoved) && (cases[caseNameStringList.indexOf(posToName(7, this.ypos))].utilisation.length == 0 && cases[caseNameStringList.indexOf(posToName(6, this.ypos))].utilisation.length == 0)){
                    casePossible.push(posToName(7, this.ypos))
                }
            }
            if(cases[caseNameStringList.indexOf(posToName(1, this.ypos))].utilisation.length != 0){
                if(this.hasNotMoved && (cases[caseNameStringList.indexOf(posToName(1, this.ypos))].utilisation[0].hasNotMoved) && (cases[caseNameStringList.indexOf(posToName(2, this.ypos))].utilisation.length == 0 && cases[caseNameStringList.indexOf(posToName(3, this.ypos))].utilisation.length == 0) && cases[caseNameStringList.indexOf(posToName(4, this.ypos))].utilisation.length == 0){
                    casePossible.push(posToName(3, this.ypos))
                }
            }

        }

    return(casePossible)


    }

    getLegalMove(){
        let legalMoves = []
        let oldxpos = this.xpos
        let oldypos = this.ypos
        let oldUsage
        let possibleMove = this.trouverCasePossible()
        let pieceCapturePossible
        for(i in possibleMove){
            this.xpos = nameToxpos(possibleMove[i])
            this.ypos = nameToypos(possibleMove[i])
            cases[caseNameStringList.indexOf(posToName(oldxpos, oldypos))].utilisation = []
            oldUsage = cases[caseNameStringList.indexOf(posToName(this.xpos, this.ypos))].utilisation
            cases[caseNameStringList.indexOf(posToName(this.xpos, this.ypos))].utilisation = [this]
            
            pieceCapturePossible = pieces.filter(function(x) { return x !== oldUsage[0]; }); //cette partie du code est grandement inspirée de https://stackoverflow.com/questions/15361189/how-to-select-all-other-values-in-an-array-except-the-ith-element 

            if(isKingChecked(this.color, pieceCapturePossible) == false){
                legalMoves.push(posToName(this.xpos, this.ypos))
            }
            cases[caseNameStringList.indexOf(posToName(oldxpos, oldypos))].utilisation = [this]
            cases[caseNameStringList.indexOf(posToName(this.xpos, this.ypos))].utilisation.splice(cases[caseNameStringList.indexOf(posToName(this.xpos, this.ypos))].utilisation.length-1, 1)
            cases[caseNameStringList.indexOf(posToName(this.xpos, this.ypos))].utilisation = oldUsage
        }
       
        this.xpos = oldxpos
        this.ypos = oldypos
        return(legalMoves)
    }

    promotion(){ //la promotion donne directement une reine, par soucis de temps
        if(this.name == "pawn"){
            if(this.ypos == 1){
                this.symbol = '\u265B'
                this.name = "queen"
                deplacement(this, posToName(this.xpos, this.ypos))
            }
            else if(this.ypos == 8){
                this.symbol = '\u2655'
                this.name = "queen"
                deplacement(this, posToName(this.xpos, this.ypos))  
            }
            
        }
    }
}

//classe case qui définit toute les cases de plateau et un bout de code qui créer les 64 cases

class Case{
    constructor(name){
        this.name = name
        this.utilisation = []
        this.xpos = nameToxpos(name)
        this.ypos = nameToypos(name)
    }
}

var cases = []
var caseNameStringList = []
let chiffreCase;
let lettreCase;
let caseName
for(i = 1; i <= 64; i++){
    if(i % 8 != 0){
        chiffreCase = i % 8
    }else{
        chiffreCase = 8
    }
    lettreCase = String.fromCharCode((i-chiffreCase)/8+97)
    caseName = lettreCase + chiffreCase;
    cases[i-1] = new Case(caseName)
    caseNameStringList[i-1] = cases[i-1].name
}

//bout de code qui permet le jeu et l'interaction avec les elements HTML

let caseSelect
let pieceSelect;
var tour = "white"
var caseAffichee = false
let casePossiblePieceSelect
let end = false


document.addEventListener('click', (e) =>
    {
      let elementId = e.target.id;
      
      if(elementId !== '') {
        if(!caseAffichee){
            caseSelect = cases[caseNameStringList.indexOf(elementId)]
            if(caseSelect.utilisation.length == 1){
                if(caseSelect.utilisation[0].color == tour){
                    pieceSelect = caseSelect.utilisation[0]
                    casePossiblePieceSelect = pieceSelect.getLegalMove()
                    casePossiblePieceSelect.forEach(element => {
                        document.getElementById(element).style.backgroundColor = boardThemes[throughTheme % boardThemes.length].moveColor
                    });
                    caseAffichee = true
                }  
            }
        }
        else{
            if(casePossiblePieceSelect.includes(elementId)){
                if(pieceSelect.name == "king" && pieceSelect.hasNotMoved && elementId == posToName(7, pieceSelect.ypos)){
                    deplacement(cases[caseNameStringList.indexOf(posToName(8, pieceSelect.ypos))].utilisation[0], posToName(6, pieceSelect.ypos))
                }
                if(pieceSelect.name == "king" && pieceSelect.hasNotMoved && elementId == posToName(3, pieceSelect.ypos)){
                    deplacement(cases[caseNameStringList.indexOf(posToName(1, pieceSelect.ypos))].utilisation[0], posToName(4, pieceSelect.ypos))
                }
                deplacement(pieceSelect, elementId)
                boardThemes[throughTheme % boardThemes.length].initColor()
                caseAffichee = false
                

                if(tour == "white"){
                    tour = "black"
                }
                else{
                    tour = "white"
                }

                if(isThereEnd(tour, "checkmate")){
                    end = true
                    if(tour == "white"){
                        indicateur.innerHTML = "black won by checkmate"
                    }
                    else{
                        indicateur.innerHTML = "white won by checkmate"
                    }  
                }
                if(isThereEnd(tour, "stalemate")){
                    end = true
                    indicateur.innerHTML = "draw by stalemate"
                }

                if(end != true){
                    indicateur.innerHTML = tour + " to play"
                }
                
            }
            else{
                boardThemes[throughTheme % boardThemes.length].initColor()
                caseAffichee = false
            }
            
        }
          
      }
    }
  );

  //la base de ce code vient de: https://makersaid.com/id-of-clicked-dom-element-javascript/


  //creation pieces

  function creationPiece(xpos, ypos, color, symbol, name){
    pieces[pieces.length] = new piece(xpos, ypos, color, symbol, name)
  }

let pieces = new Array
for(let i = 1; i <= 8; i++){
    creationPiece(i, 2, "white", '\u2659', "pawn")
}
for(let i = 1; i <= 8; i++){
    creationPiece(i, 7, "black", '\u265F', "pawn")
}

creationPiece(1, 1, "white", '\u2656', "rook")
creationPiece(8, 1, "white", '\u2656', "rook")
creationPiece(1, 8, "black", '\u265C', "rook")
creationPiece(8, 8, "black", '\u265C', "rook")

creationPiece(2, 1, "white", '\u2658', "knight")
creationPiece(7, 1, "white", '\u2658', "knight")
creationPiece(2, 8, "black", '\u265E', "knight")
creationPiece(7, 8, "black", '\u265E', "knight")

creationPiece(3, 1, "white", '\u2657', "bishop")
creationPiece(6, 1, "white", '\u2657', "bishop")
creationPiece(3, 8, "black", '\u265D', "bishop")
creationPiece(6, 8, "black", '\u265D', "bishop")

creationPiece(4, 1, "white", '\u2655', "queen")
creationPiece(4, 8, "black", '\u265B', "queen")

creationPiece(5, 1, "white", '\u2654', "king")
creationPiece(5, 8, "black", '\u265A', "king")

//fonction de deplacement

function deplacement(piece, newPlace){
    if(cases[caseNameStringList.indexOf(newPlace)].utilisation.length != 0){
        pieces.splice(pieces.indexOf(cases[caseNameStringList.indexOf(newPlace)].utilisation[0]), 1)
    }
    cases[caseNameStringList.indexOf(posToName(piece.xpos, piece.ypos))].utilisation = []
    document.getElementById(piece.casePos).innerHTML = ""
    document.getElementById(newPlace).innerHTML = piece.symbol
    piece.xpos = nameToxpos(newPlace)
    piece.ypos = nameToypos(newPlace)
    piece.casePos = newPlace
    cases[caseNameStringList.indexOf(newPlace)].utilisation[0] = piece
    piece.hasNotMoved = false
    piece.promotion()
}

//fonction onlaod qui permet de changer le contenu des elements HTML dès qu'ils ont chargés (je n'ai plus la source pour ce window.onlaod mais je me rapelle qu'il vient de https://stackoverflow.com/)

window.onload = function() {
    for(i in pieces){
        let pieceInit = pieces[i]
        deplacement(pieceInit, posToName(pieceInit.xpos, pieceInit.ypos))
        pieces[i].hasNotMoved = true
    }
    const indicateur = document.getElementById("indicateur")

};


