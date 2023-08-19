"""
Advent of Code 2022 Challenge 1 by pleitner
"""

# read in the input
def get_input(filename):
    """read input"""
    with open(filename, "r") as f:
        return [x.strip("\n") for x in f.readlines()]

def calculate_calories_per_elf(data):
    """sums up all items in list if they are of != """""
    # sum up calories per elf
    elf_calories = list()
    cur_elf = 0
    for item in data:
        if item:
            cur_elf += int(item)
        else:
            elf_calories.append(cur_elf)
            cur_elf = 0
    elf_calories.sort()
    return elf_calories

def sum_top_n(n: int, data):
    """sums up n biggest entries in sorted list data"""
    idx = n * -1
    _sum = 0
    for x in data[idx:]:
        _sum += x
    return _sum


if __name__ == '__main__':
    filename = "input.txt"  # input any file you want
    data = get_input("input.txt")
    elf_calories = calculate_calories_per_elf(data)
    result = elf_calories[-1]
    result_top_3 = sum_top_n(n=3, data=elf_calories)
    print(f"Result part1: {result}")
    print(f"Result part2: {result_top_3}")


