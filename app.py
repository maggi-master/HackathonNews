from flask import Flask, render_template, request, jsonify, session, flash, redirect, url_for
from database import ServerFirebaseConfig, ClientFirebaseConfig, FirebaseHandler
from firebase_admin import auth
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

config_db = ServerFirebaseConfig()
db = FirebaseHandler(config_db)

@app.route('/firebase-config')
def get_firebase_config():
    client_config = ClientFirebaseConfig()
    return jsonify(client_config.get_credentials())

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user_record = auth.create_user(email=email, password=password)
            user_id = user_record.uid
            db.write_user_data(user_id, {
                "email":email,
                "tags":[],
                "verified":False
            })
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            flash(f'Error: {str(e)}', 'error')
            return redirect(url_for('register'))

    return render_template('register.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    if 'user' in session:
        return redirect(url_for('settings'))
    return render_template('login.html')

@app.route('/validate-token', methods=['POST'])
def validate_token():
    try:
        data = request.get_json()
        id_token = data.get('idToken')
        decoded_token = auth.verify_id_token(id_token)
        uid = decoded_token['uid']

        session['user'] = uid
        return jsonify({'success': True, 'uid': uid}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

@app.route('/settings')
def settings():
    user_id = session.get('user')
    if not user_id:
        return redirect(url_for('login'))

    user = db.get_user_data(user_id)
    return render_template('settings.html', user=user)

if __name__ == "__main__":
    app.run(debug=True)