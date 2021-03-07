from MessageSender import MessageSender
from UsersRepo import UsersRepo
from tqdm import tqdm
import json
import os


class Conversation:
    titleCrop = ["<title>", "</title>"]
    usersCrop = ["class=\"_2lek\">", "</div>"]
    messageSeparators = ["<div class=\"_3-96 _2pio _2lek _2lel\">",
                         "</div><div class=\"_3-96 _2let\"><div><div></div><div>", "</div>"]

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

    def getNames(self):
        return self.usersRepo.getNames()

    def getMessages(self):
        return self.usersRepo.getMessages()

    def getChars(self):
        return self.usersRepo.getChars()

    def readFile(self,path):
        #json file reading
        file=json.load(open(path))
        #users reading
        print("Users reading")
        for user in tqdm(file["participants"]):
            self.usersRepo.addUser(user["name"])
        #messages reading
        print("Messages reading")
        for message in tqdm(file["messages"]):
            if  "content" in message:
                self.usersRepo.messageFound(message["sender_name"],message["content"])