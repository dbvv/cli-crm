from flask import Blueprint

vk_blueprint = Blueprint('vk', __name__)

@vk_blueprint.route("/groups", methods=['GET'])
def get_groups():
  groups = vk_parser.groups()
  return json.dumps(groups)