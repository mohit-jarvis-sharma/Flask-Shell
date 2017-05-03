from peewee import *

db = SqliteDatabase('shell.db')

class My_Shell(Model):
    id = PrimaryKeyField()
    my_cmd = CharField()
    result_of_cmd = CharField()

    class Meta:
        database = db

def initialize_db():
    db.connect()
    db.create_tables([My_Shell] , safe = True)

initialize_db()
