import firebase_admin
from firebase_admin import credentials, firestore, auth
import logging as log
from .server_firebase_config import ServerFirebaseConfig

class FirebaseHandler:
    _initialized = False
    def __init__(self, config:ServerFirebaseConfig) -> None:
        self._logger = log.getLogger(__name__)
        self._logger.setLevel(log.ERROR)

        if not FirebaseHandler._initialized:
            self._credentials = credentials.Certificate(config.get_credentials())
            firebase_admin.initialize_app(self._credentials)
            FirebaseHandler._initialized = True

        self._database = firestore.client()
        self._users_ref = self._database.collection("users")

    def _get_user_ref(self, user_id:str):
        """Fetches and returns user refrence."""
        return self._users_ref.document(user_id)
    
    def get_user_id(self, id_token): #missing error handling
        """Fetches and returns user ID from provided login."""
        decoded_token = auth.verify_id_token(id_token)
        uid = decoded_token['uid']
        return uid
        
    def get_user_data(self, user_id:str) -> (dict|None):
        """Fetches and returns user data if stored, else returns nothing."""
        user_ref = self._get_user_ref(user_id)
        doc = user_ref.get()
        if doc.exists:
            return doc.to_dict()
        else:
            self._logger.info(f"Error fetching data, userID: {user_id} not found")
            return None
        
    def write_user_data(self, user_id:str, data:dict) -> None: #missing error handling
        """Writes data to user using corresponding user ID."""
        user_ref = self._get_user_ref(user_id)
        user_ref.set(data)

    def get_all_users(self) -> list[dict]:
        """Fetches data from all users and returns it as a list."""
        users_ref = self._database.collection('users')
        users = users_ref.stream()
        user_list = [user.to_dict() for user in users]
        return user_list
    
    def delete_user(self, user_id:str) -> None:
        """Deletes all data connected to user ID."""
        user_ref = self._get_user_ref(user_id)
        user_ref.delete()
        auth.delete_user(user_id)