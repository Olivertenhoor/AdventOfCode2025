
def checkRanges(range, id):
    return range[0] <= id <= range[1]


def amountOfRanges(range):
    return ((range[1]-range[0]) +1)


# NOT USED
def checkIfDouble(range, ranges):
    
    for ran in ranges:
        # range falls within another range
        if range[0] >= ran[0] and range[1] <= ran[1]:
            # print(range[1], ran[1])
            print("new range obsolete")
            return ranges

        # other way around
        if ran[0] >= range[0] and ran[1] <= range[1]:
            ranges.remove(ran)
            ranges.add(range)
            print("old range obsolete")
            return ranges
        #range has lower bottom
        if range[0] < ran[0] and ran[0] <= range[1] <= ran[1]:
            newRange = (range[0], ran[1])
            ranges.remove(ran)
            ranges.add(newRange)
            print("lower bottom")
            return ranges
        # Range has higher max
        if ran[1] >= range[0] >= ran[0] and range[1] > ran[1]:
            newRange = (ran[0], range[1])
            ranges.remove(ran)
            ranges.add(newRange)
            print("higher max")
            return ranges
    print("add new")
    ranges.add(range)
    return ranges


def day5():
    count = 0
    ranges = []
    freshId = set()
    ids = []
    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line == "":
                break
            parts = line.split("-")
            ranges.append((int(parts[0]),int(parts[1])))
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
    # Idea, update ranges so there are no doubles allowed.
    updatedRanges = set()
    # print(ranges)

    ranges.sort(key=lambda r: r[0])

    merged = []
    for start, end in ranges:
        if not merged:
            merged.append([start, end])
        else:
            last_start, last_end = merged[-1]

            if start <= last_end + 1:
                merged[-1][1] = max(last_end, end)
            else:
                merged.append([start, end])

    for ran in merged:
        count += amountOfRanges(ran)
    return count

    for ran in ranges:
        print(ran)
        if  not updatedRanges:
            print("empty")
            updatedRanges.add(ran)
        # print(ran)
        else:
            updatedRanges = checkIfDouble(ran, updatedRanges)


    return count
    
    return updatedRanges
    # return count




if __name__ == "__main__":
    print(day5())