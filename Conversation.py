class Conversation:
    users=[]    #array of users

    def __init__(self, source):     #init
        self.source=source
        self.readUsers()

    def readUsers(self):
        file = open(self.source, "r",encoding='utf-8')   #open read only
        for line in file:
            print(line)
        file.close;

    def addUser(self,user):
        self.users.append(user)

    def countMessaes(self):
        total=0
        for user in self.users:
            total+=user.messages
        return total

    def countChars(self):
        total=0
        for user in self.users:
            total+=user.chars
        return total