# object-oriented implementation of Peter Norvig's solution at:
# http://norvig.com/sudoku.html

import sys


class SudokuSolver(object):

    def __init__(self, grid):
        self.grid = self.format_input(grid)
        # self.grid = grid
        self.digits = '123456789'
        self.rows = 'ABCDEFGHI'
        self.squares = self.cross(self.rows, self.digits)
        self.unitlist = (
            [self.cross(self.rows, c) for c in self.digits] +
            [self.cross(r, self.digits) for r in self.rows] +
            [self.cross(rs, cs) for rs in (
                'ABC', 'DEF', 'GHI') for cs in (
                '123', '456', '789')]
        )
        self.units = dict((
            s, [u for u in self.unitlist if s in u])
            for s in self.squares)
        self.peers = dict(
            (s, set(sum(self.units[s], [])) - set([s]))
            for s in self.squares)
        self.solution = None

    def cross(self, A, B):
        u"Cross product of elements in A and elements in B."
        return [a + b for a in A for b in B]

    def format_input(self, grid):
        g = [l.split(",") for l in grid.splitlines()]
        return [item for sublist in g for item in sublist]

    def parse_grid(self):
        u"""Convert grid to a dict of possible values, {square: digits}, or
        return False if a contradiction is detected."""
        values = dict((s, self.digits) for s in self.squares)
        for s, d in self.grid_values().items():
            if d in self.digits and not self.assign(values, s, d):
                return False
        return values

    def grid_values(self):
        u"""Convert grid into a dict of {square: char}
        with '0' or '.' for empties."""
        chars = [c if c in self.digits or c in '0.' else "." for c in self.grid]
        if len(chars) != 81:
            raise ValueError("Invalid input grid; grid must be 9x9.")
        return dict(zip(self.squares, chars))

    def assign(self, values, s, d):
        u"""Eliminate all the other values (except d)
        from values[s] and propagate.
        Return values, except return False if a contradiction is detected."""
        other_values = values[s].replace(d, '')
        if all(self.eliminate(values, s, d2) for d2 in other_values):
            return values
        else:
            return False

    def eliminate(self, values, s, d):
        u"""Eliminate d from values[s]; propagate when values or places <= 2.
        Return values, except return False if a contradiction is detected."""
        if d not in values[s]:
            return values
        values[s] = values[s].replace(d, '')
        if len(values[s]) == 0:
            return False
        elif len(values[s]) == 1:
            d2 = values[s]
            if not all(self.eliminate(values, s2, d2) for s2 in self.peers[s]):
                return False
        for u in self.units[s]:
            dplaces = [s for s in u if d in values[s]]
            if len(dplaces) == 0:
                return False
            elif len(dplaces) == 1:
                if not self.assign(values, dplaces[0], d):
                    return False
        return values

    def search(self, values):
        "Using depth-first search and propagation, try all possible values."
        if values is False:
            return False
        if all(len(values[s]) == 1 for s in self.squares):
            return values
        n, s = min(
            (len(values[s]), s) for s in self.squares if len(
                values[s]) > 1)
        return self.some(self.search(
            self.assign(values.copy(), s, d)) for d in values[s])

    def some(self, seq):
        "Return some element of seq that is true."
        for e in seq:
            if e:
                return e
        return False

    def display(self):
        print "\n"
        if self.solution:
            for r in self.rows:
                print ''.join(self.solution[r + c] + (
                    "" if not (int(c) % 9) else ',') for c in self.digits)
        else:
            print "Invalid starting board: no solution possible."
        print "\n"

    def solve(self):
        self.solution = self.search(self.parse_grid())

if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.exit("Please provide a filename.")

    with open(sys.argv[1], 'r') as f:
        ss = SudokuSolver(f.read().strip())
        ss.solve()
        ss.display()
