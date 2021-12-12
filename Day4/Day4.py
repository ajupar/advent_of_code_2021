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
        Palauttaa sisällön iteroitavassa muodossa
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


    def checkRowsColumns(self) -> bool:
        """
        Kertoo, onko jokin bingotaulun rivi tai sarake täysi
        :return: rivi tai sarake täysi (bool)
        """

        for count, row in enumerate(self.content):
            if all(x.called for x in row):
                return True
            if all(row2[count].called for row2 in self.content):
                return True

        return False


class BingoNum:
    def __init__(self, num_in):
        self.num = num_in

    def __str__(self):
        return self.num

    called = False


boards = []


def readInput():

    with open('Day4/Day4_input.txt') as f:
        input_lines = f.readlines()

    print(input_lines)


    global nums_to_call
    nums_to_call = input_lines[0].split(',')
    nums_to_call[-1] = nums_to_call[-1].rstrip("\n")

    #input_lines.append("\n")  # lukumetodi olettaa, että viimeisenä tyhjä rivi

    for count, num in enumerate(nums_to_call):
        nums_to_call[count] = int(num)

    board_input = input_lines[1:]
    print("board input", board_input)

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

    # board: BingoBoard
    # for board in boards:
    #     board.callNum(22)
    #     board.callNum(5)
    #     board.callNum(23)
    #     board.callNum(4)
    #     board.callNum(6)

    # print("boards[1].content[1][2].called", boards[1].content[1][2].called)
    # print("boards[1].content[1] (second row) called)", boards[1].content[1][0].called, boards[1].content[1][1].called, boards[1].content[1][2].called, boards[1].content[1][3].called, boards[1].content[1][4].called)
    # print("boards[1].checkRowsColumns", boards[1].checkRowsColumns())  # metodi ei toimi vielä


def callNums():

    board_won = False

    board: BingoBoard

    global current_called_num

    for num_call_count, current_called_num in enumerate(nums_to_call):
        for board in boards:
            board.callNum(current_called_num)

        for board in boards:
            if board.checkRowsColumns():
                board_won = True
                winning_board = board
                break

        if board_won:
            calculate_winning_score(winning_board)
            break


def calculate_winning_score(winning_board: BingoBoard):
    win_sum = 0

    for count, row in enumerate(winning_board.content):
        for bnum in row:
            if not bnum.called:
                win_sum += bnum.num

    print("uncalled nums sum:", win_sum)
    print("current_called_num:", current_called_num)
    print("product:", win_sum * current_called_num)


def task1():

    print("task1")
    readInput()

    callNums()





def task2():
    print("task2")
