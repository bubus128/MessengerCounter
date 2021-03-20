from Conversation import Conversation
from Plotter import Plotter
from tkinter.filedialog import askdirectory

if __name__ == '__main__':
    # dir chooser
    path = askdirectory()
    # reading conversation
    conv = Conversation(path)
    # plot results
    plot = Plotter(conv)
