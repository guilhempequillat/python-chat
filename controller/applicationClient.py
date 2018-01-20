from view.interface import Interface
from networkingClient import Networking
import model.message
from Tkinter import *

class Application:
    
    def __init__(self):
        self.index = 0
        self.networkingCreation()
        self.interfaceCreation()
        
        
    def interfaceCreation(self):
        self.fenetre = Tk()
        
        self.textEntry = Entry(self.fenetre, textvariable="Text", width=30)
        self.buttonShowMessage = Button(self.fenetre, text="Show message", command=self.showValue)
        self.text = StringVar()
        
        
        
        frame = Frame(self.fenetre, borderwidth=2, relief=GROOVE,width=35,height=50)
        #Frame1.pack(side=LEFT, padx=3, pady=3)        
        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        self.textList = Listbox(frame,width=35,height=15)
        
        self.textLabel = Label(frame, textvariable = self.text)
        self.text.set("")
        scrollbar.config(command=self.textList.yview)
        
        self.buttonClose = Button(self.fenetre, text="Fermer", command=self.closeApplication)
        
        self.networking.setTextList(self.textList)
        self.interface = Interface(self.fenetre,self.buttonClose,self.textEntry,self.buttonShowMessage,self.textLabel,self.textList,frame)
        self.interface.mainloop()
        self.interface.destroy()
        
    def networkingCreation(self):
        self.networking = Networking()
        self.networking.start()
        
    def closeApplication(self):
        self.fenetre.quit()
        self.networking.stop()
        
    def showValue(self):
        value = StringVar()
        value = self.textEntry.get()
        messageSend = model.message.Message("Client", str(value))
       
        self.networking.sendMessage(messageSend)
        self.updateIndex()
        
        self.textList.insert(self.index , str(messageSend))
        self.incrementIndex()
        print(value)    
        
    def changeTextLabel(self,value):
        self.text.set(value)
        self.textLabel.pack()
        
    def incrementIndex(self):
        self.networking.incrementIndex()
        self.index +=1
        
    def updateIndex(self):
        self.index = self.networking.getIndex()