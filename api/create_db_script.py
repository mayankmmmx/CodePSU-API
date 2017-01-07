import peewee
from Routes.db import RegistrationForm
from Routes import constants

db = peewee.MySQLDatabase(constants.DB_NAME, user=constants.DB_USER_NAME,
                            passwd=constants.DB_PASSWORD, host=constants.DB_HOST)

RegistrationForm.create_table()