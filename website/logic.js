const themeBoxEl = document.querySelector("#temabox")
const themes = [
    "Politikk",
    "Økonomi",
    "Sport",
    "Kultur",
    "Teknologi",
    "Helse",
    "Utdanning",
    "Miljø",
    "Kriminalitet",
    "Samfunn",
    "Internasjonale nyheter",
    "Vitenskap",
    "Underholdning",
    "Reise",
    "Mat og drikke",
    "Arbeidsmarked",
    "Boligmarked",
    "Transport",
    "Klimaendringer",
    "Forskning",
    "Digitalisering",
    "Medier og journalistikk",
    "Sosiale medier",
    "Energipolitikk",
    "Industri og næringsliv",
    "Forsvar og sikkerhet",
    "Internett og personvern",
    "Teknologiutvikling",
    "Ulykker og katastrofer",
    "Naturkatastrofer",
    "Terrorisme",
    "Flyktninger og migrasjon",
    "Utenrikspolitikk",
    "Lokale nyheter",
    "Kunst og design",
    "Litteratur",
    "Musikk",
    "Film og TV",
    "Spill og e-sport",
    "Trender og livsstil",
    "Familie og oppvekst",
    "Psykisk helse",
    "Medisin og behandling",
    "Dyr og naturvern",
    "Religiøse spørsmål",
    "Menneskerettigheter",
    "Kriger og konflikter",
    "Teknologiske innovasjoner",
    "Historie og arkeologi",
    "Kunstig intelligens",
    "Personlig økonomi"
  ]
loadBoxes()
//const { ChatSession } = require("firebase/vertexai")
const abonnerEl = document.querySelector("#abonnerKnapp")
const gmailEl = document.querySelector("#gmail")
const chosenThemesEl = document.querySelector("#chosenThemes")
const themesEl = document.querySelectorAll(".tema")
const searchEl = document.querySelector("#search")



searchEl.addEventListener("input", search)
abonnerEl.addEventListener("click", abonner)
for (let i = 0; i < themesEl.length; i++) {
    themesEl[i].addEventListener("click", createDiv)
}


function loadBoxes() {//Loads the themes in at the start of ur code. 
    for (let i = 0; i < themes.length; i++) {
        let temaBox = document.createElement("div")
        temaBox.classList.add("tema")
        temaBox.innerHTML = `${themes[i]}`
        themeBoxEl.appendChild(temaBox)
    }
}

function search() {//Lets you search through the themes
    let søket = searchEl.value.toLowerCase()
    for (let i = 0; i < themesEl.length; i++) {
        let text = themesEl[i].innerHTML.toLowerCase()
        if (text.includes(søket)) {
            themesEl[i].classList.remove("notSearched")
        } else {
            themesEl[i].classList.add("notSearched")
        }
    }
}


function abonner() {
    let lagredeTema = LagreTema()
    console.log("Temaer:", lagredeTema)
}

function LagreTema() {//Saves the themes the user has chosen
    let newBoxList = document.querySelectorAll(".newBox")
    let stringBox = []
    for (let i = 0; i < newBoxList.length; i++) {
        stringBox.push(newBoxList[i].innerHTML)
    };
    return stringBox
}


/*
function createDiv(e) {
    let clickeddoor = e.target
    if (clickeddoor.classList.contains("newBox")) {
        console.log("can make another")
        clickeddoor.classList.remove("newBox")
        clickeddoor.classList.add("tema")
    } else {
        clickeddoor.classList.add("newBox"); clickeddoor.classList.remove("tema")};
    
}
*/
