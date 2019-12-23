import copy  
import time

class SudokuSolver:
    def solve( puzzle ):
        solution = copy.deepcopy( puzzle )
        if SudokuSolver.solve_helper( solution ):
            return solution
        return None

    def solve_helper( solution ):
        minPossibleValueCountCell = None
        while True:
            minPossibleValueCountCell = None
            for rowIndex in range( 9 ):
                for columnIndex in range( 9 ):
                    if solution[ rowIndex ][ columnIndex ] != 0:
                        continue
                    possibleValues = SudokuSolver.find_possible_values( rowIndex, columnIndex, solution )
                    possibleValueCount = len( possibleValues )
                    if possibleValueCount == 0:
                        return False
                    if possibleValueCount == 1:
                        solution[ rowIndex ][ columnIndex ] = possibleValues.pop()
                    if not minPossibleValueCountCell or \
                       possibleValueCount < len( minPossibleValueCountCell[ 1 ] ):
                        minPossibleValueCountCell = ( ( rowIndex, columnIndex ), possibleValues )
            if not minPossibleValueCountCell:
                return True
            elif 1 < len( minPossibleValueCountCell[ 1 ] ):
                break
        r, c = minPossibleValueCountCell[ 0 ]
        for v in minPossibleValueCountCell[ 1 ]:
            solutionCopy = copy.deepcopy( solution )
            solutionCopy[ r ][ c ] = v
            if SudokuSolver.solve_helper( solutionCopy ):
                for r in range( 9 ):
                    for c in range( 9 ):
                        solution[ r ][ c ] = solutionCopy[ r ][ c ]
                return True
        return False

    def find_possible_values( rowIndex, columnIndex, puzzle ):
        values = { v for v in range( 1, 10 ) }
        values -= SudokuSolver.get_row_values( rowIndex, puzzle )
        values -= SudokuSolver.get_column_values( columnIndex, puzzle )
        values -= SudokuSolver.get_block_values( rowIndex, columnIndex, puzzle )
        return values

    def get_row_values( rowIndex, puzzle ):
        return set( puzzle[ rowIndex ][ : ] )

    def get_column_values( columnIndex, puzzle ):
        return { puzzle[ r ][ columnIndex ] for r in range( 9 ) }

    def get_block_values( rowIndex, columnIndex, puzzle ):
        blockRowStart = 3 * ( rowIndex // 3 )
        blockColumnStart = 3 * ( columnIndex // 3 )
        return {
            puzzle[ blockRowStart + r ][ blockColumnStart + c ]
                for r in range( 3 )
                for c in range( 3 )
        }


