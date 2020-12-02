def get_lines(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

    return lines


def get_all_character_naive_indexes(character, s):
    return [i + 1 for i, char in enumerate(s) if char == character]


def get_valid_password_count_at_old_job(filename="input.txt"):
    lines = get_lines(filename)
    valid_password_count = 0
    for line in lines:
        (input_params, password) = line.split(":")
        (target_char_range, target_char) = input_params.split()
        (min_chars, max_chars) = [int(s) for s in target_char_range.split("-")]
        password = password.strip()
        num_target_chars = password.count(target_char)
        if min_chars <= num_target_chars <= max_chars:
            valid_password_count += 1

    return valid_password_count


def get_valid_password_count_at_new_job(filename="input.txt"):
    lines = get_lines(filename)
    valid_password_count = 0
    for line in lines:
        (input_params, password) = line.split(":")
        (target_char_positions, target_char) = input_params.split()
        (first_char_pos, second_char_pos) = [
            int(s) for s in target_char_positions.split("-")
        ]
        password = password.strip()
        observed_char_positions = get_all_character_naive_indexes(target_char, password)
        if (first_char_pos in observed_char_positions) ^ (
            second_char_pos in observed_char_positions
        ):
            valid_password_count += 1

    return valid_password_count


valid_password_count_at_old_job = get_valid_password_count_at_old_job()
print(f"Valid password count at old job: {valid_password_count_at_old_job}")
valid_password_count_at_new_job = get_valid_password_count_at_new_job()
print(f"Valid password count at new job: {valid_password_count_at_new_job}")

