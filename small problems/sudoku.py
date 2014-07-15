def check_sudoku(list):
    n=len(list) #Get the size of the grid
    digit=1 #Check to see if the first digit is in the grid
    while digit <= n:
        i= 0
        while i< n:
            row_count=0
            col_count=0
            j=0
            while j < n:
                if list[i][j] == digit:
                    row_count = row_count + 1
                if list[j][i] == digit:
                    col_count = col_count + 1
                j = j+ 1
            if row_count !=1 or col_count != 1:
               return False
            i = i+ 1
        digit = digit + 1
    return True
