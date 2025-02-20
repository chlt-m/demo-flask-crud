from bson import ObjectId

class Note:
    def __init__(self, title, content, important, tag):
        self.title = title
        self.content = content
        self.important = important
        self.tag = tag

    
    def to_dict(self,id=None):
        if id == None:
            id=str(ObjectId())
        return {
            "_id": id,  
            "title": self.title,
            "content": self.content,
            "important": self.important,
            "tag": self.tag
        }   