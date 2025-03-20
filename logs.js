


// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCzNPOIvNkGb_mXK1obLRRmb3bpJYc-QKY",
  authDomain: "nyhetsprosjekt.firebaseapp.com",
  projectId: "nyhetsprosjekt",
  storageBucket: "nyhetsprosjekt.firebasestorage.app",
  messagingSenderId: "20490355410",
  appId: "1:20490355410:web:f06588ed2e96e6f298a30b",
  measurementId: "G-T51P8D3EZ9"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);



const takkemeldingEl = document.querySelector("#takkemelding")
const emailEl = document.querySelector("#email")
const abonnerEl = document.querySelector("#abonnerKnapp")
const params1 = createMap()



//transformData()
getInfo()
//abonnerEl.addEventListener("click", saveEmailAndAbonomangInJson)

function createMap() {
    let qs = decodeURIComponent(location.search.substring(1)); //alt dette er for å definere 
    let params = new Map();
    let parts = qs.split("&")
    parts.forEach((part) => {
        let key = part.split("=")[0];
        let val = part.split("=")[1];
        params.set(key, val);
    });

    console.log("dit");
    console.log(params);
    return params
}

function getInfo() {
    takkemeldingEl.textContent = `thank you for logging into Nova, and to verify is this your email?`;
    emailEl.textContent = `${params1.get("email")}`
} //Etter verfiy email, lagre email i database





/*
function transformData() {
    let data2 = fetch('./data.json') // Use the correct path to your JSON file
        .then(response => response.json()) // Convert response to JSON
        .then(data => console.log(data))   // Use the JSON data
        .catch(error => console.error("Error fetching JSON:", error));
    
    return data2
}

function saveEmailAndAbonomangInJson() {
    let data = transformData()
    console.log(data);
    
    console.log(params1.get("email"));
    
    data[params1.get('email')] = true
    let jsonData = JSON.stringify(data)
    console.log(jsonData)
    fs.writeFile("data.json", jsonData)
    
}

*/
