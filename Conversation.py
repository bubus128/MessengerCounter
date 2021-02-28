from MessageSender import MessageSender
from User import User


class Conversation:
    users=[]    #array of users
    titleCrop=["<title>","</title>"]
    usersCrop=["class=\"_2lek\">","</div>"]
    messageSeparators=["<div class=\"_3-96 _2pio _2lek _2lel\">","</div><div class=\"_3-96 _2let\"><div><div></div><div>","</div>"]

    def __init__(self, source):     #init
        #seting sourcefile of conversation
        self.source=source
        #creating messageSender
        self.messageSender = MessageSender()
        #red title and content of conversation
        self.readConv()
        #create users of conversation
        self.readUsers()
        #read messages
        self.readMessages()

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

    def readMessages(self):
        message=self.content
        cropPoint=message.find(self.messageSeparators[0])
        while(cropPoint>-1):
            message=message[cropPoint+len(self.messageSeparators[0]):]
            #find author of message
            crop1=message.find(self.messageSeparators[1])
            author=message[:crop1]
            message=message[crop1+len(self.messageSeparators[1]):]
            #find content of message
            crop2=message.find(self.messageSeparators[2])
            content=message[:crop2]
            self.messageSender.messageFound(author,content)
            cropPoint = message.find(self.messageSeparators[0])

    def addUser(self,name):
        user=User(name)
        self.users.append(user)
        self.messageSender.userCreated(name)

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