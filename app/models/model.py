from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()

# Joint tables
PersonThing = db.Table('person_thing',
                        db.Column('personid', db.Integer, db.ForeignKey('person.id'), primary_key=True),
                        db.Column('thingid', db.Integer, db.ForeignKey('thing.id'), primary_key=True),
                        db.Column('isTrue', db.Boolean))

PersonSubject = db.Table('person_subject',
                      db.Column('personid', db.Integer, db.ForeignKey('person.id'), primary_key=True),
                      db.Column('subjectid', db.Integer, db.ForeignKey('subject.id'), primary_key=True),
                      db.Column('isTrue', db.Boolean))

ThingSubject = db.Table('thing_subject',
                      db.Column('thingid', db.Integer, db.ForeignKey('thing.id'), primary_key=True),
                      db.Column('subjectid', db.Integer, db.ForeignKey('subject.id'), primary_key=True),
                      db.Column('isTrue', db.Boolean))


class Person(db.Model):
    __tablename__ = "person"
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    lastname = db.Column(db.Text)
    firstname = db.Column(db.Text)


class Thing(db.Model):
    __tablename__ = "thing"
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    title = db.Column(db.Text)
    provenance = db.Column(db.Text)
    decade = db.Column(db.Integer)
    isTrue = db.Column(db.Boolean)


class Subject(db.Model):
    __tablename__ = "subject"
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    date = db.Column(db.Text)
    decade = db.Column(db.Integer)
    url = db.Column(db.Text)
    subjecttype = db.Column(db.Text)


class Response(db.Model):
    __tablename__ = "response"
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    thingid = db.Column(db.Integer, db.ForeignKey('thing.id'))
    isTrue = db.Column(db.Boolean)
    answer = db.Column(db.Boolean)
    thingProvenance = db.Column(db.Text)

    @staticmethod
    def add_response(thing, answer):
        response = Response(thingid=thing.id, isTrue=thing.isTrue, answer=answer, thingProvenance=thing.provenance)
        try:
            db.session.add(response)
            db.session.commit()
            return response
        except Exception as e:
            return False, [str(e)]
