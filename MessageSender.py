class MessageSender:

    def __init__(self):
        print("messageSender created")

    def usersCreated(self,count):
        message="{} users created"
        print(message.format(count))

    def repoInit(self):
        print("users repo is starting")

    def userNotFound(self,name):
        message="user: {} not found in conversation"
        print(message.format(name))

    def messagesReaded(self,messages,chars):
        message="{} messages readed (containing {} chars)"
        print(message.format(messages,chars))