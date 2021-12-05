from typing import List, Any


class BingoBoard:
    def __init__(self, dim_x_in, dim_y_in, content_in):
        print("bingoboard constructor content_in", content_in)
        self.dim_x = dim_x_in
        self.dim_y = dim_y_in
        self.content = self.parseInput(content_in)  # assignment pitää tehdä tässä eli ei voi ajaa metodia jonka sisällä kutsutaan this.content = ...

        print(self, "my content is", self.content)

    won = False
    content = []

    def getContentAsNum(self, just_nums):
        ret = []
        for i in range(0, len(self.content)):
            temp_ret = []
            for j in range(0, len(self.content[i])):
                temp_ret.append(self.content[i][j].num) if just_nums == True else temp_ret.append(self.content[i][j])
            ret.append(temp_ret)
        return ret

    def getIterableContent(self, just_nums):
        """
        :type just_nums: bool
        """
        it = []
        for i in range(0, len(self.content)):
            for j in range(0, len(self.content[i])):
                it.append(self.content[i][j].num) if just_nums == True else it.append(self.content[i][j])

        return it


    def parseInput(self, content_in):
        cont = []

        print("bingoboard setContent content_in", content_in)
        test = [i for i in content_in[0].split(" ") if len(i) > 0]
        test[-1] = test[-1].rstrip("\n")

        print("bingoboard setContent content_in[0]", test)

        i = 0
        while i < len(content_in):
            while i == 0 or i % self.dim_x != 0:
                # https://note.nkmk.me/en/python-list-clear-pop-remove-del/
                temp_row = [j for j in content_in[i].split(" ") if len(j) > 0]
                temp_row[-1] = temp_row[-1].rstrip("\n")
                print("temp row", temp_row)
                bn_row = [BingoNum(int(k)) for k in temp_row]  # huom tyyppimuunnos tässä, BingoNumille string --> int
                cont.append(bn_row)
                i += 1

        return cont

    def callNum(self, num_in):
        # print("callNum with num", num_in)
        for i in range(0, len(self.content)):
            for j in range(0, len(self.content[i])):
                if self.content[i][j].num == num_in:
                    # print("Hit at index", i, j)
                    self.content[i][j].called = True


    def checkRowsColumns(self):
        for i in range(0, self.dim_x):
            full_row = all(bn.called for bn in self.content[i])
            full_column = all(bn.called for bn in list(map(lambda x: x[i], self.content)))
            if full_row or full_column:
                return True
        return False


class BingoNum:
    def __init__(self, num_in):
        self.num = num_in

    def __str__(self):
        return self.num

    called = False


def readInput():

    with open('Day4/test_input.txt') as f:
        input_lines = f.readlines()

    print(input_lines)

    nums_to_call = input_lines[0].split(',')
    nums_to_call[-1] = nums_to_call[-1].rstrip("\n")
    print(nums_to_call)

    board_input = input_lines[1:-1]
    print("board input", board_input)

    boards = []

    i = 0
    while i < len(board_input):
        if(board_input[i] == "\n"):
            i += 1
        else:
            new_board_content = board_input[i:i+5]
            print("appending", new_board_content)
            new_board = BingoBoard(5, 5, new_board_content)
            boards.append(new_board)
            i += 5


    print(boards)
    print("boards length", len(boards))
    print("boards[0] content", boards[0].getContentAsNum(True))
    print("boards[1] content", boards[1].getContentAsNum(True))
    print("boards[2] content", boards[2].getContentAsNum(True))

    print("boards[0] checkRowsColumns", boards[0].checkRowsColumns())
    print("boards[0] getIterableContent", boards[0].getIterableContent(True))

    bn = BingoNum(3)
    print("bn num", bn.num)

    for board in boards:
       board.callNum(9)
       board.callNum(18)
       board.callNum(13)
       board.callNum(17)
       board.callNum(15)

    print("boards[1].content[1][2].called", boards[1].content[1][2].called)
    print("boards[1].checkRowsColumns", boards[1].checkRowsColumns())  # metodi ei toimi vielä

def task1():
    print("task1")
    readInput()



def task2():
    print("task2")
