from .db_initialise import db  # Importing from extensions.py
import bcrypt
from datetime import datetime

class User(db.Document):
    name = db.StringField(required=True)
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)
    created_at = db.DateTimeField(default=datetime.utcnow)
    updated_at = db.DateTimeField(default=datetime.utcnow)
    
    meta = {'collection': 'users','indexes': ['email']}
        
    def hash_password(self):
        self.password = bcrypt.hashpw(self.password.encode('utf-8'),bcrypt.gensalt()).decode('utf-8')
        
    
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'),self.password.encode('utf-8'))
            
            
        
