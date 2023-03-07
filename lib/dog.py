from sqlalchemy import create_engine

from models import Dog
# Engine: a Python object that translates SQL to Python and vice-versa.
engine = create_engine('sqlite:///:memory:')

# creates table "dogs" if it does not exist, and returns the engine
def create_table(base):
    base.metadata.create_all(engine)
    return engine

# takes a Dog instance and session as arguments, 
# saves the dog to the database, and returns the session.
# Session is a Python object that uses an engine to allow us 
# to programmatically interact with a database.
def save(session, dog):
    session.add(dog)
    session.commit()
    return session

# takes a database row and returns a Dog instance.
def new_from_db(session, row):
    return session.query(Dog).filter_by(id = row.id).first()

# takes a session and returns a list of Dog instances 
# for every record in the database.
def get_all(session):
    return [dog for dog in session.query(Dog)]

# takes a session and name and returns a Dog instance 
# corresponding to its database record retrieved by name.
def find_by_name(session, name):
    return session.query(Dog).filter_by(name=name).first()

# takes a session and id and returns a Dog instance 
# corresponding to its database record retrieved by id.
def find_by_id(session, id):
    return session.query(Dog).filter_by(id=id).first()

# takes a session, a name, and a breed as arguments 
# and returns a Dog instance matching that record.
def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter_by(name=name, breed=breed).first()

# takes a session instance, and breed as arguments 
# and updates the instance's breed.
def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()
    return session