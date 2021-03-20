import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


class Plotter:
    outputLoc = r'output\\'

    def __init__(self, conversation):
        self.conversation = conversation
        self.data = conversation.get_data()
        self.plot_chars()

    def plot_chars(self):
        with PdfPages(self.outputLoc+self.conversation.title+".pdf") as pdf:
            title = "statistics of \"{}\" conversation"
            info = pdf.infodict()
            info["Title"] = title.format(self.conversation.title)
            # sorting data by count of messages sent
            self.data = dict(sorted(list(self.data.items()), key=lambda item: item[1].messages, reverse=True))
            messages = self.get_messages()
            self.chart_create("percentage of messages sent", messages, self.get_names(), sum(messages))
            pdf.savefig()
            plt.close()
            # sorting data by count of messages sent
            self.data = dict(sorted(list(self.data.items()), key=lambda item: item[1].chars, reverse=True))
            chars = self.get_chars()
            self.chart_create("percentage of chars in messages sent", chars, self.get_names(), sum(chars))
            pdf.savefig()
            plt.close()

    @staticmethod
    def chart_create(title, values, labels, max_value):
        plt.figure(figsize=[11.69, 8.27])
        plt.pie(values, labels=labels, autopct='%1.2f%%')
        plt.title(title).set_ha("left")
        plt.legend(loc='upper left', bbox_to_anchor=(1.3, 1),
                   labels=['%s, %1.2f %%' % (label, value / max_value * 100) for label, value in zip(labels, values)])
        plt.subplots_adjust(left=0.1, right=0.55)

    # return messages counts for each user
    def get_messages(self):
        return list(user.messages for user in (self.data.values()))

    # return chars counts for each user
    def get_chars(self):
        return list(user.chars for user in (self.data.values()))

    # return names of users
    def get_names(self):
        return list(user.name for user in (self.data.values()))
