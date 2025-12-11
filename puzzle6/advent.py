def day6():
    count = 0
    # problems = [][]
    grid = [[0, 0, 0, 0, 0] for _ in range(1000)]
    
    depth = 0
    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            parts = line.split()
            for i in range(len(parts)):
                grid[i][depth] = parts[i]
            depth+=1
    for i in range(1000):
        if grid[i][4] == "*":
            count += (int(grid[i][0]) * int(grid[i][1]) * int(grid[i][2]) * int(grid[i][3]))
        elif grid[i][4] == "+":
            count += (int(grid[i][0]) + int(grid[i][1]) + int(grid[i][2]) + int(grid[i][3]))
    return count
            

if __name__ == "__main__":
    print(day6())