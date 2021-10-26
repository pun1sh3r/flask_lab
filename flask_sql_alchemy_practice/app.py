from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #to supress warning
db = SQLAlchemy(app)




class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80),index=True, unique=True)
    author_surname = db.Column(db.String(80), index=True, unique=False)  # author surname
    author_name = db.Column(db.String(50),index=True,unique=False)
    month = db.Column(db.String(20), index=True, unique=False)  # the month of book suggestion
    year = db.Column(db.Integer, index=True, unique=False)  # the year of book suggestion
    reviews = db.relationship('Review', backref = 'book', lazy = 'dynamic', cascade = "all, delete, delete-orphan")  # relationship of Books and Reviews
    annotations = db.relationship('Annotation', backref='book', lazy='dynamic', cascade="all, delete, delete-orphan")
    def __repr__(self):
        return "{} in: {},{}".format(self.title, self.month,self.year)

# Add your columns for the Reader model here below.
class Reader(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True, unique=False)
    surname = db.Column(db.String(80), unique=False, index=True)
    email = db.Column(db.String(120), unique=True, index=True)
    reviews = db.relationship("Review", backref='reviewer', lazy='dynamic')
    annotations = db.relationship('Annotation', backref='author', lazy='dynamic', cascade="all, delete, delete-orphan")
    def __repr__(self):
        return "Reader ID: {}, email: {}".format(self.id, self.email)


#declaring the Review model
class Review(db.Model):
    id = db.Column(db.Integer, primary_key = True) #primary key column, automatically generated IDs
    stars = db.Column(db.Integer, unique = False) #a review's rating
    text = db.Column(db.String(200), unique = False) #a review's text
    book_id = db.Column(db.Integer, db.ForeignKey('book.id')) #foreign key column
    reviewer_id = db.Column(db.Integer, db.ForeignKey('reader.id'))

    def __repr__(self):
        return "Review ID: {}, {} stars {}".format(self.id, self.stars, self.book_id)

class Annotation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), unique=False)
    reviewer_id = db.Column(db.Integer, db.ForeignKey('reader.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))

    def __repr__(self):
        return '<Annotation {}-{}:{} >'.format(self.reviewer_id, self.book_id, self.text)
#some routing for displaying the home page
import routes
