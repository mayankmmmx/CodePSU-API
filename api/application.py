from flask import Flask, request, jsonify
import Routes.register
from Routes.constants import API_KEY

application = Flask(__name__)

@application.route('/')
@application.route('/index')
def index():
    return "Welcome to CodePSU's RESTful API!"

@application.route('/register', methods=['POST'])
def register():
    if request.headers['Auth-Token'] == API_KEY:
        return jsonify(Routes.register.respond(request))

if __name__ == "__main__":
    application.run(debug=True)