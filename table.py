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
    def __init__(self, to_fill):
        self.table = [[0 for i in range(9)] for i in range(9)]
        self.tf = to_fill
        self.fill()
    
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
         

    def fill(self):
        filled = 0
        listON = random.sample(range(1, 10), 9)
        for i in range(9):
            self.table[i][0] = listON[i]
        l = sample_without(self.table[0][0])
        for i in range(8):
            self.table[0][i + 1] = l[i]
        



    def print(self): 
        for i in self.table:
            print(i)
    



        
s = STable(50)
s.print()
print("line number 7:")
print(s.line(7))



        
