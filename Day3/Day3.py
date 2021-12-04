from statistics import mode


# https://www.geeksforgeeks.org/binary-decimal-vice-versa-python/
def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1

    return(decimal)


def task1():
    most_common_binaries = []
    least_common_binaries = []

    with open('Day3/Day3_input.txt') as f:
        input_lines = f.readlines()

    for i in range(0, len(input_lines[0])-1):  # viimeinen iteroitava indeksissä 11 eli ylärajaksi 12
        count_list = []
        for j in range(0, len(input_lines)):
            l = input_lines[j]

            count_list.append(l[i])

        most_common_binaries.append(int(mode(count_list)))
        least_common_binaries.append(abs(int(mode(count_list))-1))  # käännetty binääri

    mc = ''.join(map(str, most_common_binaries))
    print("Gamma rate in binary:", mc)
    mc_int = int(mc)

    lc = ''.join(map(str, least_common_binaries))
    print("Epsilon rate in binary:", lc)
    lc_int = int(lc)

    mc_dec = binaryToDecimal(mc_int)
    lc_dec = binaryToDecimal(lc_int)
    print("Gamma rate in decimal:", mc_dec)
    print("Epsilon rate in decimal:", lc_dec)
    print("Power consumption:", mc_dec*lc_dec)


def task2():
    with open('Day3/Day3_input.txt') as f:
        input_lines = f.readlines()

    # matriisimuotoon helpompaa käsittelyä varten
    for i in range(0, len(input_lines)):
        input_lines[i] = [int(x) for x in input_lines[i].rstrip("\n")]

    # modes = []
    anti_modes = []

    print(list(map(lambda x: x[4], input_lines)))

    # https://betterprogramming.pub/lambda-map-and-filter-in-python-4935f248593
    # for k in range(0, len(input_lines[0])):
    #     modes.append(binary_mode(list(map(lambda x: x[k], input_lines))))
        # anti_modes.append(binary_mode(list(map(lambda x: abs(x[k]-1), input_lines))))

    # anti_modes = list(map(lambda x: abs(x-1), modes))
    # print(modes)
    # print(anti_modes)

    possible_oxygen = input_lines
    iteration_count = 0

    # https://betterprogramming.pub/lambda-map-and-filter-in-python-4935f248593
    while len(possible_oxygen) > 1:
        current_pos = list(map(lambda x: x[iteration_count], possible_oxygen))
        possible_oxygen = list(filter(lambda x: x[iteration_count] == binary_mode(current_pos), possible_oxygen))
        # print(possible_oxygen)
        iteration_count += 1

    oxygen_rating = ''.join(map(str, possible_oxygen[0][0:len(possible_oxygen[0])]))
    oxygen_rating_dec = binaryToDecimal(int(oxygen_rating))

    possible_co2 = input_lines
    iteration_count = 0

    while len(possible_co2) > 1:
        current_pos = list(map(lambda x: x[iteration_count], possible_co2))
        possible_co2 = list(filter(lambda x: x[iteration_count] == abs(binary_mode(current_pos)-1), possible_co2))
        # print(possible_co2)
        iteration_count += 1

    co2_rating = ''.join(map(str, possible_co2[0][0:len(possible_co2[0])]))
    co2_rating_dec = binaryToDecimal(int(co2_rating))

    # print("Modes:", modes)
    # print("Antimodes:", anti_modes)
    print("Oxygen rating bin:", oxygen_rating)
    print("CO2 rating bin:", co2_rating)
    print("Oxygen rating:", oxygen_rating_dec)
    print("CO2 rating:", co2_rating_dec)

    print("Life support rating:", oxygen_rating_dec * co2_rating_dec)



def binary_mode(input_list):
    ''' Palauttaa binääriluvun moodin. Jos yhtä monta, palautetaan 1. '''
    count_0 = 0
    count_1 = 0

    for i in range(0, len(input_list)):
        if input_list[i] == 0:
            count_0 += 1
        elif input_list[i] == 1:
            count_1 += 1

    if count_0 > count_1:
        return 0
    elif count_0 < count_1:
        return 1
    elif count_0 == count_1:
        return 1



