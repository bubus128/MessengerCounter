import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

class Plotter:
    outputLoc=r'output\outpu.pdf'
    def __init__(self,conversation):
        self.conversation=conversation
        self.totalChars=conversation.usersRepo.totalChars()
        self.totalMessages=conversation.usersRepo.totalMessaes()
        self.plotChars()


    def plotChars(self):
        with PdfPages(self.outputLoc) as pdf:
            info = pdf.infodict()
            title = "statistics of \"{}\" conversation"
            info["Title"] = title.format(self.conversation.title)
            self.chartCreate("percentage of messages sent",self.conversation.getMessages(),self.conversation.getNames(),self.totalMessages)
            pdf.savefig()
            plt.close()

            self.chartCreate("percentage of chars in messages sent", self.conversation.getChars(), self.conversation.getNames(), self.totalChars)
            pdf.savefig()
            plt.close()

    def chartCreate(self,title,values,lables,maxValue):
        plt.figure(figsize=[11.69, 8.27])
        plt.pie(values, labels=lables, autopct='%1.2f%%')
        plt.title(title).set_ha("left")
        plt.legend(loc='upper left', bbox_to_anchor=(1.3, 1),
                   labels=['%s, %1.2f %%' % (l, s / maxValue * 100) for l, s in zip(lables, values)])
        plt.subplots_adjust(left=0.1, right=0.55)