from MessageSender import MessageSender
from User import User
from UsersRepo import UsersRepo


class Conversation:
    titleCrop=["<title>","</title>"]
    usersCrop=["class=\"_2lek\">","</div>"]
    messageSeparators=["<div class=\"_3-96 _2pio _2lek _2lel\">","</div><div class=\"_3-96 _2let\"><div><div></div><div>","</div>"]

    def __init__(self, source):     #init
        #seting sourcefile of conversation
        self.source=source
        #creating messageSender
        self.messageSender = MessageSender()
        #users repo initialization
        self.users = UsersRepo(self.messageSender)
        #red title and content of conversation
        self.readConv()
        #create users of conversation
        self.readUsers()
        #read messages
        self.readMessages()
        #summary
        self.users.summary()

    def getNames(self):
        return self.users.getNames()

    def getMessages(self):
        return self.users.getMessages()

    def getChars(self):
        return self.users.getChars()

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
        usersCroped=users.replace(' i ',', ').replace(' and ',',v').replace('Uczestnicy: ','').replace('Users: ','').split(', ')
        for user in usersCroped:
            self.users.addUser(user)

    def readMessages(self):
        message=self.content
        cropPoint=message.find(self.messageSeparators[0])
        while(cropPoint>-1):
            #find author of message
            crop1=message.find(self.messageSeparators[1])
            author=message[cropPoint+len(self.messageSeparators[0]):crop1]
            message=message[crop1+len(self.messageSeparators[1]):]
            #find content of message
            crop2=message.find(self.messageSeparators[2])
            content=message[:crop2]
            self.users.messageFound(author,content)
            cropPoint = message.find(self.messageSeparators[0])



