class CSVManager:
    
    header = []
    data = {}
    filePath = ""
    with_header = True
    
    def __init__(self, filePath: str, with_header: bool = True, auto_load: bool = True):
        print("CSVManager[__init__]: with filePath: " + filePath + " and with_header: " + str(with_header) + ".")
        self.filePath = filePath
        self.with_header = with_header
        if (auto_load): self.load()
    
    def setFilePath(self, filePath: str):
        self.filePath = filePath
        
    def getFilePath(self):
        return self.filePath
    
    def load(self):
        print("CSVManager[load]: loading file: " + self.filePath + ".")
        read_str = ""
        with open(self.filePath, 'r', encoding='utf-8-sig') as f: read_str = f.read()
        read_str = read_str.split('\n')
        if (self.with_header):
            print("CSVManager[load]: getting header from file: " + self.filePath + ".")
            self.header = read_str[0].split(',')
            print("CSVManager[load]: header: " + str(self.header) + ".")
            read_str.pop(0)
        else:  self.header = [i for i in range(len(read_str[0].split(',')))]
        listing_data = []
        for i in range(len(read_str)): listing_data.append(read_str[i].split(','))
        for i in range(len(listing_data)): 
            data_line = {}
            if (len(listing_data[i]) != len(self.header)): # throw errr
                if (len(listing_data[i]) == 0): continue
                raise Exception("Error: CSVManager: load: line " + str(i) + " has " + str(len(listing_data[i])) + " columns, but header has " + str(len(self.header)) + " columns.")
            for j in range(len(self.header)): data_line[self.header[j]] = listing_data[i][j]
            print("CSVManager[load]: adding data line: " + str(data_line) + ".")
            self.data[listing_data[i][0]] = data_line
        print("CSVManager[load]: data loaded.")
        
    def getData(self):
        return self.data
    
    def setData(self, data):
        self.data = data
    
    def getHeader(self):
        return self.header
    
    def setHeader(self, header):
        self.header = header
    
    def save(self): # write to csv file line by line
        print("CSVManager[save]: saving data to file: " + self.filePath + ".")
        f = open(self.filePath, 'w', encoding="utf8")
        f.write(','.join(self.header) + '\n')
        f.close()
        f = open(self.filePath, 'a', encoding="utf8")
        for i in self.data: f.write(','.join([str(self.data[i][j]) for j in self.header]) + '\n')
        f.close()