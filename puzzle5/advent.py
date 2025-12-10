
def checkRanges(range, id):
    return range[0] <= id <= range[1]


def amountOfRanges(range):
    return ((range[1]-range[0]) +1)


def day5():
    count = 0
    ranges = set()
    freshId = set()
    ids = []
    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line == "":
                break
            parts = line.split("-")
            ranges.add((int(parts[0]),int(parts[1])))
        for line in f:
            line.strip()
            ids.append(int(line))
    # part 1
    # for id in ids:
    #     for range in ranges:
    #         if checkRanges(range, id):
    #             count += 1
    #             break
    # return count

    # part 2
    for ran in ranges:
        freshId.update(range(ran[0], (ran[1]+1)))
    return len(freshId)
    # return count




if __name__ == "__main__":
    print(day5())