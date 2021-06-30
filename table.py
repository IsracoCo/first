import random
def TOF():
    n = random.random()%2
    if(n):
        return True
    else :
        return False

class STable:
    def __init__(self, to_fill):
        self.table = [[0 for i in range(9)] for j in range(9)] 
        self.tf = to_fill


    def fill(self):
        filled = 0
        

        
        
    

s = STable(70)
s.fill()
print(s.table)
        







