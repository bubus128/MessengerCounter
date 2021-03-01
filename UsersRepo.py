from User import User
class UsersRepo:

    users = []  # array of users
    def __init__(self,sender):
        self.messageSender=sender
        self.messageSender.repoInit()

    def addUser(self, name):
        user = User(name)
        self.users.append(user)
        self.messageSender.userCreated(name)

    #find user by name, if not found then return -1
    def findUserByName(self,name):
        for user in self.users:
            if user.name==name:
                return user
        return -1

    def messageFound(self,name,content):
        user=self.findUserByName(name)
        if user!=-1:
            chars=len(content)
            user.addMessage(chars)
        else:
            self.messageSender.userNotFound(name)

    def summary(self):
        messages=self.totalMessaes()
        chars=self.totalChars()
        for user in self.users:
            self.messageSender.printUser(messages,chars,user)

    def totalMessaes(self):
        total=0
        for user in self.users:
            total+=user.messages
        return total

    def totalChars(self):
        total=0
        for user in self.users:
            total+=user.chars
        return total

    def getNames(self):
        return [user.name for user in self.users]

    def getMessages(self):
        return [user.messages for user in self.users]

    def getChars(self):
        return [user.chars for user in self.users]