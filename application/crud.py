from bson import ObjectId
from .connection import get_db
from .model import Note

db = get_db()
collection = db['data'] 

def add_note(data):
    data = Note(data['title'],data['content'],data['important'],data['tag'])
    result = collection.insert_one(data.to_dict())
    if result.inserted_id:
        return "Insert successful {}".format(data.to_dict())
    else:
        return "Insert failed"

def get_note():
    notes = collection.find()
    list_note = list(notes)
    for note in list_note:
            note['_id'] = str(note['_id'])

    return list_note
        
def delete_note(id):
    id = {
        '_id': id
    }
    result = collection.delete_one(id)
    if result.deleted_count > 0:
        return "Delete successful"
    else:
        return "No document found to delete"


def update_note(id, data):
    data = Note(data['title'],data['content'],data['important'],data['tag'])
    data_change = {
        '$set': data.to_dict(id)
    }
    id = {
        '_id': id
    }    
    result = collection.update_one(id,data_change)
    if result.modified_count > 0:
        return "Update successful"
    else:
        return "No document found to update"


