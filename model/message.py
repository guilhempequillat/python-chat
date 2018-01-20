class Message:
    
    def __init__(self, userName, text):
        self.userName = userName
        self.text = text
        
    def __str__(self):
        return self.userName + " : " + self.text