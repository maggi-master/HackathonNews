import { initializeApp } from 'https://www.gstatic.com/firebasejs/9.17.1/firebase-app.js';
import { getAuth, signInWithEmailAndPassword } from 'https://www.gstatic.com/firebasejs/9.17.1/firebase-auth.js';

// Fetch Firebase config from the backend
fetch('/firebase-config')
    .then(response => response.json())
    .then(firebaseConfig => {
        const app = initializeApp(firebaseConfig);
        const auth = getAuth(app);

        document.getElementById('login-form').addEventListener('submit', function(event) {
            event.preventDefault();
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;

            signInWithEmailAndPassword(auth, email, password)
                .then(async (userCredential) => {
                    const user = userCredential.user;
                    const idToken = await user.getIdToken();

                    fetch('/validate-token', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ idToken })
                    })
                    .then(response => response.json())
                    .then(data => {
                        if (data.success) {
                            window.location.href = '/settings';
                        } else {
                            alert('Authentication failed!');
                        }
                    })
                    .catch(error => console.error('Error sending token:', error));
                })
                .catch(error => alert('Login failed: ' + error.message));
        });
    })
    .catch(error => console.error('Error fetching Firebase config:', error));
