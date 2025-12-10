# First half
def day1first():
    dial = 50
    count = 0
    with open("input.txt", "r") as f:
        for line in f:
            number = int(line[1:0])
            if line[0] == "L":
                dial = (dial - number) % 100
            else:
                dial = (dial + number) % 100
            if dial == 0:
                count += 1
    return count


#second half
def day1second():
    dial = 50
    count = 0
    with open("input2.txt", "r") as f:
        for line in f:
            number = int(line[1:])
            if line[0] == "L":
                for _ in range(number):
                    dial = (dial -1 ) % 100
                    if dial == 0:
                        count += 1
            else:
                for _ in range(number):
                    dial =( dial +1) % 100
                    if dial == 0:
                        count += 1

            #Got frustratd with trying an elegant way
            
            # if line[0] == "L":
                
            #     count += abs((dial - number) // 100)
            #     if dial == 0 and number > 100:
            #         count -= 1
            #     dial = (dial + number) % 100
            #     if dial == 0 and number < 100:
            #         count += 1
                
            # else:
            #     count += (dial + number) // 100
            #     dial = (dial + number) % 100

        return count
    





if __name__ == "__main__":
    # print(20%100)
    print(day1second())
