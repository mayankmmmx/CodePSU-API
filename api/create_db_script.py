import peewee as pw
from Routes.db import RegistrationForm
from Routes.constants

db = peewee.MySQLDatabase(constants.DB_NAME, user=constants.DB_USER_NAME,
                            passwd=constants.DB_PASSWORD)

RegistrationForm.create_table()