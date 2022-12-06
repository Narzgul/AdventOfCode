def all_unique(char_array):
    for test_char in char_array:
        if char_array.count(test_char) > 1:
            return False
    return True


with open("inputs/day6_input.txt") as puzzle_input:
    chars_processed = 0

    most_recent_chars = []
    for char in puzzle_input.readline():
        chars_processed += 1
        most_recent_chars.append(char)
        if len(most_recent_chars) == 4 and all_unique(most_recent_chars):
            break

        if len(most_recent_chars) >= 4:
            most_recent_chars.pop(0)

    print(chars_processed)
