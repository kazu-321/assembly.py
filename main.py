class assembly:
    def __init__(self):
        self.REG=[]
        self.OUTPUT=[]
    
    def load(self,reg,value):
        if reg>len(self.REG)-1:
            while reg>len(self.REG):
                self.REG.append("")
            self.REG.append(value)
        else:
            self.REG[reg]=value