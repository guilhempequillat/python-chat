from Tkinter import *

class Interface(Frame):  
    
    def __init__(self, fenetre, buttonClose,textEntry,buttonShowMessage,textLabel,textList,frame, **kwargs):
        Frame.__init__(self, fenetre, width=900, height=200, **kwargs)
        p = PanedWindow(fenetre, orient=VERTICAL)
        textEntry.pack()
        
        textLabel.pack()
        textList.pack()
        
        buttonShowMessage.pack()
        frame.pack()
        buttonClose.pack()