from termcolor import colored

class MessageSender:

    def __init__(self):
        print("messageSender created")

    def usersCreated(self,count):
        message="{} users created"
        print(message.format(count))

    def repoInit(self):
        print("users repo is starting")

    def userNotFound(self,name):
        print(colored("user: "+name+" not found in conversation",'red'))

    def messagesReaded(self,messages,chars):
        message="{} messages readed (containing {} chars)"
        print(message.format(messages,chars))