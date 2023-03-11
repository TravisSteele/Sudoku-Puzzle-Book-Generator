# Sudoku-Puzzle-Book-Generator
Generates HTML pages with sudoku puzzles and solutions, converts the pages to PDF with wkhtmltopdf, and merges the pages together with the PyPDF2 package. Written in Python 2, and may not work on Linux or Mac.

For the code to run, 'Sudoku.py' and 'writer.py' must be placed in the same directory as wkhtmltopdf.exe and wkhtmltox.dll.

|=============|
|  Sudoku.py  |
|=============|

The Sudoku class represents a sudoku puzzle. Inside this class is the field 'puzzle' which is a string of 81 digits between 0 and 9. The first nine characters represent the first row of the puzzle, the next nine characters represent the second row, and so on. A zero only appears in unsolved puzzles and represents a blank cell.
If initialized without any arguments, the puzzle field will be set to a string of 81 zeros.
The Sudoku class has three methods: 'fill' tries to fill in blank cells with valid digits, 'check' determines whether the puzzle is solvable, and 'sieve' tries to make a given number of cells blank while preserving the solvability of the puzzle.
The 'generate' function takes one argument, num_puzzles, and generates that many solved sudoku puzzles. The solved puzzles are saved to 'Solutions.txt' and 'sieve' is called to eliminate up to 24 cells from each puzzle. The resulting unsolved puzzles are saved to 'puzzles.txt'.

|=============|
|  writer.py  |
|=============|

The 'grid' function generates HTML code for a 9x9 grid as an <svg> element.
The Page class is initialized with two strings of 81 digits between 0 and 9, and the 'write' method makes an HTML document with the corresponding puzzles, a number to identify the puzzles, a page number, and a page number for the solutions.
The Spage class is similar to the Page class, but it takes six strings instead of two. An HTML document is made displaying these six puzzles, with each puzzle number displayed below the respective puzzle, and a page number.
The rest of the code reads 'puzzles.txt' and 'Solutions.txt' and prints them on HTML pages, then converts them to PDF documents with os.system and wkhtmltopdf.
Finally, the pdf documents are merged into a single document.
