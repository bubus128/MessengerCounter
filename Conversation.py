from MessageSender import MessageSender
from UsersRepo import UsersRepo
import json
import os


class Conversation:

    def __init__(self, path):  # init
        self.dir = os.listdir(path)
        # creating messageSender
        self.messageSender = MessageSender()
        # users repo initialization
        self.usersRepo = UsersRepo(self.messageSender)
        self.title = ""
        # read files
        for file in self.dir:
            if file.startswith("message"):
                self.read_file(os.path.join(path, file))

    def read_file(self, path):
        # json file reading
        file = json.load(open(path, encoding='utf8'))
        # users reading
        self.title = self.to_utf8(file["title"])
        for user in file["participants"]:
            self.usersRepo.add_user(self.to_utf8(user["name"]))
        # messages reading
        for message in file["messages"]:
            name = self.to_utf8(message["sender_name"])
            if "content" in message:
                self.usersRepo.add_message(name, self.to_utf8(message["content"]))
            if "photos" in message:
                for _ in message["photos"]:
                    self.usersRepo.add_photo(name)
            if "reactions" in message:
                for reaction in message["reactions"]:
                    self.usersRepo.add_reaction(name, self.to_utf8(reaction["actor"]), self.to_utf8(reaction["reaction"]))

    def get_data(self):
        return self.usersRepo.get_data()

    @staticmethod
    def to_utf8(text):
        return text.encode('latin_1').decode('utf-8')
