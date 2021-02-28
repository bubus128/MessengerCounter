class User:
    messages=0
    chars=0
    emojis=0
    photos=0
    files=0
    def __init__(self,name):
        self.name=name
    def addMessage(self, chars):
        self.messages+=1
        self.chars+=chars
