def part1():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        num_lines = len(lines)
        left = [0] * num_lines
        right = [0] * num_lines
        for i in range(num_lines):
            if not lines[i].strip():
                continue
            words = lines[i].split()
            left[i] = int(words[0])
            right[i] = int(words[1])

    merge_sort(left, 0, len(left) - 1)
    merge_sort(right, 0, len(right) - 1)

    total_dist = 0
    for i in range(len(left)):
        total_dist += abs(right[i] - left[i])

    print("Part 1:", total_dist)

def part2():
    with open("input.txt", 'r') as file:
        lines = file.readlines()
        num_lines = len(lines)
        my_dict = {}
        right = [0] * num_lines
        for i in range(num_lines):
            if not lines[i].strip():
                return
            words = lines[i].split()
            num1 = int(words[0])
            num2 = int(words[1])
            my_dict.setdefault(num1, 0)
            right[i] = num2

    for num in right:
        if num in my_dict:
            my_dict[num] += num

    similarity_score = 0
    for value in my_dict.values():
        similarity_score += value

    print("Part 2:", similarity_score)


def merge_sort(arr, s, e):
    length = e - s + 1
    if length <= 1:
        return
    m = s + (e - s) // 2

    merge_sort(arr, s, m)
    merge_sort(arr, m + 1, e)

    merge(arr, s, m, e)

def merge(arr, s, m, e):
    left_len = (m + 1) - s
    right_len = (e + 1) - (m + 1)

    left_arr = [0] * left_len
    right_arr = [0] * right_len

    for i in range(left_len):
        left_arr[i] = arr[i + s]
    for i in range(right_len):
        right_arr[i] = arr[i + (m + 1)]

    i = 0
    j = 0
    k = s

    while i < left_len and j < right_len:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1

if __name__ == "__main__":
    part1()
    part2()