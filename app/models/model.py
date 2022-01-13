from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()

# Joint tables
Participation = db.Table('participation',
                        db.Column('personid', db.Integer, db.ForeignKey('person.id'), primary_key=True),
                        db.Column('eventid', db.Integer, db.ForeignKey('event.id'), primary_key=True),
                        db.Column('desc', db.Boolean))

Relation = db.Table('relation',
                      db.Column('pers1id', db.Integer, db.ForeignKey('person.id'), primary_key=True),
                      db.Column('pers2id', db.Integer, db.ForeignKey('person.id'), primary_key=True),
                      db.Column('desc', db.Text))


class Person(db.Model):
    __tablename__ = "person"
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    lastname = db.Column(db.Text)
    firstname = db.Column(db.Text)


class Event(db.Model):
    __tablename__ = "event"
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    name = db.Column(db.Text)
    date = db.Column(db.Date)
    desc = db.Column(db.Text)
    place_id = db.Column(db.Integer, db.ForeignKey('place.id'))

    @staticmethod
    def add_event(name, date, place, desc=""):
        event = Event(name=name, date=date, place_id=place.id, desc=desc)
        try:
            db.session.add(event)
            db.session.commit()
            return event
        except Exception as e:
            return False, [str(e)]


class Place(db.Model):
    __tablename__ = "place"
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    date = db.Column(db.Text)
    decade = db.Column(db.Integer)
    url = db.Column(db.Text)
    placetype = db.Column(db.Text)
