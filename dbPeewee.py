# import peewee library
from peewee import *

# create an instancce of SQLite database
db=SqliteDatabase("students.db")

# define a class that manages database
class Student(Model):
    admNo=IntegerField()
    name=TextField()
    doA=DateField(formats='%Y-%m-%d')
    regestration=BooleanField()

    class Meta:
        database=db

# creating a table
Student.create_table()
