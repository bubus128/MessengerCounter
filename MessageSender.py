class MessageSender:

    def userCreated(self,name):
        message="user: {} created"
        print(message.format(name))