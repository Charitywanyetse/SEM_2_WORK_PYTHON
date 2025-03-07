
from app.extensions import db
from datetime import datetime 

class Company (db.Model):
    __tablename__ = "co"
    id = db.Column(db.Integer, primary_key=True,nullable =False)
    Name = db.Column(db.String(20),nullable =False)
    Location = db.Column(db.String(100),nullable =False)
    contact = db.Column(db.String(10),nullable =False,unique = True)
    email = db.Column(db.String(50),nullable =False,unique = True)
    bio = db.Column(db.String(50),nullable =False)
    created_at = db.Column(db.DateTime,default = datetime.now)
    updated_at = db.Column(db.DateTime,onupdate = datetime)
    
    
    def __init__(self, Name,Location, contact,email, bio,):
        self.Name = Name
        self.Location = Location
        self.contact = contact
        self.email = email
        self.bio = bio
        
    


 




