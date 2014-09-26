##Homework Qs
===========

1. The solution shown here is an object-oriented implementation of <a href="http://norvig.com/sudoku.html">Peter Norvig's design-driven algorithm</a>. The pre-processing stage for the algorithm is simple; the program reads in a file provided at the command line (i.e. `python solve.py input.txt`) and parses a 9x9 csv formatted multi-line grid into an 81-character string containing digits and dots representing cells with unknown values. Norvig's algorithm works by taking two basic principles:
    (1) If a square has only one possible value, then eliminate that value from the square's peers ('peers' are explained below).
    (2) If a unit has only one possible place for a value, then put the value there.
and abstracting these principles out by a process called 'constraint propogation' (in other words, taking a single known constraint and making inferences about how that constraint affects other elements in the system).  

The set up for the algorithm works by first providing a unique alphanumeric identifier (i.e. 'A1' or 'G6') for each cell in the 9 x 9 grid, and then by identifying each individual cell by membership in three 'units' (the cell's row, column, and subsquare); the other cells belonging to those units are then knwon as the cell's 'peers'. The next step the algorithm takes is to cast these so-far undifferentiated cells into a dictionary/hash table, where each cell name points to a string representing all possible values for a Sudoku cell (i.e. '123456789'); the dictionary is then checked against the 'known' cell values from the input grid, and all 'impossible' values are recursively eliminated from a given cell's values and those of its peers.

Once this set up stage is completed, many puzzles will already have solutions; for those that do not, the algorithm then implements a depth-first search, cell-by-cell, to identify possible solutions. The algorithm begins with the cells that have the fewest possible values (since the chance of correctly guessing the value is greater if there are only two possible answers than if there are five); the algorithm arbitrarily chooses one of the possible answers, then checks each of the cell's peers (and each of their peers) until either a complete valid solution is reached (at which point the search algorithm terminates) or a cell is reached where the only possible cell value (according to the arbitrary value chosen for the first cell on this search) is not in the particular cell's set of possible values. In this last case, where an impossible value is required, the algorithm goes back to the beginning and recursively chooses another value for the starting cell, then executes the search again. 

2. The Big-O notation of the depth-first algorithm is O(n * m), where n is the number of possible values for each cell (here, 9) and m is the number of blank cells (which varies, but is usually at least 40 or 50. However, the expected runtime is significantly better, as outlined by Norvig in his extensive benchmarking; in the best case scenario, the algorithm would have effectively constant time (if, for example, the correct value were initially selected for each cell), while the general expected runtime would be O(n).

3. The program is designed this way because (a) the given parameters were to explore an object-oriented approach, and (b) as Norvig explains, the combination of using a recursive, depth-first seach algorithm to eliminate impossible values for given cells and using the principle of constraint propogation to eliminate possibilities from a cell's peers's possible values allows the algorithm to be extremely efficient at identifying solutions. There is huge value, in my experience, in building systems on already identified efficient solutions and focusing innovative attention on non-optimized parts of a system!

4. Other decisions I might have made include using an array/set-based approach; however, Norvig explains that the Python string copying function .copy() is more efficient than .copy().deepcopy(), which would be required to copy lists or sets. I initially began writing out the class using lists (the Python term for an array), but stumbled across Norvig's convincing explanation of why strings were more efficient and decided to adopt his approach. Another approach might be to make this a more 'pure' object-oriented approach (like that <a href="http://xprogramming.com/articles/sudoku5/">explored by Ron Jeffries</a>; this approach, however, did not seem to be as efficient as the algorithm outlined by Norvig. The solution I presented here takes a middle ground and incorporates the design-driven efficiency of Norvig's approach into an object-oriented design. 
