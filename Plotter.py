import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

from Conversation import Conversation

class Plotter:
    outputLoc=r'output\outpu.pdf'
    def __init__(self,conversation):
        names=conversation.getNames()
        messages=conversation.getMessages()
        chars=conversation.getChars()
        with PdfPages(self.outputLoc) as pdf:
            plt.pie(messages,labels=names, autopct='%1.2f%%')
            plt.legend(loc='upper left',bbox_to_anchor=(1.3, 1),labels=['%s, %1.2f %%' % (l, s/100) for l, s in zip(names, messages)])
            pdf.savefig()
            plt.close()
            plt.pie(chars,labels=names, autopct='%1.2f%%')
            plt.legend(loc='upper left', bbox_to_anchor=(1.3, 1),labels=['%s, %1.2f %%' % (l, s / 100) for l, s in zip(names, chars)])
            pdf.savefig()