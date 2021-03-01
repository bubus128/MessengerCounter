from Conversation import Conversation
from Plotter import Plotter

path=r'D:\Python\messages data\messages\inbox\niestetycosposzlonietak_kuakwbs37w\message_1.html'    #ścieżka do folderu z konwersacją
if __name__ == '__main__' :
    conv=Conversation(path)
    plot=Plotter(conv)