
const Elglider = document.querySelector("#glider")
const ElgliderLabel = document.querySelector("#gliderLabel")
Elglider.addEventListener("change", update)



function update() {
    ElgliderLabel.innerHTML = `Antallpersoner: ${Elglider.value}`
}
let dict = {"blue": "green"}








