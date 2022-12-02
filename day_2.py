from enum import Enum

from data.data_2_1 import strategy_guide
from util import print_header


class Shape(Enum):
    ROCK='ROCK'
    PAPER='PAPER'
    SCISSORS='SCISSORS'

class Outcome(Enum):
    LOSE = 'LOSE'
    DRAW = 'DRAW'
    WIN = 'WIN'

my_shapes = {
    'X': Shape.ROCK,
    'Y': Shape.PAPER,
    'Z': Shape.SCISSORS
}

their_shapes = {
    'A': Shape.ROCK,
    'B': Shape.PAPER,
    'C': Shape.SCISSORS
}

outcomes = {
    'X': Outcome.LOSE,
    'Y': Outcome.DRAW,
    'Z': Outcome.WIN
}


def get_score_for_shape(shape: Shape):
    if shape == Shape.ROCK:
        return 1
    if shape == Shape.PAPER:
        return 2
    if shape == Shape.SCISSORS:
        return 3

def get_score(my_shape: Shape, their_shape: Shape):
    # DRAW
    if my_shape == their_shape:
        return 3

    # I WIN
    if (
        (my_shape == Shape.ROCK and their_shape == Shape.SCISSORS)
        or
        (my_shape == Shape.SCISSORS and their_shape == Shape.PAPER)
        or 
        (my_shape == Shape.PAPER and their_shape == Shape.ROCK) 
    ):
        return 6

    # I LOSE
    return 0

# PART 1
print_header(day=2, part=1, expected_result=11767)

total_score = 0

for round in strategy_guide:
    # Read data
    their_shape = their_shapes[round[0]]
    my_shape = my_shapes[round[1]]

    # Calculate score
    score_for_shape = get_score_for_shape(my_shape)
    my_score_for_this_round = get_score(my_shape, their_shape)

    total_score = total_score + score_for_shape + my_score_for_this_round

print (total_score)



# PART 2
print_header(day=2, part=1, expected_result=13886)

def guess_my_shape(their_shape: Shape, outcome: Outcome) -> Shape:

    if outcome == Outcome.DRAW:
        return their_shape
    
    if outcome == Outcome.LOSE:
        if their_shape == Shape.ROCK:
            return Shape.SCISSORS
        if their_shape == Shape.SCISSORS:
            return Shape.PAPER
        if their_shape == Shape.PAPER:
            return Shape.ROCK

    if outcome == Outcome.WIN:
        if their_shape == Shape.ROCK:
            return Shape.PAPER
        if their_shape == Shape.SCISSORS:
            return Shape.ROCK
        if their_shape == Shape.PAPER:
            return Shape.SCISSORS


total_score = 0

for round in strategy_guide:
    # Read data
    their_shape = their_shapes[round[0]]
    outcome = outcomes[round[1]]

    my_shape = guess_my_shape(their_shape, outcome)

    # Calculate score
    score_for_shape = get_score_for_shape(my_shape)
    my_score_for_this_round = get_score(my_shape, their_shape)

    total_score = total_score + score_for_shape + my_score_for_this_round


print (total_score)
