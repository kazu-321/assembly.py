class Assembler:
    def __init__(self):
        self.REG = [0] * 10
        self.MEM = [0] * 100
        self.PC = 0

    def LOAD(self, reg, value):
        self.REG[reg] = value

    def STORE(self, reg, addr):
        self.MEM[addr] = self.REG[reg]

    def ADD(self, reg1, reg2, reg3):
        self.REG[reg3] = self.REG[reg1] + self.REG[reg2]

    def SUB(self, reg1, reg2, reg3):
        self.REG[reg3] = self.REG[reg1] - self.REG[reg2]

    def MUL(self, reg1, reg2, reg3):
        self.REG[reg3] = self.REG[reg1] * self.REG[reg2]

    def DIV(self, reg1, reg2, reg3):
        self.REG[reg3] = self.REG[reg1] / self.REG[reg2]

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