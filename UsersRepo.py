from User import User


class UsersRepo:
    users = {}  # dictionary of users

    def __init__(self, sender):
        self.messageSender = sender
        self.messageSender.repo_init()

    # add user if not exists
    def add_user(self, name):
        if name not in self.users:
            user = User(name)
            self.users[name] = user

    def add_file(self, name):
        if name in self.users:
            self.users[name].add_file()
        else:
            self.messageSender.user_not_found(name)

    def add_photo(self, name):
        if name in self.users:
            self.users[name].add_photo()
        else:
            self.messageSender.user_not_found(name)

    def add_reaction(self, receiver, feeder, react):
        if receiver in self.users:
            if feeder in self.users:
                self.users[receiver].add_earned_reaction(react)
                self.users[feeder].add_given_reaction(react)
            else:
                self.messageSender.user_not_found(feeder)
        else:
            self.messageSender.user_not_found(receiver)

    # add message to user
    def add_message(self, name, content):
        if name in self.users:
            self.users[name].add_message(len(content))
        else:
            self.messageSender.user_not_found(name)

    # return list of users names
    def get_data(self):
        return self.users
