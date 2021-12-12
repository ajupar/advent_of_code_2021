
import numpy


def read_input(t: str):
    if t == "test":
        filename = "test_input.txt"
    elif t == "task":
        filename = "Day5_input.txt"

    global input_lines
    with open('Day5/{0}'.format(filename)) as f:
        input_lines = f.readlines()

    global ziplist
    ziplist = list(zip(list(map(lambda line: list(map(lambda coord: int(coord), line.split(" ")[0].split(","))), input_lines)), list(map(lambda line: list(map(lambda coord: int(coord), line.split(" ")[2].rstrip("\n").split(","))), input_lines))))
    print(ziplist)

    global max_dimensions
    max_dimensions = [max(list(numpy.concatenate(list(map(lambda x: [x[0][0], x[1][0]], ziplist))).flat)), max(list(numpy.concatenate(list(map(lambda y: [y[0][1], y[1][1]], ziplist))).flat))]
    print(max_dimensions)


def task1():
    read_input("test")

    dir_lines = list(filter(lambda x: x[0][0] == x[1][0] or x[0][1] == x[1][1], ziplist))
    print(dir_lines)

    task1_matrix = numpy.zeros((max_dimensions[0], max_dimensions[1]), int)
    print(task1_matrix)

    for line in dir_lines:
        if line[0][0] == line[1][0]:
            print(line[0], line[1])
            # line_matrix = numpy.zeros((max_dimensions[0], max_dimensions[1]), int)
            x_dim = [line[0][1], line[1][1]]
            line_matrix = numpy.ones((1, max(x_dim)+1 - min(x_dim)), int)
            # print(y_dim)
            # print([min(y_dim), max(y_dim)+1])
            task1_matrix[line[0][0]][(min(x_dim)):(max(x_dim)+1)] = line_matrix

            # task1_matrix[line[0][0]:line[1][1]][line[0][0]] = 1
        if line[0][1] == line[1][1]:
            print(line[0], line[1])
            y_dim = [line[0][0], line[1][0]]
            print(min(y_dim))
            line_matrix_2 = numpy.ones((1, max(y_dim)+1 - min(y_dim)), int)
            print(line_matrix_2)
            print(task1_matrix[0][3:8])
            print(task1_matrix[(min(y_dim)):(max(y_dim)+1)][(line[0][1])-1])
            task1_matrix[(min(y_dim)):(max(y_dim)+1)][line[0][1]-1] = line_matrix_2


    # task1_matrix[0][1:5] = [3, 5, 4, 7]
    print(task1_matrix.transpose())

def task2():
    pass




