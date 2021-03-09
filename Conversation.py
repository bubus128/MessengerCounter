from MessageSender import MessageSender
from UsersRepo import UsersRepo
import json
import os


class Conversation:

    def __init__(self, path):  #init
        self.dir=os.listdir(path)
        #creating messageSender
        self.messageSender = MessageSender()
        #users repo initialization
        self.usersRepo = UsersRepo(self.messageSender)
        #read files
        for file in self.dir:
            if file.startswith("message"):
                self.readFile(os.path.join(path,file))
        #sorting
        self.usersRepo.messageSort()

    def readFile(self,path):
        #json file reading
        file=json.load(open(path,encoding='utf8'))
        #users reading
        self.title=self.toUtf8(file["title"])
        for user in file["participants"]:
            self.usersRepo.addUser(self.toUtf8(user["name"]))
        #messages reading
        for message in file["messages"]:
            name=self.toUtf8(message["sender_name"])
            if "content" in message:
                self.usersRepo.addMessage(name,self.toUtf8(message["content"]))
            if "photos" in message:
                for photo in message["photos"]:
                    self.usersRepo.addPhoto(name)

    def getNames(self):
        return self.usersRepo.getNames()

    def getMessages(self):
        return self.usersRepo.getMessages()

    def getChars(self):
        return self.usersRepo.getChars()

    def toUtf8(self,text):
        return text.encode('latin_1').decode('utf-8')