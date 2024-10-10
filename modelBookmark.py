"""Represents a bookmark in the model."""

from peewee import *
from database_config import database_path

db = SqliteDatabase(database_path)

class BookMark(Model):

    """ Represents a bookmark in the database """
    parkdata = CharField()
    weatherdata = CharField()
    directiondata = CharField()

    class Meta:
        database = db
        constraints = [SQL('UNIQUE( parkdata COLLATE NOCASE )')]

    def __str__(self):
        return self.parkdata + " " + self.directiondata + " " + self.weatherdata


db.connect()
db.create_tables([BookMark])