

def task1():

    with open('Day2/Day2_input.txt') as f:
        input_lines = f.readlines()

    pos = [0, 0]

    for line in input_lines:
        s = line.split(" ")
        if s[0] == "forward":
            pos[0] = pos[0] + int(s[1])

        elif s[0] == "up":
            pos[1] = pos[1] - int(s[1])

        elif s[0] == "down":
            pos[1] = pos[1] + int(s[1])

    print("Final horizontal position: " + str(pos[0]))
    print("Final depth: " + str(pos[1]))
    print("Final depth * final horizontal position:", pos[0] * pos[1])


def task2():
    pos = [0, 0]
    aim = 0

    with open('Day2/Day2_input.txt') as f:
        input_lines = f.readlines()

    for line in input_lines:
        s = line.split(" ")
        if s[0] == "forward":
            pos = [pos[0] + int(s[1]), pos[1] + aim*int(s[1])]

        elif s[0] == "up":
            aim = aim - int(s[1])

        elif s[0] == "down":
            aim = aim + int(s[1])


    print("Final horizontal position:", pos[0])
    print("Final depth:", pos[1])
    print("Final depth * final horizontal position:", pos[0] * pos[1])