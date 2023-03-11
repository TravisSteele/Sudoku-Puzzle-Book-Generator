import os
from Sudoku import Sudoku
from PyPDF2 import PdfFileMerger, PdfFileReader

def grid(puzzle,size='120'):
    n = size
    s =  '<svg height="'+n+'mm" width="'+n+'mm" align="center">\n'
    s += '<rect width="'+n+'mm" height="'+n+'mm" style="fill:rgb(255,255,255);stroke-width:8;stroke:rgb(0,0,0)" />\n'
    for i in [1,2,4,5,7,8]:
        m = str(i*(float(n)/9.0))
        s += '<line x1="'+m+'mm" y1="0mm" x2="'+m+'mm" y2="'+n+'mm" style="stroke:rgb(0,0,0);stroke-width:2" />\n'
        s += '<line x1="0mm" y1="'+m+'mm" x2="'+n+'mm" y2="'+m+'mm" style="stroke:rgb(0,0,0);stroke-width:2" />\n'
    for i in [3,6]:
        m = str(i*(float(n)/9.0))
        s += '<line x1="'+m+'mm" y1="0mm" x2="'+m+'mm" y2="'+n+'mm" style="stroke:rgb(0,0,0);stroke-width:4" />\n'
        s += '<line x1="0mm" y1="'+m+'mm" x2="'+n+'mm" y2="'+m+'mm" style="stroke:rgb(0,0,0);stroke-width:4" />\n'
    for i in range(9):
        for j in range(9):
            t = str(float(n)/12.0)
            mx = str((i*(float(n)/9.0)+float(n)/18.0))
            my = str((j*(float(n)/9.0)+float(n)/18.0)+float(t)/3.0)
            s += '<text x="'+mx+'mm" y="'+my+'mm" font-size="'+t+'mm" text-anchor="middle">'+puzzle[9*j+i]+'</text>\n'
    s += '</svg>\n'
    return s
    

class Page:
    def __init__(self, ptop, pbot):
        self.top = ptop.replace('0',' ')
        self.bot = pbot.replace('0',' ')
    def write(self, filepath, pNo, sPgNo=False):
        with open(filepath, 'w') as f:
            f.write("<!DOCTYPE html>\n")
            f.write("<html>\n")
            f.write("<body>\n")
            f.write('<div align="left" style="padding: 18mm 0mm 38mm 18mm;">\n')
            f.write('<div style="float: right; text-align: center; height: 120mm;"><h1>'+str(pNo)+'</h1></div>\n')
            f.write(grid(self.top))
            f.write('</div>\n')
            f.write('<div align="right" style="padding: 0mm 18mm 18mm 0mm;">\n')
            f.write('<div style="float: left; text-align: center; height: 120mm;"><h1>'+str(pNo+1)+'</h1></div>\n')
            f.write(grid(self.bot))
            f.write('</div>\n')
            if sPgNo:
                f.write('<h1>Solution on pg. '+str(sPgNo)+'</h1>\n')
            f.write("</body>\n")
            f.write("</html>")
            f.close()

class Spage:
    def __init__(self, p1, p2, p3, p4, p5, p6):
        self.puzzles = [p1,p2,p3,p4,p5,p6]
    def write(self, filepath, pNo, PgNo=False):
        with open(filepath, 'w') as f:
            f.write("<!DOCTYPE html>\n")
            f.write("<html>\n")
            f.write("<body>\n")
            f.write('<div height="20mm"></div>\n')
            f.write('<table cellpadding="18mm" align="center">\n')
            for i in range(3):
                f.write("<tr>\n")
                for j in range(2):
                    f.write("<td>\n")
                    f.write(grid(self.puzzles[2*i+j],'75'))
                    f.write('<h2 align="center">'+str(pNo+2*i+j)+'</h2>\n')
                    f.write("</td>\n")
                f.write("</tr>\n")
            f.write("</table>\n")
            if PgNo:
                f.write('<h1 align="center">'+str(PgNo)+'</h1>\n')
            f.write("</body>\n")
            f.write("</html>")
            f.close()

with open("puzzles.txt",'r') as f:
    d = f.read().split("\n")[:-1]
    l = (len(d) / 2) + 1

with open("Solutions.txt",'r') as f:
    e = f.read().split("\n")[:-1]
p = 1
s = l

while len(d) >= 6:
    p1 = d.pop()
    p2 = d.pop()
    p3 = d.pop()
    p4 = d.pop()
    p5 = d.pop()
    p6 = d.pop()

    s1 = e.pop()
    s2 = e.pop()
    s3 = e.pop()
    s4 = e.pop()
    s5 = e.pop()
    s6 = e.pop()
    
    Spage(s1,s2,s3,s4,s5,s6).write('html/s' + str(s) + '.html',p,s)
    os.system('wkhtmltopdf html/s'+str(s)+'.html s'+str(s)+'.pdf')
    
    Page(p1,p2).write('html/p' + str(p) + '.html',p,s)
    os.system('wkhtmltopdf html/p'+str(p)+'.html p'+str(p)+'.pdf')
    p+=2
    Page(p3,p4).write('html/p' + str(p) + '.html',p,s)
    os.system('wkhtmltopdf html/p'+str(p)+'.html p'+str(p)+'.pdf')
    p+=2
    Page(p5,p6).write('html/p' + str(p) + '.html',p,s)
    os.system('wkhtmltopdf html/p'+str(p)+'.html p'+str(p)+'.pdf')
    p+=2
    s+=1
    
merger = PdfFileMerger()
for i in range(1,p+1,2):
    try:
        merger.append(PdfFileReader(file('p'+str(i)+'.pdf','rb')))
    except:
        print("omitted" + str(i))
for i in range(l,s+1):
    try:
        merger.append(PdfFileReader(file('s'+str(i)+'.pdf','rb')))
    except:
        print("omitted" + str(i))
merger.write("puzzles.pdf")

for i in range(1,p+1,2):
    try:
        os.remove('p'+str(i)+'.pdf')
    except:
        print(str(i) + " does not exist.")
for i in range(l,s+1):
    try:
        os.remove('s'+str(i)+'.pdf')
    except:
        print(str(i) + " does not exist.")

