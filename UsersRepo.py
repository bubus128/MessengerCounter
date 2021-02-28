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
        chars=len(content)
        user.addMessage(chars)