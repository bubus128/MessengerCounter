from MessageSender import MessageSender
from User import User


class Conversation:
    users=[]    #array of users
    titleCrop=["<title>","</title>"]
    usersCrop=["class=\"_2lek\">","</div>"]

    def __init__(self, source):     #init
        self.source=source
        self.messageSender = MessageSender()
        self.readConv()
        self.readUsers()

    def readConv(self):
        #reading conversation
        file = open(self.source, "r", encoding='utf-8')  # open read only
        self.content = file.read()
        file.close;
        #extracting title from content
        titleStart=self.content.find(self.titleCrop[0])+len(self.titleCrop[0])
        titleEnd=self.content.find(self.titleCrop[1])
        self.title=self.content[titleStart:titleEnd]
        #print(self.title)

    def readUsers(self):
        #extractiong users from content
        startUsers=self.content.find(self.usersCrop[0])+len(self.usersCrop[0])
        crop1=self.content[startUsers:]
        endUsers=crop1.find(self.usersCrop[1])
        users=crop1[:endUsers]
        #extracting particular users
        usersCroped=users.replace(' i ',', ').replace(' and ',',v').split(', ')
        for user in usersCroped:
            self.addUser(user)

    def addUser(self,name):
        user=User(name)
        self.users.append(user)
        self.messageSender.userCreated(name)

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