import matplotlib.pyplot as plt
from Conversation import Conversation

class Plotter:
    def __init__(self,conversation):
        names=conversation.getNames()
        messages=conversation.getMessages()
        chars=conversation.getChars()
        plt.pie(messages,labels=names, autopct='%1.2f%%')
        plt.legend(loc='upper left',bbox_to_anchor=(1.3, 1),labels=['%s, %1.2f %%' % (l, s/100) for l, s in zip(names, messages)])
        plt.show()