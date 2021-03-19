from User import User
class UsersRepo:
    users = {}  #dictionary of users

    def __init__(self,sender):
        self.messageSender=sender
        self.messageSender.repoInit()

    #add user if not exists
    def addUser(self, name):
        if name not in self.users:
            user = User(name)
            self.users[name]=user

    def addFile(self,name):
        if name in self.users:
            self.users[name].addFile()
        else:
            self.messageSender.userNotFound(name)

    def addPhoto(self,name):
        if name in self.users:
            self.users[name].addPhoto()
        else:
            self.messageSender.userNotFound(name)

    def addReaction(self,receiver,feeder,react):
        if receiver in self.users:
            if feeder in self.users:
                self.users[receiver].addErnedReaction(react)
                self.users[feeder].addGivenReaction(react)
            else:
                self.messageSender.userNotFound(feeder)
        else:
            self.messageSender.userNotFound(receiver)
        pass

    #add message to user
    def addMessage(self,name,content):
        if name in self.users:
            self.users[name].addMessage(len(content))
        else:
            self.messageSender.userNotFound(name)

    #return list of users names
    def getData(self):
        return self.users