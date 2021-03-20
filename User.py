class User:
    messages=0
    chars=0
    givenReactions={}
    ernedReactions={}
    photos=0
    files=0
    def __init__(self,name):
        self.name=name

    def addMessage(self, chars):
        self.messages+=1
        self.chars+=chars

    def addPhoto(self):
        self.photos+=1

    def addGivenReaction(self,react):
        if react in self.givenReactions.keys():
            self.givenReactions[react]+=1
        else:
            self.givenReactions[react] =1

    def addErnedReaction(self,react):
        if react in self.ernedReactions.keys():
            self.ernedReactions[react] += 1
        else:
            self.ernedReactions[react] = 1

    def addFile(self):
        self.files+=1
