class Matrix:
    def __init__(self, rows, cols):
        self.matrix = []
        self.rows = rows
        self.cols = cols

    def generate_matrix(self):
        num = 1
        if self.rows == 0 and self.cols == 0:
            return
        for row in range(self.rows):#change i ->row
            self.matrix.append([])
            for col in range(self.cols):#change j->col
                self.matrix[row].append(num)
                num += 1

    def print_matrix(self):#change name from print to print_matrix
        for row in self.matrix:
            print("\t".join(map(str, row)))
        print("-----------------")

    def find_coordinate(self, value):
        for row_index in range(self.rows):#change r to row_index
            if value in self.matrix[row_index]:
                col_index = self.matrix[row_index].index(value)#changed c to col_index
                return {'x': row_index, 'y': col_index}
        return None

    def get_value(self, row_num, col_num): #rename func get->get_value
        return self.matrix[row_num][col_num]

    def print_row(self, row_num):
        for column_value in self.matrix[row_num]:#change c->column_value
            print(column_value)

    def alter(self, row_num, col_num, new_value):
        self.matrix[row_num][col_num] = new_value


