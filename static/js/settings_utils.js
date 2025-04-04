
const tags = [
    "Politikk", "Samfunn", "Økonomi", "Krig", "Helse", "Klima", "Miljø", "Teknologi", "Vitenskap", "Utdanning",
    "Kriminalitet", "Kultur", "Sport", "Internasjonalt", "Arbeid", "Reise", "Mat", "Livsstil", "Religion", "Historie",
  
    "Justis", "Næring", "Skole", "Forskning", "Energi", "Sikkerhet", "Ulykker", "Media", "Valg", "Diplomati",
    "Konflikt", "Forsvar", "Skatt", "Handel", "Fattigdom", "Inflasjon", "Bank", "Finans", "Aksjer", "Børs",
  
    "IT", "Mobil", "Internett", "Kunstig", "Intelligens", "Robotikk", "Medisin", "Psykologi", "Vaksine", "Pandemi",
    "Sykehus", "Kreft", "Kosthold", "Trening", "Natur", "Forurensning", "Bærekraft", "Fornybar", "Olje", "Gass",
  
    "Transport", "Vei", "Tog", "Fly", "Båt", "Bygg", "Bolig", "Leie", "Eiendom", "Lån",
    "Ungdom", "Barn", "Foreldre", "Likestilling", "Minoriteter", "Diskriminering", "Ytring", "Demokrati", "Ytringsfrihet", "Rettigheter",
  
    "Skolegang", "Karakterer", "Studier", "Universitet", "Eksamen", "Lærer", "Student", "Elever", "Pensjon", "Arbeidsledighet",
    "Streik", "Lønn", "Jobb", "Stillinger", "Bedrift", "Gründere", "Oppstart", "Innovasjon", "Militær", "Terror",
  
    "Etikk", "Moral", "Kunst", "Film", "TV", "Musikk", "Teater", "Litteratur", "Spill", "Serier",
    "Festival", "Kjendis", "Mote", "Design", "Foto", "Arkitektur", "Språk", "Tradisjon", "Museum", "Scene",
  
    "Fotball", "Håndball", "Ski", "Sykkel", "Friidrett", "Basket", "Tennis", "Svømming", "E-sport", "OL",
    "VM", "EM", "Kamp", "Turnering", "Seier", "Tap", "Supporter", "Dommer", "Lag", "Spiller",
  
    "USA", "Kina", "Russland", "Norge", "Europa", "Asia", "Afrika", "Midtøsten", "Verden", "FN",
    "EU", "NATO", "Statsbudsjett", "Skog", "Dyreliv", "Art", "Økosystem", "Resirkulering", "Plast", "Hav",
  
    "Drap", "Tyveri", "Vold", "Trusler", "Svindel", "Hacking", "Overgrep", "Mistenkt", "Etterforskning", "Domstol",
    "Rettssak", "Lov", "Paragraf", "Straff", "Advokat", "Politi", "Fengsel", "Rettsvesen", "Tiltale", "Anke",
  
    "Innvandring", "Asyl", "Flyktninger", "Grense", "Statsborgerskap", "Valgfusk", "Propaganda", "Sensur", "Overvåking", "Personvern",
    "Netthets", "Sosiale", "Medier", "Kommentar", "Debatt", "Satire", "Kritikk", "Kronikk", "Rapport", "Analyse",
  
    "Trender", "Tidsånd", "Subkultur", "Generasjon", "Digitalt", "Dataspill", "Streaming", "Youtube", "TikTok", "Influencer",
    "Podcast", "Blogg", "Nettside", "App", "Utvikling", "Koding", "Datasikkerhet", "Sky", "Programvare", "Maskinvare",
  
    "Solenergi", "Vindkraft", "Batteri", "Lading", "Elbil", "Hydrogen", "Kull", "Kjernekraft", "Strøm", "Pris",
    "Budsjett", "Velferd", "Trygd", "NAV", "Barnevern", "Eldre", "Omsorg", "Hjem", "Institusjon", "Frivillighet",
  
    "Penger", "Gull", "Valuta", "Krypto", "Bitcoin", "Investering", "Fond", "Gjeld", "Skulder", "Sparing",
    "Prisvekst", "Renter", "Boliglån", "Markeder", "Import", "Eksport", "Toll", "Avtale", "Sanksjoner", "Økonomisk",
  
    "Jordbruk", "Fiskeri", "Skogbruk", "Matproduksjon", "Dyrevelferd", "Landbruk", "Avling", "Korn", "Kjøtt", "Meieri",
    "Vegetar", "Vegan", "Oppskrift", "Restaurant", "Kafé", "Servering", "Kunde", "Marked", "Handel", "Shopping",
  
    "Psykisk", "Helsevern", "Terapi", "Diagnose", "Behandling", "Legemidler", "Apotek", "Pårørende", "Selvmord", "Rus",
    "Avhengighet", "Alkohol", "Narkotika", "Røyking", "Snus", "Skader", "Utskrivning", "Sykehjem", "Fastlege", "Helsepersonell",
  
    "Fangst", "Jakt", "Vær", "Storm", "Flom", "Brann", "Skred", "Naturkatastrofe", "Beredskap", "Evakuering",
    "Varsel", "Krisesituasjon", "Hjelp", "Redning", "Sivilforsvar", "Miljøvern", "Naturressurser", "Bevaring", "Felt", "Forvaltning",
  
    "Frihet", "Undertrykkelse", "Korrupsjon", "Protest", "Demonstrasjon", "Motstand", "Reform", "Revolusjon", "Opprør", "Sensitivt",
    "Krise", "Leder", "President", "Statsminister", "Konge", "Dronning", "Monarki", "Republikk", "Regjering", "Parlament"
  ].sort();

let showLimit = 50;
let extended = false
const tagsContainer = document.getElementById("tags-container");
const selectedTagsContainer = document.getElementById("selected-tags");
const searchInput = document.getElementById("search");
const saveButton = document.getElementById("save-button")
const deleteButton = document.getElementById("delete-button")
let userData = await fetchUserData()

async function fetchUserData() {
    try {
        const response = await fetch('user-data', { method: 'POST' })
        const userData = await response.json()
        return userData
    } catch (error) {
        console.error("Error loading data:", error);
    }
}

async function deleteAccount() {
    try {
        const response = await fetch('delete-data', {method: 'POST'})
        window.location.href = '/'
    } catch (error) {
        console.error("Error deleting data:", error);
    }
}

async function saveUserData() {
    try {
        const response = await fetch('/save-data', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(userData)
        });
    } catch (error) {
        console.error("Error saving data:", error);
    }
}

function renderTags(filter = "") {
    const tagsList = tags.filter(tag => tag.toLowerCase().includes(filter.toLowerCase()));
    let limitedTagsList = tagsList
    if (extended) {
        extended = false
    } else {
        limitedTagsList = tagsList.slice(0, showLimit)
    };
    tagsContainer.innerHTML = "";
    limitedTagsList.forEach(tag => {
        const tagElement = document.createElement("div");
        tagElement.className = "tag-box";
        tagElement.textContent = tag;
        tagElement.onclick = () => selectTag(tag);
        tagsContainer.appendChild(tagElement);
    });
    const extraTags = tagsList.length-limitedTagsList.length
    if (extraTags != 0) {
        const moreElement = document.createElement("div")
        moreElement.className = "more-box";
        moreElement.textContent = `+ ${extraTags}`
        moreElement.onclick = () => {
            extended = true
            renderTags()
        }
        tagsContainer.appendChild(moreElement);
    }
    

}

function selectTag(tag) {
    if (!userData.tags.includes(tag)) {
        userData.tags.push(tag);
        updateSelectedTags();
    }
}

function updateSelectedTags() {
    selectedTagsContainer.innerHTML = "";
    userData.tags.sort().forEach(tag => {
        const tagElement = document.createElement("div");
        tagElement.className = "tag-box";
        tagElement.textContent = tag;
        tagElement.onclick = () => removeTag(tag);
        selectedTagsContainer.appendChild(tagElement);
    });
}

function removeTag(tag) {
    userData.tags = userData.tags.filter(t => t !== tag);
    updateSelectedTags();
}

searchInput.addEventListener("input", (e) => renderTags(e.target.value));
renderTags();
updateSelectedTags();
saveButton.addEventListener("click", saveUserData)
deleteButton.addEventListener("click", deleteAccount)