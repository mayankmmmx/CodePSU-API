import peewee
import constants

db = peewee.MySQLDatabase(constants.DB_NAME, user=constants.DB_USER_NAME,
                            passwd=constants.DB_PASSWORD)

class RegistrationForm(peewee.Model):
    ''' Model for Registration '''

    name = peewee.TextField()
    email = peewee.TextField()
    shirt = peewee.TextField()
    linkedin = peewee.TextField(null=True)
    github = peewee.TextField(null=True)
    resume_link = peewee.TextField()
    can_share = peewee.TextField()
    highest_cs = peewee.TextField()
    tier = peewee.TextField()
    allergies = peewee.TextField(null=True)
    team_or_match = peewee.TextField()
    team_name = peewee.TextField()
    teammate_1_name = peewee.TextField(null=True)
    teammate_1_email = peewee.TextField(null=True)
    teammate_2_name = peewee.TextField(null=True)
    teammate_2_email = peewee.TextField(null=True)

    class Meta:
        database = db
        db_table = constants.DB_TABLE_NAME

# Inserts record into db
def insert_record(registration_info):
    record = RegistrationForm(
                name=registration_info['name'],
                email=registration_info['email'],
                shirt=registration_info['shirt'],
                linkedin=registration_info['linkedin'],
                github=registration_info['github'],
                resume_link=registration_info['resume_file_path'],
                can_share=registration_info['can_share_info'],
                highest_cs=registration_info['highest_cs_course'],
                tier=registration_info['tier'],
                allergies=registration_info['allergies'],
                team_or_match=registration_info['team_or_match'],
                team_name=registration_info['team_name'],
                teammate_1_name=registration_info['teammate_1_name'],
                teammate_1_email=registration_info['teammate_1_email'],
                teammate_2_name=registration_info['teammate_2_name'],
                teammate_2_email=registration_info['teammate_2_email']
            );

    try:
        record.save()
    except:
        return ['-1', 'Could not register. Please try again']

    return ['0', 'Successfully added to database']
