from enum import unique
from . import db
from flask_login import UserMixin
# from sqlalchemy.sql import func

# model for author
class Author(db.Model, UserMixin):
    AuthorID = db.Column(db.Integer, primary_key=True,)
    FirstName = db.Column(db.String(50))
    MiddleInitial = db.Column(db.String(1))
    LastName = db.Column(db.String(50))
    Affiliation = db.Column(db.String(50))
    Department = db.Column(db.String(50))
    Address = db.Column(db.String(50))
    City = db.Column(db.String(50))
    State = db.Column(db.String(2))
    ZipCode = db.Column(db.String(10))
    PhoneNumber = db.Column(db.String(50))
    EmailAddress = db.Column(db.String(100),unique=True)
    Password = db.Column(db.String(5))
    Papers = db.relationship('Paper')

    # uses authorID for getting ID
    def get_id(self):
        return self.AuthorID

# model for reviewers
class Reviewer(db.Model, UserMixin):
    ReviewID = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(50))
    MiddleInitial = db.Column(db.String(1))
    LastName = db.Column(db.String(50))
    Affiliation = db.Column(db.String(50))
    Department = db.Column(db.String(50))
    Address = db.Column(db.String(50))
    City = db.Column(db.String(50))
    State = db.Column(db.String(2))
    ZipCode = db.Column(db.String(10))
    PhoneNumber = db.Column(db.String(50))
    EmailAddress = db.Column(db.String(100), unique=True)
    Password = db.Column(db.String(5))
    # bits for topics

     # uses reviewerID for getting ID
    def get_id(self):
        return self.ReviewID


class Paper(db.Model,UserMixin):
    PaperID = db.Column(db.Integer, primary_key=True)
    AuthorID = db.Column(db.Integer, db.ForeignKey('author.AuthorID'))
    Active = db.Column(db.LargeBinary(1))
    FileName = db.Column(db.String(100))
    FileData = db.Column(db.LargeBinary)
    Title = db.Column(db.String(500))
    Certification = db.Column(db.String(3))
    # bits for topics





 

# class Review(db.Model,UserMixin):
#     pass
