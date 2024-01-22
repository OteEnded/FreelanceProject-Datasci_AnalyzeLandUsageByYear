class TXTManager:
    
    header = []
    data = ""
    filePath = ""
    
    def __init__(self, filePath: str, auto_load: bool = True):
        print("TXTManager[__init__]: with filePath: " + filePath + ".")
        self.filePath = filePath
        if (auto_load): self.load()
    
    def setFilePath(self, filePath: str):
        self.filePath = filePath
        
    def getFilePath(self):
        return self.filePath
    
    def load(self):
        print("TXTManager[load]: loading file: " + self.filePath + ".")
        with open(self.filePath, 'r', encoding="utf8") as f: self.data = f.read()
        print("TXTManager[load]: data loaded.")
        
    def getData(self):
        return self.data
    
    def setData(self, data):
        self.data = data
    
    def save(self): # write to csv file line by line
        print("TXTManager[save]: saving data to file: " + self.filePath + ".")
        f = open(self.filePath, 'w', encoding="utf8")
        f.write(self.data)
        f.close()