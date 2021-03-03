from Conversation import Conversation
from Plotter import Plotter
from tkinter.filedialog import askopenfilename

if __name__ == '__main__' :
    #file chooser
    path= askopenfilename()
    conv=Conversation(path)
    plot=Plotter(conv)