class User:
    messages=0
    chars=0
    reactions=[]
    photos=0
    files=0
    def __init__(self,name):
        self.name=name

    def addMessage(self, chars):
        self.messages+=1
        self.chars+=chars

    def addPhoto(self):
        self.photos+=1

    def addReaction(self,react):
        self.reactions[react]+=1

    def addFile(self):
        self.files+=1

    def getMessagesCount(self):
        return self.messages

    def getCharsCount(self):
        return self.chars
