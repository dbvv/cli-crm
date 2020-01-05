from pony.orm import *

db = Database()

class Vk_Source(db.Entity):
  id = PrimaryKey(int, auto=True)
  type = Required(str)
  #last_id = 

class Contact(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    

