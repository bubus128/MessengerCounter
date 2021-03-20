import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

class Plotter:
    outputLoc=r'output\\'
    def __init__(self,conversation):
        self.conversation=conversation
        self.data=conversation.getData()
        self.plotChars()


    def plotChars(self):
        with PdfPages(self.outputLoc+self.conversation.title+".pdf") as pdf:
            title = "statistics of \"{}\" conversation"
            info = pdf.infodict()
            info["Title"] = title.format(self.conversation.title)
            #sorting data by count of messages sent
            self.data=dict(sorted(list(self.data.items()),key=lambda item:item[1].messages,reverse=True))
            messages=self.getMessages()
            self.chartCreate("percentage of messages sent",messages,self.getNames(),sum(messages))
            pdf.savefig()
            plt.close()
            # sorting data by count of messages sent
            self.data = dict(sorted(list(self.data.items()), key=lambda item: item[1].chars, reverse=True))
            chars = self.getChars()
            self.chartCreate("percentage of chars in messages sent", chars, self.getNames(), sum(chars))
            pdf.savefig()
            plt.close()

    def chartCreate(self,title,values,lables,maxValue):
        plt.figure(figsize=[11.69, 8.27])
        plt.pie(values, labels=lables, autopct='%1.2f%%')
        plt.title(title).set_ha("left")
        plt.legend(loc='upper left', bbox_to_anchor=(1.3, 1),
                   labels=['%s, %1.2f %%' % (l, s / maxValue * 100) for l, s in zip(lables, values)])
        plt.subplots_adjust(left=0.1, right=0.55)

    # return messages counts for each user
    def getMessages(self):
        return list(user.messages for user in (self.data.values()))

    # return chars counts for each user
    def getChars(self):
        return list(user.chars for user in (self.data.values()))

    # return names of users
    def getNames(self):
        return list(user.name for user in (self.data.values()))