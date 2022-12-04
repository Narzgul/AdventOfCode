with open("inputs/day2_input.txt") as file:
    puzzle_input = file.readlines()

# A X Rock
# B Y Paper
# C Z Scissors

shape_scores = {'X': 1, 'Y': 2, 'Z': 3}

outcomes_loss = {'A': 'Z', 'B': 'X', 'C': 'Y'}
outcomes_draw = {'A': 'X', 'B': 'Y', 'C': 'Z'}
outcomes_win = {'A': 'Y', 'B': 'Z', 'C': 'X'}
outcomes_shape = {'X': outcomes_loss, 'Y': outcomes_draw, 'Z': outcomes_win}
outcomes_score = {'X': 0, 'Y': 3, 'Z': 6}

score = 0

for line in puzzle_input:
    if len(line.strip()) != 0:
        shapes = line.split()
        score += outcomes_score[shapes[1]]
        score += shape_scores[outcomes_shape[shapes[1]][shapes[0]]]

print(score)
