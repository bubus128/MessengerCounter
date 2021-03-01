import matplotlib.pyplot as plt
from Conversation import Conversation

class Plotter:
    def __init__(self,conversation):
        names=conversation.getNames()
        messages=conversation.getMessages()
        chars=conversation.getChars()
        fig, (messagePlot, charPlot) = plt.subplots(1, 2)
        messagePlot.pie(messages,labels=names, autopct='%1.2f%%')
        messagePlot.legend(loc='upper left',bbox_to_anchor=(1.3, 1),labels=['%s, %1.2f %%' % (l, s/100) for l, s in zip(names, messages)])
        charPlot.pie(chars,labels=names, autopct='%1.2f%%')
        messagePlot.legend(loc='upper left', bbox_to_anchor=(1.3, 1),labels=['%s, %1.2f %%' % (l, s / 100) for l, s in zip(names, chars)])
        plt.show()