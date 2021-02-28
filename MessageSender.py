class MessageSender:

    def __init__(self):
        print("messageSender created")

    def userCreated(self,name):
        message="user: {} created"
        print(message.format(name))

    def messageFound(self,author,content):
        message="{} wtire: {}"
        print(message.format(author,content))

    def repoInit(self):
        print("users repo is starting")

    def userNotFound(self,name):
        message="user: {} not found in conversation"
        print(message.format(name))

    def printUser(self,totalMessages,totalChars,user):
        message="user {} wrote: {} messages(containing {} chars), it's {}% of all messages({}% of all chars) in this conversation"
        print(message.format(user.name,user.messages,user.chars,user.messages/totalMessages*100,user.chars/totalChars*100))