class Assembler:
    def __init__(self):
        self.REG = [0] * 10
        self.MEM = [0] * 100
        self.PC = 0
        self.FLAG = 0

    def MOV(self,value1,value2):
        if value1[0]=="[" and value1[-1]=="]":
            if value2[0]=="[" and value2[-1]=="]":
                self.MEM[int(value1[1:-1])] = self.MEM[int(value2[1:-1])]
            else:
                self.MEM[int(value1[1:-1])] = self.REG[int(value2)]
        else:
            if value2[0]=="[" and value2[-1]=="]":
                self.REG[int(value1)] = self.MEM[int(value2[1:-1])]
            else:
                self.REG[int(value1)] = self.REG[int(value2)]

    def ADD(self, reg1, reg2, reg3):
        self.REG[reg3] = self.REG[reg1] + self.REG[reg2]

    def SUB(self, reg1, reg2, reg3):
        self.REG[reg3] = self.REG[reg1] - self.REG[reg2]

    def MUL(self, reg1, reg2, reg3):
        self.REG[reg3] = self.REG[reg1] * self.REG[reg2]

    def DIV(self, reg1, reg2, reg3):
        self.REG[reg3] = self.REG[reg1] // self.REG[reg2]

    def JMP(self, addr):
        self.PC = addr

    def JZ(self, reg, addr):
        if self.REG[reg] == 0:
            self.PC = addr

    def JNZ(self, reg, addr):
        if self.REG[reg] != 0:
            self.PC = addr

    def COMP(self, reg1, reg2):
        if self.REG[reg1] < self.REG[reg2]:
            self.FLAG = -1
        elif self.REG[reg1] > self.REG[reg2]:
            self.FLAG = 1
        else:
            self.FLAG = 0

    def HLT(self):
        pass

    def run(self,code):
        while self.PC < len(code):
            inst = code[self.PC]
            if inst[0] == "MOV":
                self.MOV(inst[1],inst[2])
            elif inst[0] == "ADD":
                self.ADD(int(inst[1]),int(inst[2]),int(inst[3]))
            elif inst[0] == "SUB":
                self.SUB(int(inst[1]),int(inst[2]),int(inst[3]))
            elif inst[0] == "MUL":
                self.MUL(int(inst[1]),int(inst[2]),int(inst[3]))
            elif inst[0] == "DIV":
                self.DIV(int(inst[1]),int(inst[2]),int(inst[3]))
            elif inst[0] == "JMP":
                self.JMP(int(inst[1]))
            elif inst[0] == "JZ":
                self.JZ(int(inst[1]),int(inst[2]))
            elif inst[0] == "JNZ":
                self.JNZ(int(inst[1]),int(inst[2]))
            elif inst[0] == "COMP":
                self.COMP(int(inst[1]),int(inst[2]))
            elif inst[0] == "HLT":
                self.HLT()
                break
            self.PC += 1