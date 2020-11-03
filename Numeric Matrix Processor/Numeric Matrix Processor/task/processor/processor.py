class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.value = []

    def fill_matrix(self):
        new_value = [input().split() for _ in range(self.rows)]
        try:
            assert all(len(x) == self.columns for x in new_value)
        except AssertionError:
            print('Input dimension not matching')
        else:
            self.value = new_value

    def print_matrix(self):
        if self.value:
            for i in range(self.rows):
                print(' '.join(self.value[i]))

    def matrix_addition(self, matrix):
        new_matrix = Matrix(self.rows, self.columns)

        try:
            assert self.rows == matrix.rows
            assert self.columns == matrix.columns
        except AssertionError:
            print("The operation can not be performed\n")
        else:
            result = []
            for i in range(new_matrix.rows):
                result_row = []
                for j in range(new_matrix.columns):
                    new_element = float(self.value[i][j]) + float(matrix.value[i][j])
                    result_row.append(f"{new_element}")
                result.append(result_row)

            new_matrix.value = result

        return new_matrix

    def scalar_multiplication(self, scalar):
        new_matrix = Matrix(self.rows, self.columns)
        result = []
        for i in range(new_matrix.rows):
            result_row = []
            for j in range(new_matrix.columns):
                new_element = float(self.value[i][j]) * scalar
                result_row.append(f"{new_element}")
            result.append(result_row)

        new_matrix.value = result

        return new_matrix

    def matrix_multiplication(self, matrix):
        new_matrix = Matrix(self.rows, matrix.columns)

        try:
            assert self.columns == matrix.rows
        except AssertionError:
            print("The operation can not be performed")
        else:
            result = []
            for i in range(new_matrix.rows):
                result_row = []
                for j in range(new_matrix.columns):
                    row_a = self.value[i]
                    column_b = [matrix.value[x][j] for x in range(len(matrix.value))]
                    new_element = sum(map(lambda x, y: float(x) * float(y), row_a, column_b))
                    result_row.append(f"{new_element}")
                result.append(result_row)

            new_matrix.value = result

        return new_matrix

    def transpose(self, trans_type='main'):
        if trans_type == 'main':
            new_matrix = Matrix(self.columns, self.rows)
            new_matrix.value = [[self.value[i][j] for i in range(self.rows)]
                                for j in range(self.columns)]
            return new_matrix
        elif trans_type == 'side':
            new_matrix = Matrix(self.columns, self.rows)
            new_matrix.value = [[self.value[i][j] for i in range(self.rows - 1, -1, -1)]
                                for j in range(self.columns - 1, -1, -1)]
            return new_matrix
        elif trans_type == 'vertical':
            new_matrix = Matrix(self.rows, self.columns)
            new_matrix.value = [[self.value[i][j] for j in range(self.columns - 1, -1, -1)]
                                for i in range(self.rows)]
            return new_matrix
        elif trans_type == 'horizontal':
            new_matrix = Matrix(self.rows, self.columns)
            new_matrix.value = [self.value[i] for i in range(self.rows - 1, -1, -1)]
            return new_matrix

    def determinant(self, sub_mat=None):
        if sub_mat is None:
            try:
                assert self.rows == self.columns
            except AssertionError:
                print("Must be quadratic")
            else:
                if self.rows == 1:
                    return self.value[0][0]
                elif self.rows == 2:
                    return float(self.value[0][0]) * float(self.value[1][1])\
                           - float(self.value[0][1]) * float(self.value[1][0])
                else:
                    sub_matrices = [[[float(self.value[i][j]) for j in range(self.columns) if j != k]
                                     for i in range(self.rows - 1)]
                                    for k in range(self.columns)]
                    minors = [self.determinant(sub_mat=sub_mat) for sub_mat in sub_matrices]
                    cofactors = [(-1) ** (self.rows + j + 1) * minors[j] for j in range(self.columns)]

                    return sum([cofactors[j] * float(self.value[self.rows - 1][j]) for j in range(self.columns)])

        else:
            if len(sub_mat) == 2:
                return float(sub_mat[0][0]) * float(sub_mat[1][1])\
                       - float(sub_mat[0][1]) * float(sub_mat[1][0])

            sub_matrices = [[[sub_mat[i][j] for j in range(len(sub_mat)) if j != k]
                             for i in range(len(sub_mat) - 1)]
                            for k in range(len(sub_mat))]
            minors = [self.determinant(sub_mat=mat) for mat in sub_matrices]
            cofactors = [(-1) ** (len(sub_mat) + j + 1) * minors[j] for j in range(len(sub_mat))]

            return sum([cofactors[j] * float(sub_mat[len(sub_mat) - 1][j])
                        for j in range(len(sub_mat))])

    def inverse(self):
        new_matrix = Matrix(self.rows, self.columns)

        try:
            return self.cofactors().transpose().scalar_multiplication(1 / self.determinant())
        except ZeroDivisionError:
            print("This matrix does not have an inverse.")

        return new_matrix

    def cofactors(self):
        new_matrix = Matrix(self.rows, self.columns)
        new_matrix.value = [[0 for _ in range(new_matrix.columns)] for _ in range(new_matrix.rows)]

        for i in range(self.rows):
            for j in range(self.columns):
                minor = Matrix(self.rows - 1, self.columns - 1)
                minor.value = [[self.value[n][m] for m in range(self.columns) if m !=j]
                               for n in range(self.rows) if n != i]
                new_matrix.value[i][j] = str((-1) ** (i + j + 2) * minor.determinant())

        return new_matrix


class Calculator:
    MENU = "1. Add matrices\n" \
           "2. Multiply matrix by a constant\n" \
           "3. Multiply matrices\n"\
           "4. Transpose matrix\n"\
           "5. Calculate a determinant\n"\
           "6. Inverse Matrix\n"\
           "0. Exit"

    T_MENU = "1. Main diagonal\n" \
             "2. Side diagonal\n" \
             "3. Vertical line\n" \
             "4. Horizontal line\n" \
             "0. Back"

    def __init__(self):
        self.actions = {'1': self.matrix_addition,
                        '2': self.scalar_multiplication,
                        '3': self.matrix_multiplication,
                        '5': self.determinant,
                        '6': self.inverse}

        self.transpositions = {'1': 'main',
                               '2': 'side',
                               '3': 'vertical',
                               '4': 'horizontal'}

    def start(self):
        while True:
            print(self.MENU)
            if choice := input("Your choice: "):
                if choice == '0':
                    break
                elif choice == '4':
                    self.transpose_menu()
                else:
                    try:
                        self.actions[choice]()
                    except TypeError:
                        print("Incomplete dimension")
                    except ValueError:
                        print("Please enter numbers")
                    except KeyError:
                        print("Invalid option")

    def transpose_menu(self):
        print(self.T_MENU)
        while True:
            if choice := input("Your choice: "):
                if choice == '0':
                    break
                else:
                    try:
                        self.transpose(self.transpositions[choice])
                    except KeyError:
                        print('No such option')
                    else:
                        break

    @staticmethod
    def matrix_addition():
        dim = map(int, input("Enter size of first matrix: ").split())
        a = Matrix(*dim)
        print("Enter first matrix: ")
        a.fill_matrix()
        dim = map(int, input("Enter size of second matrix: ").split())
        b = Matrix(*dim)
        print("Enter second matrix: ")
        b.fill_matrix()
        c = a.matrix_addition(b)
        if c.value:
            print("The result is: ")
            c.print_matrix()

    @staticmethod
    def scalar_multiplication():
        dim = map(int, input("Enter size of matrix: ").split())
        a = Matrix(*dim)
        print("Enter matrix: ")
        a.fill_matrix()
        scalar = float(input("Enter constant: "))
        b = a.scalar_multiplication(scalar)
        if b.value:
            print("The result is: ")
            b.print_matrix()

    @staticmethod
    def matrix_multiplication():
        dim = map(int, input("Enter size of first matrix: ").split())
        a = Matrix(*dim)
        print("Enter first matrix: ")
        a.fill_matrix()
        dim = map(int, input("Enter size of second matrix: ").split())
        b = Matrix(*dim)
        print("Enter second matrix: ")
        b.fill_matrix()
        c = a.matrix_multiplication(b)
        if c.value:
            print("The result is: ")
            c.print_matrix()

    @staticmethod
    def transpose(trans_type):
        dim = map(int, input("Enter size of matrix: ").split())
        a = Matrix(*dim)
        print("Enter matrix: ")
        a.fill_matrix()
        b = a.transpose(trans_type=trans_type)
        if b.value:
            print("The result is: ")
            b.print_matrix()

    @staticmethod
    def determinant():
        dim = map(int, input("Enter size of matrix: ").split())
        a = Matrix(*dim)
        print("Enter matrix: ")
        a.fill_matrix()
        b = a.determinant()
        if b:
            print("The result is: ")
            print(b)

    @staticmethod
    def inverse():
        dim = map(int, input("Enter size of matrix: ").split())
        a = Matrix(*dim)
        print("Enter matrix: ")
        a.fill_matrix()
        b = a.inverse()
        if b:
            print("The result is: ")
            b.print_matrix()


if __name__ == '__main__':
    calc = Calculator()
    calc.start()
