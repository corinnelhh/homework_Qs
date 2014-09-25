##Homework Qs
===========

1. The solution shown here is an object-oriented implementation of <a href="http://norvig.com/sudoku.html">Peter Norvig's algorithm</a>. The pre-processing stage for the algorithm is simple; the program reads in a file provided at the command line (i.e. `python solve.py input.txt`) and parses a 9x9 csv-separated multi-line grid into an 81-character string containing digits and dots representing cells with unknown values. Norvig's algorithm works by taking two basic principles:
 
    (1) If a square has only one possible value, then eliminate that value from the square's peers.
    (2) If a unit has only one possible place for a value, then put the value there.

and abstracting these principles out byb a process he terms 'constraint propogation' (in other words, taking a known constraint and applying it to all other possible 

The algorithm works by first providing a unique alphanumeric identifier (i.e. 'A1' or 'G6') for each cell in the 9 x 9 grid, and then by identifying each individual cell by membership in three 'units' (the cell's row, column, and subsquare); the other cells belonging to those units are then knwon as the cell's 'peers'. The next step the algorithm takes is to cast these cells into a dictionary/hash table, where each cell name points to a string representing all possible values for a Sudoku cell (i.e. '123456789'); the dictionary is then checked against the 'known' cell values from the input grid, and all 'impossible' values are recursively 


2. The Big-O notation of this program is O(V + E), where V is the number of vertices () and E the number of edges (). In the worst case scenario,   However, the expected runtime is significantly better, as outlined by Norvig in his extensive benchmarking. 

3. The program is designed this way because (a) the given parameters were to explore an object-oriented approach, and (b) the detailed benchmarking of Norvig's algorithm demonstrate that it is extremely efficient at solving sudoku programs. The combination of using a recursive, depth-first seach algorithm to eliminate impossible values for given cells and using the principle of constraint propogation to eliminate possibilities from a cell's peers's possible values allows the algorithm to be extremely efficient at identifying solutions. 
4. Other decisions I might have made include using an array/set-based approach; however, Norvig explains that the Python string copying function .copy() is more efficient than .copy().deepcopy(), which would be required to copy lists or sets. I initially began writing out the class using lists (the Python term for an array), but stumbled across Norvig's convincing explanation of why strings were more efficient and decided to adopt his approach.
