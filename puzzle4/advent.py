# Checks which rolls to remove
def countRolls(world, length):
    count = 0
    removeRolls = []
    for i, char in enumerate(world):
        if char == "@":
            localCount = 0
                
            if i > length-1:
                
                if i % length != 0:
                    if world[i-(length+1)] == "@":
                        localCount += 1
                
                if world[i-(length)] == "@":
                    localCount += 1

                if i % length != (length-1):
                    if world[i-(length-1)] == "@":
                        localCount += 1
            
            
            if i % length != 0:
                if world[i-1] == "@":
                    localCount += 1
            

            if i % length != (length-1):
                if world[i+1] == "@":
                    localCount += 1
            
            if i < length*138:    

                if i % length != (length-1):
                    if world[i+length+1] == "@":
                        localCount += 1

                if world[i+(length)] == "@":
                    localCount +=1

                if i % length != 0:
                    if world[i+(length-1)] == "@":
                        localCount += 1


            
            # less then 4
            if localCount < 4:
                count += 1
                removeRolls.append(i)
    return count, removeRolls
            

# Removes the removed rolls from string
def remove(removeRolls, world):
    for i in removeRolls:
        world = world[:i] + "." + world[i+1:]
    return world




# Main function
def day4():
    world = ""
    totalCount = 0
    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            length = len(line)
            world += line
        
    count, removeRolls = countRolls(world, length)
    totalCount += count

    while removeRolls:
        world = remove(removeRolls, world)
        count, removeRolls = countRolls(world, length)
        totalCount += count
    return totalCount




if __name__ == "__main__":
    print(day4())
