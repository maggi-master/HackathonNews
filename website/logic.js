//const { ChatSession } = require("firebase/vertexai")
const abonnerEl = document.querySelector("#abonnerKnapp")
const gmailEl = document.querySelector("#gmail")
const chosenThemesEl = document.querySelector("#chosenThemes")
const themesEl = document.querySelectorAll(".tema")


abonnerEl.addEventListener("click", abonner)
for (let i = 0; i < themesEl.length; i++) {
    themesEl[i].addEventListener("click", createDiv)
}



function abonner() {
    console.log("Gmail:", gmailEl.value)//gmailen som kan bli lagret i database, men må lage en funksjon som sjekker om det er en gyldig gmail.
    let lagredeTema = LagreTema()
    console.log("Temaer:", lagredeTema)
}

function LagreTema() {
    let newBoxList = document.querySelectorAll(".newBox")
    let stringBox = []
    for (let i = 0; i < newBoxList.length; i++) {
        stringBox.push(newBoxList[i].innerHTML)
    };
    return stringBox
}



function createDiv(e) {
    let newBoxList = document.querySelectorAll(".newBox")
    let go = true
    let clickeddoor = e.target
    for (let i = 0; i < newBoxList.length; i++) {
        //check if it has same name as another box
        if (newBoxList[i].innerHTML == clickeddoor.innerHTML) {
            go = false
        }
    }
    if (go) {
        console.log("can make another")
        let newBox = document.createElement("div")
        newBox.className = "newBox"
        newBox.textContent = clickeddoor.innerHTML
        chosenThemesEl.appendChild(newBox)
        updateNewBoxes() //oppdaterer evenlistener etter lagt til box
    } else {console.log("couldnt make another of the same")}
    
}

function updateNewBoxes() {
    let boxesEl = document.querySelectorAll(".newBox")
    for (let i = 0; i < boxesEl.length; i++) {
        boxesEl[i].addEventListener("click", removeDiv)
    }
    
}

function removeDiv(e) {
    chosenThemesEl.removeChild(e.target)
}

