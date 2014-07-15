def is_identity_matrix(matrix):
    '''
     A list of lists representing a n * n matrix as input.
     A  procedure that returns True if the input is an identity matrix 
     and False otherwise.

     An IDENTITY matrix is a square matrix in which all the elements 
     on the principal/main diagonal are 1 and all the elements outside 
     the principal diagonal are 0.

      (A square matrix is a matrix in which the number of rows 
      is equal to the number of columns)

    '''


    matrix_len = len(matrix[0])

    if len(matrix) == 1 or len(matrix) == 0:
        return False
    else:

        for x in xrange(matrix_len):
            zero_count = 0

            # check the position of each matrix and to check it its a identity matrix
            for y in xrange(matrix_len):

                # first if statement checks if the matrix is an identity
                # by using the variable pos_x and pos_y to check the
                # vector positon of the matrix in order to determine
                # if 1 is within the right position
                if matrix[x][x] != 1:
                    return False
                else:

                    # check the rest of the rows for the zeroes
                    if matrix[x][y] == 0:
                        zero_count += 1


            # checks it the number of 0 is equal to len of the list - 1
            # if so the next position vectors are incremented
            if zero_count != (matrix_len - 1):
                return False

        return True
