
# For the first half
def checkDouble(num):
    length = len(str(num))
    if length % 2 != 0:
        return False
    else:
        string = str(num)
        if string[:(length//2)] == string[(length//2):]:
            return True
        else:
            return False


# Second half
def checkMultiple(num):
    length = len(str(num))
    string = str(num)
    size = 1
    waar = False
    while size != ((length//2)+1):
        stukje = string[:size]
        temp = size
        while temp != length:
            if stukje == string[temp:temp+size]:
                temp += size
                if temp == length:
                    waar = True
            else:
                break
        if waar:
            return True
        
        size += 1
    return False




def day2():
    sum = 0
    with open("input.txt", "r") as f:
        for line in f:
            line = line.split(sep=",")
            for range in line:
                range = range.split(sep="-")
                bottom = int(range[0])
                top = int(range[1])
                while bottom != top:
                    if checkMultiple(bottom):
                        sum += bottom
                    bottom += 1
    return sum



if __name__ == "__main__":
    print(day2())
    # print(checkDouble(1213))
    # print(checkMultiple(824824824))