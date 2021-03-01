import matplotlib.pyplot as plt
from Conversation import Conversation

class Plotter:
    def __init__(self,conversation):
        names=conversation.getNames()
        messages=conversation.getMessages()
        chars=conversation.getChars()
        plt.pie(messages,labels=names)
        plt.legend(loc='upper left',bbox_to_anchor=(1.3, 1))
        plt.show()