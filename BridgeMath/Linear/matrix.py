class Matrix:
    """
    Defines an N by N sized matrix
    """
    def __init__(self, num_rows: int, num_columns: int):
        if num_rows <= 0:
            raise ValueError('One or more rows required to define matrix')
        if num_columns <= 0:
            raise ValueError('One or more columns required to define matrix')

        self.__row_count = num_rows
        self.__column_count = num_columns

        self.__data = [0] * (num_rows * num_columns)

    @property
    def column_count(self) -> int:
        """
        Number of columns defined in matrix
        """
        return self.__column_count

    @property
    def is_square(self) -> bool:
        """
        Checks if number of rows equals the number of columns
        """
        return self.__row_count == self.__column_count

    @property
    def row_count(self) -> int:
        """
        Number of rows defined in matrix
        """
        return self.__row_count

    def scale(self, factor: float) -> 'Matrix':
        """
        Multiply all matrix elements by a given factor
        """
        mat = Matrix(self.row_count, self.column_count)
        for row_index in range(mat.row_count):
            for column_index in range(mat.column_count):
                mat.set_value(row_index, column_index, factor * self.value_at(row_index, column_index))

        return mat

    def set_value(self, row_index: int, column_index: int, value):
        """
        Sets a value in the matrix at the given row/column address
        :param row_index: Row index
        :param column_index: Column index
        :param value: Value to assign to matrix address
        """
        self.__data[self.__get_index(row_index, column_index)] = value

    def transposed(self) -> 'Matrix':
        """
        Returns transposed matrix
        """
        mat = Matrix(self.column_count, self.row_count)
        for row_index in range(mat.row_count):
            for column_index in range(mat.column_count):
                mat.set_value(row_index, column_index, self.value_at(column_index, row_index))

        return mat

    def value_at(self, row_index: int, column_index: int):
        """
        Returns the value at the given row/column address
        :param row_index: Row index
        :param column_index: Column index
        :return: Value store in Matrix
        """
        return self.__data[self.__get_index(row_index, column_index)]

    def value_at_transposed(self, row_index: int, column_index: int):
        """
        Returns the value at the index as if the matrix is transposed
        """
        return self.value_at(column_index, row_index)

    def __get_index(self, row_index: int, column_index: int):
        """
        Retrieve the one-dimensional array index of the row/column matrix address.
        The array stores the data in row-major form.
        """
        return row_index * self.__column_count + column_index

    def __add__(self, other: 'Matrix') -> 'Matrix':
        """
        Adds two matrices. Matrices must be the same size.
        """
        if self.row_count != other.row_count or self.column_count != other.column_count:
            raise ValueError('Matrices must be the same size for addition')

        mat = Matrix(self.__row_count, self.__column_count)

        for i in range(len(self.__data)):
            mat.__data[i] = self.__data[i] + other.__data[i]

        return mat

    def __sub__(self, other: 'Matrix') -> 'Matrix':
        """
        Subtracts two matrices. Matrices must be the same size.
        """
        if self.row_count != other.row_count or self.column_count != other.column_count:
            raise ValueError('Matrices must be the same size for subtraction')

        mat = Matrix(self.__row_count, self.__column_count)

        for i in range(len(self.__data)):
            mat.__data[i] = self.__data[i] - other.__data[i]

        return mat

    def __mul__(self, other: 'Matrix') -> 'Matrix':
        """
        Multiplies two matrices. The column size in the left matrix must match the row size in the right matrix.
        """
        if self.column_count != other.row_count:
            raise ValueError('Matrices are not compatible for multiplication')

        mat = Matrix(self.row_count, other.column_count)
        for row_index in range(self.row_count):
            for column_index in range(other.column_count):
                _sum = 0
                for k in range(self.column_count):
                    _sum += self.value_at(row_index, k) * other.value_at(k, column_index)
                mat.set_value(row_index, column_index, _sum)

        return mat

    def __eq__(self, other):
        if self is other:
            return True

        if not isinstance(other, Matrix):
            return False

        if not self.row_count == other.row_count or not self.column_count == other.column_count:
            return False

        if not self.__data == other.__data:
            return False
        else:
            return True
