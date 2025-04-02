from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from database import ServerFirebaseConfig, ClientFirebaseConfig, FirebaseHandler
from firebase_admin import auth, exceptions
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

config_db = ServerFirebaseConfig()
db = FirebaseHandler(config_db)

@app.route('/firebase-config', methods=['POST'])
def get_firebase_config():
    client_config = ClientFirebaseConfig()
    return jsonify(client_config.get_credentials())

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    feedback = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        password2 = request.form['password2']
        if password != password2:
            feedback = {"type":"error", "message":"Begge passord må være like"}
        else:
            try:
                user_record = auth.create_user(email=email, password=password)
                user_id = user_record.uid
                db.write_user_data(user_id, {
                    "email": email,
                    "tags": [],
                    "verified": False
                })
                feedback = {'type':"success", 'message': "Bruker opprettet"}
            except ValueError:
                feedback = {'type':"error", 'message':"Ugyldig e-post eller passord (minimum 6 tegn)."}
            except exceptions.FirebaseError:
                feedback = {'type':"error", 'message':"Bruker opptatt"}
    return render_template('register.html', feedback=feedback)

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
        return 'True'
    except Exception:
        return 'False'

@app.route('/user-data', methods=['POST'])
def get_data():
    user_id = session.get('user')
    user_data = db.get_user_data(user_id)
    return jsonify(user_data)

@app.route('/settings', methods=["GET", "POST"])
def settings():
    user_id = session.get('user')
    if not user_id:
        return redirect(url_for('login'))
    return render_template('settings.html')

@app.route('/save-data', methods=['POST'])
def save_data():
    try:
        user_id = session.get('user')
        data = request.get_json()
        db.write_user_data(user_id, data)
        return 'True'
    except Exception:
        return 'False'

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0",)