import os
from dotenv import load_dotenv

class ClientFirebaseConfig:
    def __init__(self) -> None:
        load_dotenv()
        self.api_key = os.getenv("FIREBASE_API_KEY")
        self.auth_domain = os.getenv("FIREBASE_AUTH_DOMAIN")
        self.project_id = os.getenv("FIREBASE_PROJECT_ID")
        self.storage_bucket = os.getenv("FIREBASE_STORAGE_BUCKET")
        self.messaging_sender_id = os.getenv("FIREBASE_MESSAGING_SENDER_ID")
        self.app_id = os.getenv("FIREBASE_APP_ID")

        self._validate_credentials()

    def _validate_credentials(self) -> None:
        if not all([
            self.api_key,
            self.auth_domain,
            self.project_id,
            self.storage_bucket,
            self.messaging_sender_id,
            self.app_id
        ]):
            raise ValueError("Missing required Firebase client config values. Ensure values are provided in .env")

    def get_credentials(self) -> dict:
        return {
            "apiKey": self.api_key,
            "authDomain": self.auth_domain,
            "projectId": self.project_id,
            "storageBucket": self.storage_bucket,
            "messagingSenderId": self.messaging_sender_id,
            "appId": self.app_id
        }
