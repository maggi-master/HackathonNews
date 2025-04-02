import os
from dotenv import load_dotenv

class ServerFirebaseConfig:
    def __init__(self) -> None:
        load_dotenv()
        self.account_type = "service_account"
        self.project_id = os.getenv("FIREBASE_PROJECT_ID")
        self.private_key_id = os.getenv("FIREBASE_PRIVATE_KEY_ID")
        self.private_key = os.getenv("FIREBASE_PRIVATE_KEY").replace('\\n', '\n')
        self.client_email = os.getenv("FIREBASE_CLIENT_EMAIL")
        self.client_id = os.getenv("FIREBASE_CLIENT_ID")
        self.auth_uri = os.getenv("FIREBASE_AUTH_URI")
        self.token_uri = os.getenv("FIREBASE_TOKEN_URI")
        self.auth_provider_x509_cert_url = os.getenv("FIREBASE_AUTH_PROVIDER_X509_CERT_URL")
        self.client_x509_cert_url = os.getenv("FIREBASE_CLIENT_X509_CERT_URL")
        self.universe_domain = os.getenv("FIREBASE_UNIVERSE_DOMAIN")

        self._validate_credentials()

    def _validate_credentials(self) -> None:
        if not all([
            self.project_id,
            self.private_key_id,
            self.private_key,
            self.client_email,
            self.client_id,
            self.auth_uri,
            self.token_uri,
            self.auth_provider_x509_cert_url,
            self.client_x509_cert_url,
            self.universe_domain
        ]):
            raise ValueError("Missing required Firebase server config values. Ensure values are provided in .env")
        
    def get_credentials(self) -> dict:
        return {
            "type": self.account_type,
            "project_id": self.project_id,
            "private_key_id": self.private_key_id,
            "private_key": self.private_key,
            "client_email": self.client_email,
            "client_id": self.client_id,
            "auth_uri": self.auth_uri,
            "token_uri": self.token_uri,
            "auth_provider_x509_cert_url": self.auth_provider_x509_cert_url,
            "client_x509_cert_url": self.client_x509_cert_url,
            "universe_domain": self.universe_domain
        }