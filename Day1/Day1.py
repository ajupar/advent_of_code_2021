

# https://adventofcode.com/2021/day/1
# https://www.pythontutorial.net/python-basics/python-read-text-file/
def task1():
    with open('Day1/aoc_day1_task1_input.txt') as f:
        inputlines = f.readlines()

    previousline = None
    currentline = None
    biggercount = 0
    linecount = 0

    for line in inputlines:
        previousline = currentline
        currentline = int(line)
        linecount += 1

        try:
            if currentline > previousline:
                biggercount += 1

        except TypeError:
            print("except block: first comparison")

    print("Total number of lines: " + str(linecount))
    print("Count of larger measurements: " + str(biggercount))



# https://adventofcode.com/2021/day/1#part2
def task2():
    sw_sums = []

    inputlines = []
    with open('Day1/aoc_day1_task1_input.txt') as f:
        inputlines = f.readlines()

    for iterationCount in range(0, len(inputlines)-2):  # yläraja ei inklusiivinen joten vikan ikkunan laskeminen aloitetaan indeksistä -3
        currentSum = sum(list(map(int, inputlines[iterationCount:iterationCount+3])))
        sw_sums.append(currentSum)

    sums_count = 1 # vertailu ei laske ekaa alkiota
    count_greater_than = 0

    for j in range(1, len(sw_sums)):
        sums_count += 1
        if sw_sums[j] > sw_sums[j-1]:
            count_greater_than += 1

    print("Total count of lines: " + str(len(inputlines)))
    print("Total count of sums: " + str(sums_count))
    print("Sums greater than previous: " + str(count_greater_than))


