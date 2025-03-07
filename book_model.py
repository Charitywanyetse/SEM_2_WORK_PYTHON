from flask import db
class Book (db.Model):
            
 id = db.Column(db.Integer, primary_key=True)
 title = db.Column(db.String(20))
 author = db.Column(db.String(50))
 book_cover= db.Column(db.String(50))
 discription = db.Column(db.String(50))
 production_date = db.Column(db.String(50))
 publication_date = db.Column(db.String(55))
 number_of_pages = db.Column(db.String(60))
 
def __init__(self, title, author,book_cover,discription,production_date,publication_date,number_of_pages):
   self.title = title
   self.author = author
   self.book_cover = book_cover
   self.discription = discription
   self.production_date = production_date
   self.publication_date = publication_date
   self.number_of_pages = number_of_pages


def __repr__(self):
  return '<Product %d>' % self.id
db.create_all()
