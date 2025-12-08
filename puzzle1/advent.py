# First half
def day1first():
    dial = 50
    count = 0
    with open("input.txt", "r") as f:
        for line in f:
            # print(line)
            if line[0] == "L":
                dial = (dial - int(line[1:])) % 100
            else:
                dial = (dial + int(line[1:])) % 100
            if dial == 0:
                count += 1
    return count


#second half
def day1second():
    dial = 50
    count = 0
    with open("input.txt", "r") as f:
        for line in f:
            # print(line)
            if line[0] == "L":
                # if (dial - int(line[1:])) < 0:
                #     count += 1
                count += -((dial - int(line[1:])))//100
                dial = (dial - int(line[1:])) % 100

            else:
                count += (dial + int(line[1:]))//100
                dial = (dial + int(line[1:])) % 100

            # if dial == 0:
                # count += 1
    return count
    





if __name__ == "__main__":
    # print(-128 // 100)
    print(day1second())
