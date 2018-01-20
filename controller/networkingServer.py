import socket
import threading
import time
from model.message import Message

class Networking(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self)
        self.host = ''
        self.port = 1477
        self.index = 0
        
    def run(self):
        self._stopevent = threading.Event()
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.bind((self.host, self.port))
        self.connection.listen(5)
        print("connection ...")
        self.connected = False
        while not self._stopevent.isSet() and self.connected == False:
            self.connection.settimeout(2)
            try:
                print("try to connect")
                self.connection_client, infos_connexion = self.connection.accept()
            except socket.timeout:
                print("No Connection since 2 sec")
            else:
                self.connected = True
                print("Connection done")        
                
        while not self._stopevent.isSet():
            self.connection_client.settimeout(2)
            try:
                msg_recu = self.connection_client.recv(1024)
            except socket.timeout:
                print("No messages")
            else:
                self.showRecivedMessage(msg_recu.decode())
            time.sleep(2.0) 
        
        self.connection.close()
        if self.connected:
            self.connection_client.close()
               
    def stopNetworking(self):
        self.connection.close()
        print("Stop")
        
    def stop(self):
        self._stopevent.set()
        
    def sendMessage(self, message):
        if self.connected:
            self.connection_client.send(str(message))
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