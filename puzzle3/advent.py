import heapq
from functools import lru_cache


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

def makeNumbers(numbers):
    number = 0
    for i, num in enumerate(reversed(numbers)):
        number +=  (int(num) * (10**i))
    return number

# def findLargestNumber(index ,numbers):
#     n = len(numbers)

#     @lru_cache(None)
#     def dp(i, index):
#         if index == 0:
#             return ""
#         if n - i == index:
#             return numbers

#         take = numbers[0] + findLargestNumber(index-1, numbers[1:])

#         skip = findLargestNumber(index, numbers[1:])



#         return max(take, skip) 

def findLargestNumber(index, numbers):
    n = len(numbers)

    @lru_cache(None)
    def dp(i, k):
        # i = current index in s
        # k = digits left to select

        # If we have picked all required digits
        if k == 0:
            return ""

        # If exactly k chars remain, we must take all
        if n - i == k:
            return numbers[i:]

        # Option 1: take s[i]
        take = numbers[i] + dp(i + 1, k - 1)

        # Option 2: skip s[i]
        skip = dp(i + 1, k)

        # Lexicographically largest wins
        return max(take, skip)

    return dp(0, index)


    # largest = heapq.nlargest(2, numbers)
    # maxNum = largest[0]
    # indexes = [i for i, x in enumerate(numbers) if x == maxNum]
    # biggestNumbers = []
    # for i in indexes:
    #     if len(numbers[i+1:]) >= index:
    #         biggestNumbers.append(findLargestNumber(index -1, numbers[i+1:] ))



def day3Second():
    count = 0
    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()

            numbers = [int(num) for num in line]
            maxNum = max(numbers)
            indexMax = numbers.index(maxNum)

            count += int(findLargestNumber(12,line))
            # case 12 max numbers availible 
            # if numbers.count(maxNum) >= 12:
            #     number = 0
            #     for i in range(12):
            #         number +=  (maxNum * (10**i))
            #     count += number
            
            # Is there a max number with 12 numbers behind it
            # So the number starts with this number
            # elif len(numbers[indexMax+1:]) >= 12:
            #     indexes = [i for i, x in enumerate(numbers) if x == maxNum]
            #     for i in indexes:
            #         newNumber = findLargestNumber(11,"",numbers[i+1:])


            # This is the rest of the cases
            # Starts with second largest number
            # else:
            #     largest = heapq.nlargest(2,numbers)
            #     secondIndex = numbers.index(largest[1])
            #     if len(numbers[secondIndex+1:]):
            #         temp = 0
            #     else:
            #         print("test")
            


    return count



if __name__ == "__main__":
    # print(day3())
    print(day3Second())
    # print(makeNumbers([1,2,3,4]))
    # print(max("99123","98", "89"))