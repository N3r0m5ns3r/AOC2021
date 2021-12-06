def increasing(data):
    increase = 0

    for z in range(1, len(data)):
        if data[z] > data[z - 1]:
            increase += 1

    print("Problem 1 answer: " + str(increase))


def sliding(data):
    increase = 0

    for y in range(2, len(data) - 1):
        if (data[y - 2] + data[y - 1] + data[y]) < (
                data[y - 1] + data[y] + data[y + 1]):
            increase += 1

    print("Problem 2 answer: " + str(increase))


if __name__ == '__main__':
    with open("./Inputdata.txt") as file:
        result = [int(line.strip()) for line in file]
    increasing(result)
    sliding(result)
