import tests as t
# a 9x9 grid, check if solution is valid
#valid solution is:
#rows contain numbers 1 - 9 uniqu
#columns contain numbers 1-9 unique
#sub cubes (3x3) contain numbers 1-9

def main():
    def valid_solution(board):
        def get_cubes(cube_list):
            first_cube = [number for row in cube_list[0:3] for number in row]
            second_cube = [number for row in cube_list[3:6] for number in row]
            third_cube = [number for row in cube_list[6:] for number in row]
            return [first_cube, second_cube, third_cube]

        #check for 0s and negative numbers and numbers over 9
        first_third = []
        second_third = []
        third_third = []

        for array in board:
            if len(array) < 9:
                False
            if 0 in array:
                return False
            for i in array:
                if i < 1 or i > 9:
                    return False
            if len(array) != len(set(array)): #check if rows have duplicates
                return False
            first_third.append(array[0:3])
            second_third.append(array[3:6])
            third_third.append(array[6:])

        first_third = get_cubes(first_third) # this checks the validity of the subcubes
        second_third = get_cubes(second_third)
        third_third = get_cubes(third_third)
        grid = [first_third, second_third, third_third]
        for thir in grid:
            for cube in thir:
                if len(cube) != len(set(cube)):
                    return False

        # check validity of columns
        column = 0
        while column < len(board[0]):
            column_as_list = []
            for row in range(0, len(board[0])):
                column_as_list.append(board[row][column])
            if len(column_as_list) != len(set(column_as_list)):
                return False
            column += 1
        return True
    print(t.assert_equals(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                                   [6, 7, 2, 1, 9, 5, 3, 4, 8],
                                   [1, 9, 8, 3, 4, 2, 5, 6, 7],
                                   [8, 5, 9, 7, 6, 1, 4, 2, 3],
                                   [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                   [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                   [9, 6, 1, 5, 3, 7, 2, 8, 4],
                                   [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                   [3, 4, 5, 2, 8, 6, 1, 7, 9]]), True))

    print(t.assert_equals(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                                   [6, 7, 2, 1, 9, 0, 3, 4, 9],
                                   [1, 0, 0, 3, 4, 2, 5, 6, 0],
                                   [8, 5, 9, 7, 6, 1, 0, 2, 0],
                                   [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                   [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                   [9, 0, 1, 5, 3, 7, 2, 1, 4],
                                   [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                   [3, 0, 0, 4, 8, 1, 1, 7, 9]]),False))
    return None
if __name__ == '__main__':
    main()
