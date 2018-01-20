import socket
import threading
import time
from model.message import Message

class Networking(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self)
        self.host = "localhost"
        self.port = 1477
        self.index = 0
        
    def run(self):
        self._stopevent = threading.Event()
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((self.host, self.port))
        print("connection done")
        self.connected = True
                
                
        while not self._stopevent.isSet():
            self.connection.settimeout(2)
            try:
                msg_recu = self.connection.recv(1024)
            except socket.timeout:
                print("No messages")
            else:
                self.showRecivedMessage(msg_recu.decode())
            time.sleep(2.0) 
        
        self.connection.close()
        if self.connected:
            self.connection.close()
               
    def stopNetworking(self):
        self.connection.close()
        print("Stop")
        
    def stop(self):
        self._stopevent.set()
        
    def sendMessage(self, message):
        if self.connected:
            self.connection.send(str(message))
        else:
            print("Not connected")
            
    def showRecivedMessage(self, text):
        self.textList.insert(self.index , str(text))
        self.incrementIndex()      
        
    def setTextList(self, textList):
        self.textList = textList

    def incrementIndex(self):
        self.index += 1
        
    def getIndex(self):
        return self.index