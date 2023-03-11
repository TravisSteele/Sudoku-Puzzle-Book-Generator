import random

class Sudoku:
    def __init__(self,puzzle='0'*81):
        self.isfull = False
        self.once = False
        self.twice = False
        self.checked = True
        self.nums = list(range(81))
        self.meta = puzzle
        self.fill(puzzle)
    def fill(self,a='0'*81):
        def samerow(i,j): return (i/9 == j/9)
        def samecol(i,j): return (i-j) % 9 == 0
        def samebox(i,j): return (i/27 == j/27 and i%9/3 == j%9/3)
        i = a.find('0')
        if i == -1:
            self.isfull = True
            self.meta = a
        exnums = set()
        for j in range(81):
            if samerow(i,j) or samecol(i,j) or samebox(i,j):
                exnums.add(a[j])
        for m in ''.join(random.sample('123456789',9)):
            if self.isfull:
                break
            else:
                if m not in exnums:
                    self.fill(a[:i]+m+a[i+1:])
    def sieve(self,numcells,wipstr=None):
        if numcells == 0 or len(self.nums) == 0:
            return wipstr
        random.shuffle(self.nums)
        i = self.nums.pop()
        if wipstr == None:
            copy = self.meta[:i] + '0' + self.meta[i+1:]
        else:
            copy = wipstr[:i] + '0' + wipstr[i+1:]
        self.once = False
        self.twice = False
        self.checked = True
        self.check(copy)
        if self.checked:
            return self.sieve(numcells-1,copy)
        else:
            return self.sieve(numcells,wipstr)
    def check(self,a):
        def samerow(i,j): return (i/9 == j/9)
        def samecol(i,j): return (i-j) % 9 == 0
        def samebox(i,j): return (i/27 == j/27 and i%9/3 == j%9/3)
        i = a.find('0')
        if i == -1:
            if self.once:
                self.twice = True
                self.checked = False
            else:
                self.once = True
        exnums = set()
        for j in range(81):
            if samerow(i,j) or samecol(i,j) or samebox(i,j):
                exnums.add(a[j])
        for m in ''.join(random.sample('123456789',9)):
            if self.twice:
                break
            elif m not in exnums:
                self.check(a[:i]+m+a[i+1:])

def generate(num_puzzles):
    for i in range(num_puzzles):
        s = Sudoku()
        p = s.sieve(24)
        with open("puzzles.txt",'a') as f:
            f.write(p + '\n')
        with open("Solutions.txt",'a') as f:
            f.write(s.meta + '\n')
