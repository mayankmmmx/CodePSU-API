import os
from werkzeug import secure_filename
import constants
from db import insert_record

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in constants.ALLOWED_FILE_TYPES

def save_file(request):
    file = request.files['file']

    if not file:
        return ['-1', 'Please attach file']

    if not allowed_file(file.filename):
        return ['-1', 'Incorrect file type']

    file_name = secure_filename(file.filename)
    file_path = os.path.join(constants.FILE_PATH, file_name)
    file.save(file_path)
    return ['0', file_path]     

def create_request(raw_request):
    ''' Registers user for CodePSU '''

    # Get request as json
    request = raw_request.form

    registrant_info = {}
    registrant_info['name'] = request.get('name')
    registrant_info['email'] = request.get('email')
    registrant_info['linkedin'] = request.get('linkedin')
    registrant_info['github'] = request.get('github')
    resume = save_file(raw_request)

    # Make sure file was uploaded successfully
    if resume[0] is '-1':
        return ['-1', resume[1]]

    registrant_info['resume_file_path'] = 'hi'#resume[1]
    registrant_info['can_share_info'] = request.get('can_share_info')
    registrant_info['highest_cs_course'] = request.get('highest_cs_course')
    registrant_info['tier'] = request.get('tier')
    registrant_info['allergies'] = request.get('allergies')
    registrant_info['team_or_match'] = request.get('team_or_match')
    registrant_info['team_name'] = request.get('team_name')
    registrant_info['teammate_1_name'] = request.get('teammate_1_name')
    registrant_info['teammate_1_email'] = request.get('teammate_1_email')
    registrant_info['teammate_2_name'] = request.get('teammate_2_name')
    registrant_info['teammate_2_email'] = request.get('teammate_2_email')

    record = insert_record(registrant_info)

    if record[0] is '-1':
        return ['-1', record[1]]

    return ['0', 'Successfully registered for CodePSU!']

def respond(data):
	message = create_request(data)

	return {
        'status': message[0],
		'message': message[1]
	}