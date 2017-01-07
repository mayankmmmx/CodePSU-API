import peewee as pw
from Routes.db import RegistrationForm

db = pw.MySQLDatabase('codepsu', user='root',passwd='')

RegistrationForm.create_table()