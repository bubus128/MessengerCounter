from termcolor import colored


class MessageSender:

    def __init__(self):
        print("messageSender created")

    @staticmethod
    def users_created(count):
        message = "{} users created"
        print(message.format(count))

    @staticmethod
    def repo_init():
        print("users repo is starting")

    @staticmethod
    def user_not_found(name):
        print(colored("user: "+name+" not found in conversation", 'red'))

    @staticmethod
    def messages_read(messages, chars):
        message = "{} messages read (containing {} chars)"
        print(message.format(messages, chars))
