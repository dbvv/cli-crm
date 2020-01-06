from .models import Contact, ContactMeta
from flask import Blueprint, json
from pony.orm import *

contacts_api = Blueprint('contacts', __name__)

@contacts_api.route('/api/contacts/all', methods=['GET'])
def contacts_all():
    contacts = select(c for c in Contact)[:]
    result = {'data': [p.to_dict() for p in contacts]}
    return json.dumps(result)

@contacts_api.route('/api/contacts/create', methods=['POST'])
def contact_create():
    contact = Contact(name=request.form['name'])
    commit()
    #result = {'data': [p.to_dict(]}
    return json.dumps({'data': [contact.to_dict()]})

