with open("inputs/day2_input.txt") as file:
    puzzle_input = file.readlines()

# A X Rock
# B Y Paper
# C Z Scissors

shape_scores = {'X': 1, 'Y': 2, 'Z': 3}

scores_rock = {'A': 3, 'B': 0, 'C': 6}
scores_paper = {'A': 6, 'B': 3, 'C': 0}
scores_scissors = {'A': 0, 'B': 6, 'C': 3}
scores_outcome = {'X': scores_rock, 'Y': scores_paper, 'Z': scores_scissors}

score = 0

for line in puzzle_input:
    if len(line.strip()) != 0:
        shapes = line.split()
        score += shape_scores[shapes[1]]
        score += scores_outcome[shapes[1]][shapes[0]]

print(score)
