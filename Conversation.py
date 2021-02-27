class Conversation:
    users=[]
    file

    def addUser(self,user):
        self.users.append(user)

    def countMessaes(self):
        total=0
        for user in self.users:
            total+=user.messages
        return total

    def countChars(self):
        total=0
        for user in self.users:
            total+=user.chars
        return total