"""
Advent of Code 2022 Challenge 2 by pleitner
"""


class Rock:
    points = 1
    def vs(self, cometitor):
        if isinstance(cometitor, Rock):
            return 3
        if isinstance(cometitor, Paper):
            return 0
        if isinstance(cometitor, Sizzer):
            return 6

class Paper:
    points = 2
    def vs(self, cometitor):
        if isinstance(cometitor, Rock):
            return 6
        if isinstance(cometitor, Paper):
            return 3
        if isinstance(cometitor, Sizzer):
            return 0

class Sizzer:
    points = 3
    def vs(self, cometitor):
        if isinstance(cometitor, Rock):
            return 0
        if isinstance(cometitor, Paper):
            return 6
        if isinstance(cometitor, Sizzer):
            return 3

class RightChoice:
    """based on strategy and cometitor it return a class instance that will win, lose or draw against competitor"""
    def win(competitor):
        if isinstance(competitor, Rock):
            return Paper()
        if isinstance(competitor, Paper):
            return Sizzer()
        return Rock()
    def draw(competitor):
        return competitor
    
    def lose(competitor):
        if isinstance(competitor, Rock):
            return Sizzer()
        if isinstance(competitor, Paper):
            return Rock()
        return Paper()


def main1(file_name):
    """returns the total points if second item of data rows represents the class to choose"""
    code_map = dict(A=Rock(), B=Paper(), C=Sizzer(), X=Rock(), Y=Paper(), Z=Sizzer())
    rounds = get_input(file_name)
    my_total_points = 0
    for _round in rounds:
        competitor_choice = code_map.get(_round[0])
        my_choice = code_map.get(_round[1])
        my_total_points += my_choice.points
        my_total_points += my_choice.vs(competitor_choice)
    print(f"Result part1: {my_total_points}")

def main2(file_name):
    code_map =  dict(A=Rock(), B=Paper(), C=Sizzer())
    strategy_map = dict(X="lose", Y="draw", Z="win")
    rounds = get_input(file_name)
    my_total_points = 0
    for x in rounds:
        competitor_choice = code_map.get(x[0])
        strategy = strategy_map.get(x[1])
        my_choice = choice_factory(competitor_choice, strategy)
        my_total_points += my_choice.points
        my_total_points += my_choice.vs(competitor_choice)
    print(f"Result part2: {my_total_points}")

def choice_factory(competitor, round_strategy):
    if round_strategy == "lose":
        return RightChoice.lose(competitor)
    if round_strategy == "draw":
        return RightChoice.draw(competitor)
    return RightChoice.win(competitor)
        
def get_input(filename):
    with open(filename, "r") as f:
        data = [x.strip("\n").split(" ") for x in f.readlines()]
    return data

if __name__ == '__main__':
    main1("input.txt")
    main2("input.txt")
    

        