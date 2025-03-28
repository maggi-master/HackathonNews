import firebase_admin
from firebase_admin import credentials, firestore
from email_validator import validate_email, EmailNotValidError



class EmailHandler:
    def __init__(self):
        # Initialize Firebase
        cred = credentials.Certificate("path/to/your/serviceAccountKey.json")
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def fetch_emails(self) -> dict:
        """Fetches email list from Firebase Firestore"""
        emails_ref = self.db.collection("emails")  # Get the 'emails' collection
        docs = emails_ref.stream()  # Get all documents inside the collection
        return {doc.id: doc.to_dict() for doc in docs}  # Convert them to a dictionary

    def send_verification_email(self, recieving_adress:str):
        """Sends verification email to given adress"""
        pass

    def fetch_content(self) -> str:
        pass

    def send_newsletter(self):
        pass
        
    def verify_email(self):
        """
        Fetches emails from Firebase, validates them, 
        and updates the database with validity status.
        """
        emails = self.fetch_emails()  # Get all emails from the database

        for doc_id, data in emails.items():  # Loop through each email
            email = data.get("email", "")  # Extract the email

            try:
                validate_email(email, check_deliverability=True)  # Validate email
                is_valid = True  # If it's valid, set to True
            except EmailNotValidError:
                is_valid = False  # If validation fails, set to False

            # Update Firebase with the validation result
            self.db.collection("emails").document(doc_id).update({"valid": is_valid})

        