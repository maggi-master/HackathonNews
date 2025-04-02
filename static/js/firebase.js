import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
import { getAuth, signInWithEmailAndPassword } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";

async function initFirebase() {
    try {
        const response = await fetch('/firebase-config', { method: 'POST' });
        const firebaseConfig = await response.json();
        const firebaseApp = initializeApp(firebaseConfig);
        return getAuth(firebaseApp);
    } catch (error) {
        console.error("Firebase init-feil:", error);
    }
}

const auth = await initFirebase();

document.getElementById('login-form').addEventListener('submit', async (event) => {
    event.preventDefault();
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const errorMessageEl = document.getElementById('error-message');
    errorMessageEl.textContent = '';
    try {
        const userCredential = await signInWithEmailAndPassword(auth, email, password);
        const idToken = await userCredential.user.getIdToken();
        const tokenResponse = await fetch('/validate-token', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ idToken })
        });

        const validation = await tokenResponse.text();
        if (validation === "True") {
            window.location.href = '/settings';
        } else {
            errorMessageEl.textContent = 'Klarte ikke verifisere.';
        }
    } catch (error) {
        const errorMessageEl = document.getElementById('error-message');
        errorMessageEl.textContent = "Feil e-post eller passord";
    }
});
