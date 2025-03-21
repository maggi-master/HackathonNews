from email_validator import validate_email, EmailNotValidError



class EmailHandler:
    def __init__(self):
        pass

    def fetch_emails(self) -> dict:
        """Fetches email list from database"""
        pass

    def send_verification_email(self, recieving_adress:str):
        """Sends verification email to given adress"""
        pass

    def fetch_content(self) -> str:
        pass

    def send_newsletter(self):
        pass
        
    def verify_email(self, email:str) -> bool:
        """
        Checks if an email address is valid.
        
        Given info:
            email (str): The email address to validate.
        
        Returns:
            bool: True if the email is valid, False otherwise.
        """
        try:
            validate_email(email, check_deliverability=True)  # Also checks if the domain exists
            return True
        except EmailNotValidError:
            return False