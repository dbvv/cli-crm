from pony.orm import *

db = Database()

class Contact(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    lastname = Optional(str)
    phone1 = Optional(str)
    phone2 = Optional(str)
    email = Optional(str)
    notices = Optional(str)

class ContactMeta(db.Entity):
    id = PrimaryKey(int, auto=True)
    user = Set('Contact')
    meta_key = Required(str)
    meta_value = Optional(str)
