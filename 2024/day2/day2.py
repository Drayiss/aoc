def main():
    calculate_part1()

def calculate_part1():
    safe_reports = 0
    with open("input.txt", "r") as file:
        for line in file.readlines():
            words = line.split()
            increasing = False
            decreasing = False
            for i in range(len(words) - 1):
                diff = int(words[i + 1]) - int(words[i])
                if diff > 0:
                    if decreasing: break
                    increasing = True
                if diff < 0:
                    if increasing: break
                    decreasing = True
                if abs(diff) < 1 or abs(diff) > 3:
                    break
                if i == len(words) - 2:
                    safe_reports += 1
    print("Part 1:", safe_reports)

if __name__ == "__main__":
    main()