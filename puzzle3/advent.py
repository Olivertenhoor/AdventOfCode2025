import heapq


def day3():
    count = 0
    with open("input.txt", "r") as f:
        
        for line in f:
            line = line.strip()
            numbers = [int(num) for num in line]
            maxNum = max(numbers)
            if numbers.count(maxNum) >= 2:
                count += (maxNum*10) + maxNum
            else:
                indexMax = numbers.index(maxNum)
                if numbers[indexMax+1:]:
                    maxNumSub = max(numbers[indexMax+1:])
                    count += (maxNum * 10) + maxNumSub
                else:
                    largest = heapq.nlargest(2,line)
                    biggest = int(largest[0])
                    second = int(largest[1])
                    
                    count += (second * 10) + biggest

    return count





if __name__ == "__main__":
    print(day3())