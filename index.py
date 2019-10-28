from flask import Flask, json
import vk_parser

api = Flask(__name__, static_folder="web/dist", static_url_path='')

@api.route("/", methods=['GET'])
def index():
  return api.send_static_file('index.html')

@api.route("/vk/groups", methods=['GET'])
def get_groups():
  groups = vk_parser.groups()
  return json.dumps(groups)

if __name__ == '__main__':
  api.run()