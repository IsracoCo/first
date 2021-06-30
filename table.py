import random
import math
def TOF():
    n = random.random()%2
    if(n):
        return True
    else :
        return False

def sample_without(number):
    l = random.sample(range(1, 10), 9)
    l.pop(l.index(number))
    return l
class STable:
    def __init__(self, to_remove):
        self.table = [[0 for i in range(9)] for i in range(9)]
        self.tr = to_remove
    
    def group(self, num):
        l = []
        for i in range(3):
            l.append(self.table[math.floor(num/3)*3][(num%3) * 3 + i])
        for i in range(3):
            l.append(self.table[math.floor(num/3)*3 + 1][(num%3) * 3 + i])
        for i in range(3):
            l.append(self.table[math.floor(num/3)*3 + 2][(num%3) * 3 + i])
        return l
    
    def col(self, num):
        l = []
        for i in range(9):
            l.append(self.table[i][num])
        return l

    def line(self, num):
        return self.table[num]
    
    def start(self):
        
        self.generate()
        self.defill()


    def fill(self):
        filled = 0
        listON = random.sample(range(1, 10), 9)
        for i in range(9):
            self.table[i][0] = listON[i]
        l = sample_without(self.table[0][0])
        for i in range(8):
            self.table[0][i + 1] = l[i]
    
    def not_possible(self, y, x):
        l = []
        l1 = self.line(y)
        l2 = self.col(x)
        l3 = self.group(math.floor(y/3)*3 + math.floor(x/3))

        for i in range(len(l1)):
            if(not l1[i] in l1):
                l.append(l1[i])        

        for i in range(len(l2)):
            if(not l2[i] in l2):
                l.append(l2[i])  
        
        for i in range(len(l3)):
            if(not l3[i] in l3):
                l.append(l3[i])  

        return l
    def generate(self):
        self.fill()
        l = self.not_solved()
        for i in l:
            pass
    def legal(self):
        for i in range(9):
            for h in range(9):
                if(self.table[i][h] in self.not_possible(i, h)):
                    return False
        return True
                


    def defill(self):
        l = random.sample(range(81), self.tr)
        for i in l:
            self.table[math.floor(i/9)][i%9] = 0



    def possible(self, y, x):
        l = []
        np = self.not_possible(y, x)
        temp = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in temp:
            if(not i in np):
                l.append(i)
        return l

    def not_solved(self):
        l = []
        for i in range(9):
            for h in range(9):
                if(self.table[i][h] == 0):
                    l.append((i, h))

    def solve():
        pass



    def print(self): 
        for i in self.table:
            print(i)
    



        
s = STable(10)
s.start()
s.print()



        
