from flask import Flask, json, request
import vk_parser
from pony.flask import Pony
from pony.orm import Database
from app import *

api = Flask(__name__, static_folder="web/dist", static_url_path='')

api.config.update(dict(
    DEBUG=True,
    PONY = {
        'provider': 'sqlite',
        'filename': 'db.db3',
        'create_db': True,
    }
))

db=Database()

@db.on_connect(provider='sqlite')
def sqlite_case_sensitivity(db, connection):
    cursor = connection.cursor()
    cursor.execute('PRAGMA case_sensitive_like = OFF')

db.bind(**api.config['PONY'])
db.generate_mapping(create_tables=True)

Pony(api)

@api.route("/", methods=['GET'])
def index():
  return api.send_static_file('index.html')

@api.route("/user/friends", methods=['GET'])
def get_friends():
    friends = vk_parser.get_friends(request.args.get('user_id'))
    return json.dumps(friends)

if __name__ == '__main__':
  api.run()
