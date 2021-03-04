from User import User
class UsersRepo:
    users = []  #array of users

    def __init__(self,sender):
        self.messageSender=sender
        self.messageSender.repoInit()

    #add user if not exists
    def addUser(self, name):
        user = User(name)
        if self.findUserByName(name)==-1:
            self.users.append(user)

    #count of users
    def getUsersCount(self):
        return len(self.users)

    #find user by name, if not found then return -1
    def findUserByName(self,name):
        for user in self.users:
            if user.name==name:
                return user
        return -1

    #add message to user
    def messageFound(self,name,content):
        user=self.findUserByName(name)
        if user!=-1:
            chars=len(content)
            user.addMessage(chars)
        else:
            self.messageSender.userNotFound(name)

    #retur total count of messages
    def totalMessaes(self):
        total=0
        for user in self.users:
            total+=user.messages
        return total

    #retur total count of chars in messages
    def totalChars(self):
        total=0
        for user in self.users:
            total+=user.chars
        return total

    #return list of users names
    def getNames(self):
        return [user.name for user in self.users]

    #return list of users messages count
    def getMessages(self):
        return [user.messages for user in self.users]

    #return list of users chars count
    def getChars(self):
        return [user.chars for user in self.users]

    #sorting key to sorting users by messages count
    def sortingMessagesKey(self,user):
        return user.messages

    #sorting key to sorting users by chars count
    def sortingCharsKey(self,user):
        return user.chars

    #sort users by messages count
    def messageSort(self):
        self.users.sort(key=self.sortingMessagesKey,reverse=True)
        print("sorted by messages count")

    #sort users by chars count
    def charsSort(self):
        self.users.sort(key=self.sortingCharsKey, reverse=True)
        print("sorted by chars count")