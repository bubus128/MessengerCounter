class MessageSender:

    def __init__(self):
        print("messageSender created")

    def userCreated(self,name):
        message="user: {} created"
        print(message.format(name))

    def messageFound(self,author,content):
        message="{} wtire: {}"
        print(message.format(author,content))