class User:

    def __init__(self, name):
        self.name = name
        self.messages = 0
        self.chars = 0
        self.givenReactions = dict()
        self.earnedReactions = dict()
        self.givenReactionsCount = 0
        self.earnedReactionsCount = 0
        self.photos = 0
        self.files = 0

    def add_message(self, chars):
        self.messages += 1
        self.chars += chars

    def add_photo(self):
        self.photos += 1

    def add_given_reaction(self, react):
        self.givenReactionsCount += 1
        if react in self.givenReactions.keys():
            self.givenReactions[react] += 1
        else:
            self.givenReactions[react] = 1

    def add_earned_reaction(self, react):
        self.earnedReactionsCount += 1
        if react in self.earnedReactions.keys():
            self.earnedReactions[react] += 1
        else:
            self.earnedReactions[react] = 1

    def add_file(self):
        self.files += 1
