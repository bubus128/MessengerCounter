import glob

from Conversation import Conversation
from Plotter import Plotter
from tkinter.filedialog import askdirectory

if __name__ == '__main__' :
    #file chooser
    path= askdirectory()
    files=glob.glob(path+"/*.html")
    conv=Conversation(files)
    plot=Plotter(conv)