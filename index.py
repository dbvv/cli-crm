from flask import Flask, json
import vk_parser

api = Flask(__name__)

@api.route("/vk/groups", methods=['GET'])
def get_groups():
  groups = vk_parser.groups()
  return json.dumps(groups)

if __name__ == '__main__':
  api.run()