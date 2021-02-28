class Conversation:
    users=[]    #array of users

    def __init__(self, source):     #init
        self.source=source
        self.readConv()
        self.readUsers()

    def readConv(self):
        file = open(self.source, "r", encoding='utf-8')  # open read only
        self.content = file.read()
        file.close;
        titleStart=self.content.find("<title>")+7
        titleEnd=self.content.find("</title>")
        self.title=self.content[titleStart:titleEnd]
        print(self.title)

    def readUsers(self):
        print(self.title)

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