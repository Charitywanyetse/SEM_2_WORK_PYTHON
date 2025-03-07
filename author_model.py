from app.extensions import db
from datetime import datetime  



class Author (db.Model):
    __tablename__ = "authors"
    id = db.Column(db.Integer, primary_key=True,nullable =False)
    first_name = db.Column(db.String(20),nullable =False)
    last_name = db.Column(db.String(100),nullable =False)
    contact = db.Column(db.String(10),nullable =False,unique = True)
    email = db.Column(db.String(50),nullable =False,unique = True)
    password = db.Column(db.String(50),nullable =False,unique = True)
    image = db.Column(db.String(50),nullable =True)
    bio = db.Column(db.String(50),nullable =False)
    created_at = db.Column(db.DateTime,default = datetime.now)
    updated_at = db.Column(db.DateTime,onupdate = datetime)
    
    
    def __init__(self, author_id,first_name, last_name,contact,email,password,image,bio,created_at,updated_at):
        self.author_id = author_id
        self.first_name = first_name
        self.last_name = last_name
        self.contact = contact
        self.email = email
        self.password = password
        self.image = image
        self. bio = bio
        self.created_at = created_at
        self. updated_at =  updated_at
        