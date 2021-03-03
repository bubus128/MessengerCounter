import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

class Plotter:
    outputLoc=r'output\outpu.pdf'
    def __init__(self,conversation):
        names=conversation.getNames()
        messages=conversation.getMessages()
        chars=conversation.getChars()
        totalChars=conversation.usersRepo.totalChars()
        totalMessages=conversation.usersRepo.totalMessaes()
        with PdfPages(self.outputLoc) as pdf:
            plt.figure(figsize=[11.69,8.27])
            plt.pie(messages,labels=names, autopct='%1.2f%%')
            plt.title("procentowy udział względem wysłanych wiadomości").set_ha("left")
            plt.legend(loc='upper left',bbox_to_anchor=(1.3, 1),labels=['%s, %1.2f %%' % (l, s/totalMessages*100) for l, s in zip(names, messages)])
            plt.subplots_adjust(left=0.1, right=0.55)
            pdf.savefig()
            plt.close()

            plt.figure(figsize=[11.69, 8.27])
            plt.pie(chars,labels=names, autopct='%1.2f%%')
            plt.title("procentowy udział względem wysłanych znaków").set_ha("left")
            plt.legend(loc='upper left', bbox_to_anchor=(1.3, 1),labels=['%s, %1.2f %%' % (l, s/totalChars*100) for l, s in zip(names, chars)])
            plt.subplots_adjust(left=0.1, right=0.55)
            pdf.savefig()
            plt.close()