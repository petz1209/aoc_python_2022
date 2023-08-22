def main(filename):
    taskHandler(filename, machine="cratemover_9000")
    taskHandler(filename, machine="cratemover_9001")
    
def taskHandler(filename, machine):
    """main business logic handler"""
    stack, instructions = read_input(filename)
    
    my_machine = machine_factory(machine)
    my_machine(stack, instructions)
    result_string = ""
    for k, v in stack.items():
        result_string += v[-1]
    print(f"Result Task with machine {machine}: {result_string}")

def machine_factory(machine):
    if machine == "cratemover_9000":
        return cratemover_9000
    else:
        return cratemover_9001

def cratemover_9000(stack, instructions):
    """moves items one by one"""
    for instruction in instructions:
        moved = 0
        while moved < instruction["count"]:
            move_item(instruction["source"], instruction["dest"], stack)
            moved += 1

def cratemover_9001(stack, instructions):
    """moves multiple items at once. therefor no resorting"""
    for instruction in instructions:
        move_n_items(instruction["source"], instruction["dest"], stack, instruction["count"])

def move_item(source, dest, stack):
    """moves the last item from source list to destination list"""
    item = stack[source].pop()
    stack[dest].append(item)

def move_n_items(source, dest, stack, n):
    """moves n items from the end of one list to the end of another"""
    items = stack[source][-n:]
    for item in items:
        stack[dest].append(item)
    stack[source] = stack[source][:-n]
    
def read_input(filename):
    """reads input file and stores lines in array.
    once an empty line appears it switches
    """

    with open(filename, "r") as f:
        stack, instructions = None, None
        stack_input, instruction_input = list(), list()
        mode = "read_array"
        while True:
            line = f.readline()
            if not line:
                break
            line = line.strip("\n")
            if line.isspace() or line == "":
                stack = create_stack(stack_input)
                mode = "read_moves"
            else:
                if mode == "read_array":
                    stack_input.append(line)
                else:
                    instruction_input.append(line)
    instructions = create_instructions(instruction_input)
    return stack, instructions

def create_stack(stack_input):
    """Here I try to build a stack
    
    Example stack input
    [
    "        [Z]",
    "        [N]",
    "        [D]",
    "[C] [M] [P]",
    "1   2   3",    
    ]
    ==>
    Example output
    {1: ["C"],
     2: ["M"],
     3: ["P", "D", "N", "Z"]
    }
    """
    # step1: reverse stack input to get headers up to
    # print(stack_input)
    # print("\n---------------------------------------------")
    stack_input.reverse()
    # print(stack_input)
    
    # step2: lets get the headers:
    headers_line = stack_input[0]
    column: dict[int, int] = dict()
    for idx, letter in enumerate(headers_line):
        if letter == " ":
            continue
        column[int(letter)] = idx
    
    # initialize our stack
    stack: dict[int, list[str]] = {x: [] for x in column}
    # populate stack    
    for row in stack_input[1:]:     # we exclude the header line
        for key in stack:
            # If the character at to column index is empty string we have reached limit of this laines size 
            if row[column[key]] == " ":
                continue
            # if it isn't empty character we put item ontop of current laine
            stack[key].append(row[column[key]])
    
    del stack_input
    del column
    return stack
            
def create_instructions(instruction_input):

    """example line
        move 1 from 7 to 6
    """
    instructions = list()
    for line in instruction_input:

        line = line.replace(" ", "").replace("move", "").replace("from", ",").replace("to", ",").split(",")
        line = {"count": int(line[0]), "source": int(line[1]), "dest": int(line[2])}
        instructions.append(line)
    del instruction_input
    return instructions

if __name__ == '__main__':
    file_name = "input.txt"
    main(file_name)



