import matplotlib.pyplot as plt
from Conversation import Conversation

class Plotter:
    def __init__(self,conversation):
        names=conversation.getNames()
        messages=conversation.getMessages()
        chars=conversation.getChars()
        plt.plot(names,messages)
        plt.show()