
    
def main(filename):
    task_pairs = read_input(filename)
    task1(task_pairs)
    task2(task_pairs)

def task1(pairs):
    full_contain_count = 0
    

    for pair in pairs:
        min_left, max_left, min_right, max_right = pair[0][0], pair[0][-1], pair[-1][0], pair[-1][-1]
        
        if a_contains_b(min_left, max_left, min_right, max_right) or a_contains_b(min_right, max_right, min_left, max_left):
            full_contain_count += 1
    print(f"Result task1: {full_contain_count}")

def task2(pairs):
    overlap_count = 0
    for pair in pairs:
        min_left, max_left, min_right, max_right = pair[0][0], pair[0][-1], pair[-1][0], pair[-1][-1]
        if a_overlabs_b(min_left, max_left, min_right, max_right):
            overlap_count += 1
    print(f"Result task2: {overlap_count}")
    
def a_contains_b(a_min, a_max, b_min, b_max):
    """checks if a int range between max and min fully contains b"""
    if a_min <= b_min and a_max >= b_max:
        return True
    return False

def a_overlabs_b(a_min, a_max, b_min, b_max):
    """checks if a and be overlap"""
    if a_min <= b_min <= a_max or b_min <= a_min <= b_max:
        return True
    return False

def read_input(filename):
    """file reader"""
    with open(filename, "r") as f:
        return [transform_line(x) for x in f.readlines()]

def transform_line(string):
    """turns string into a list of tuples"""
    response_item = list()
    base_item = string.strip("\n").split(",")

    for x in base_item:
        ids = x.split("-")
        response_item.append((int(ids[0]), int(ids[-1])))
    return response_item

if __name__ == '__main__':
    main("input.txt")
