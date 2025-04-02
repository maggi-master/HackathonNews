
const tags = [
    "Sult", "Klimaendringer", "Økonomisk krise", "Teknologisk innovasjon", "Arbeidsledighet", 
    "COVID-19 vaksine", "Ukrainakonflikten", "Kunstig intelligens", "Kunstige kjøretøy", "Romforskning", 
    "Psykisk helse", "Bærekraft", "Digitalisering", "Sosial ulikhet", "Økologisk landbruk", 
    "Klimaforandringer", "Byutvikling", "Frivillighet", "Sosiale medier", "Matvaresikkerhet", 
    "Global helse", "Høye strømpriser", "Personvern", "Migrasjon", "Skogvern", 
    "Nettkriminalitet", "Fattigdom", "Høyere utdanning", "Forurensning", "Internett-regulering", 
    "Kjernefysisk energi", "Kreftbehandling", "Dyr på rødlista", "Dyrevelferd", "Vannmangel", 
    "Fornybar energi", "Helsevesen", "Ferie", "Kulturarv", "Globalisering", 
    "Terrorisme", "Tjenesteyting", "Turisme", "Sårbare samfunn", "Høsttørke", 
    "Nordlys", "Beredskap", "Naturkatastrofer", "Kjønnsroller", "Ulike livssyn", 
    "Transportrevolusjon", "Arktis", "Fjernarbeid", "Velferdssystem", "Menneskerettigheter", 
    "Valg", "Bærekraftig mote", "Geopolitikk", "Energikrise", "Urbanisering", 
    "Fattigdom i verden", "Sykdomsforebygging", "Miljøbevissthet", "Tegn på politisk polarisering", "Flyktningkrise", 
    "Terrorisme", "Arbeidstakere i streik", "Internasjonale handelsavtaler", "Kunstig mat", 
    "Fremtidens utdanning", "Mental helse på arbeidsplassen", "Solenergi", "Elektromobilitet", 
    "Kunstig intelligens i medisin", "Det digitale skille", "Global matvarekrise", "Armeeliv", 
    "Kjemikalier i landbruket", "Hjemløshet", "Folkehelse", "Styrking av demokrati", 
    "Fiskeindustriens fremtid", "Verdens befolkning", "Havnebyer", "Skatt", 
    "Framtidens arbeid", "Sult i verden", "Skogplanting", "Vannforvaltning", "Fornybar energi", 
    "Politisk makt", "Forurensning i havet", "Seksuell trakassering", "Vekst i urbane områder", 
    "Oljeforbruk", "Elderpleie", "Atomenergi", "Sivilisasjonens utfordringer", "Veldedighet", 
    "Fossile brensler", "Utslipp", "Dyrking av mat", "Gasskraft", "Klimapolitikk", 
    "Sosial boligbygging", "Sosialt entreprenørskap", "Kultur", "Kjappe nyheter", 
    "Helsetjenester", "Digital suksess", "Arbeidsmarked", "Pengepolitikk", "Internasjonalt samarbeid", 
    "Helsepersonell", "Fremmedfrykt", "Gjeld", "Luftforurensning", "Fremtidens mat", 
    "Datavern", "Billig transport", "Sikkerhetspolitikk", "Varmerekord", "Internasjonale konflikter", 
    "Bærekraftige byer", "Grønne byer", "Redusert matsvinn", "Ny teknologi", 
    "Gjeldskriser", "Digital utdanning", "Autonome kjøretøy", "Bygging av skoler", "Vanskelig med migrasjon", 
    "Internett-hat", "Skogvern", "Solceller", "Arbeidstid", "Rettferdig handel", 
    "Frivillig arbeid", "Luftkvalitet", "Energieffektivisering", "Grønne jobber", 
    "Nettverksangrep", "Oljeboring", "Klimatilpasning", "Redusert plastbruk", 
    "Fattigdom i Europa", "Utvikling av landbruk", "Velferdsstaten", "Vold mot kvinner", 
    "Psykologisk førstehjelp", "Ressursforvaltning", "Nedbrytbare materialer", "Skolemat", 
    "Tidsfordriv", "Koronafest", "Organisk mat", "Vannkraft", "Tropisk skog", 
    "Trender innen teknologi", "Vikinghistorie", "Grønne byer", "Klimaavtaler", 
    "Internett-abonnement", "Kulturfestivaller", "Planter som mat", "Fjernvarme", 
    "Romfartsnyheter", "Bærekraftige løsninger", "Elektriske båter", "Kampen mot ekstremisme", 
    "Virkningen av teknologi på mental helse", "Energieffektiv boligbygging", "Kostnadene ved klimaendringer", 
    "Politiske manifest", "Hverdagsforurensning", "Turistmaskin", "Grønne investeringer", 
    "Den digitale tidsalder", "Menneskelig psykologi", "Urbane gartneri", "Digital medisin", 
    "Finansielle verktøy", "Digital transformasjon", "Kjønnsforskning", "Eksportmuligheter", 
    "Verdens hav", "Reforestation", "Langsiktig økonomisk politikk", "Teater", 
    "Sykkeltransport", "Bærekraftige klær", "Urbane landskap", "Skapelse av bærekraftige økonomier", 
    "Kritiske helseproblemer", "Motivasjon", "Inkludering i utdanning", "Frivillige organisasjoner", 
    "Industriell utvikling", "Kulturhistorie", "Arven etter forfedrene", "Dynamisk læring", 
    "Genetisk forskning", "Byggearbeid", "Tidsreise", "Teorier om kunst", 
    "Klimaavtaler", "Internasjonale diplomater", "Framtiden for grønne byer", 
    "Hjelp til utviklingsland", "Spørsmål om digitalisering", "Fremtidens kommunikasjon"
  ].sort();

let showLimit = 50;
let extended = false
const tagsContainer = document.getElementById("tags-container");
const selectedTagsContainer = document.getElementById("selected-tags");
const searchInput = document.getElementById("search");
const saveButton = document.getElementById("save-button")
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