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
            self.chartCreate("procentowy udział względem wysłanych wiadomości",messages,names,totalMessages)
            pdf.savefig()
            plt.close()

            self.chartCreate("procentowy udział względem wysłanych znaków", chars, names, totalChars)
            pdf.savefig()
            plt.close()


    def chartCreate(self,title,values,lables,maxValue):
        plt.figure(figsize=[11.69, 8.27])
        plt.pie(values, labels=lables, autopct='%1.2f%%')
        plt.title(title).set_ha("left")
        plt.legend(loc='upper left', bbox_to_anchor=(1.3, 1),
                   labels=['%s, %1.2f %%' % (l, s / maxValue * 100) for l, s in zip(lables, values)])
        plt.subplots_adjust(left=0.1, right=0.55)