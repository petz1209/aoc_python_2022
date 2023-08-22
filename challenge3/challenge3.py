import string


def main(filename):
    
    rucksacks = read_input(filename)
    task1(rucksacks)
    task2(rucksacks)

def task1(rucksacks):
    total_points = 0
    for rucksack in rucksacks:
        total_points += find_wrong_element(rucksack)
    print(f"task1 total points: {total_points}")

def task2(rucksacks):
    total_points = 0
    # print(f"rucksacks: {rucksacks}")
    # uniquify each character per rucksack
    rucksacks = ["".join(set([y for y in x])) for x in rucksacks]
    groups = create_groups(rucksacks, 0, 3)
    print(f"groups: {groups}")
    

    for group in groups:
        difference = list(set([x for x in group[0]]).intersection([x for x in group[1]], [x for x in group[2]]))[0]
        total_points += get_item_priority(difference)
    print(total_points)
    return None


    

    for c in string.ascii_lowercase:
        group_found = find_group_by_char(c, new_list_of_rucksacks)
        if group_found:
            priority= get_item_priority(c)
            total_points += priority
            print(f"badeg: {c} priority: {priority}")
    for c in string.ascii_uppercase:
        group_found = find_group_by_char(c, new_list_of_rucksacks)
        if group_found:
            priority= get_item_priority(c)
            total_points += priority
            print(f"badeg: {c} priority: {priority}")

    
    print(f"len(new_list_of_rucksacks): {len(new_list_of_rucksacks)}")

    print(f"task2 total points: {total_points}")


def create_groups(base_list, cursor, move):
    groups = list()
    while cursor < len(base_list):
        cursor
        groups.append(base_list[cursor: cursor+move])
        cursor += move
    return groups



def find_group_by_char(_char, group):
    """This is overdone"""
    index_list = list()
    for idx, rucksack in enumerate(rucksack_list):
        if _char in rucksack:
            index_list.append(idx)
            if len(index_list) == 3:
                print(f"_char: {_char} Rucksacks: {rucksack_list[index_list[0]]},  {rucksack_list[index_list[1]]},  {rucksack_list[index_list[1]]}")
                break

    if len(index_list) == 3:
        index_list.reverse()
        for x in index_list:
            del rucksack_list[x]
        print(f"len(rucksack_list): {len(rucksack_list)}")
        return True
    return False


def read_input(filename):
    
    with open(filename, "r") as f:
        data = [x.strip("\n") for x in f.readlines()]
    return data


def find_wrong_element(rucksack):
    rucksack_list = [x for x in rucksack]
    first_item_storage2 = int(len(rucksack_list) / 2)
    storage1 = rucksack_list[:first_item_storage2]
    storage2 = rucksack_list[first_item_storage2:]

    # returns a set of all items that are equal in both lists as a set. I we know it will only be one so we use index 0 at the end
    difference = list(set(storage1).intersection(storage2))[0]
    return get_item_priority(difference)
    

def get_item_priority(item):
    # find index of alphabetic value of difference
    alphabetic_idx = string.ascii_lowercase.index(item.lower())
    # add 1 as a has priority 1, not 0
    priority = alphabetic_idx + 1
    if item.isupper():
        priority += 26
    return priority

if __name__ == '__main__':
    file_name = "input.txt"
    main(file_name)
    