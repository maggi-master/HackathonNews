from database import ServerFirebaseConfig, FirebaseHandler

config = ServerFirebaseConfig()
database = FirebaseHandler(config)
user_data = database.get_all_users() #list[dict]