def convert_bp_to_id(bp):
    row, col = 0, 0
    low, high = 0, 127
    low_row, high_row = 0, 7
    last_row_op, last_col_op = "", ""
    for idx, char in enumerate(bp):
        if char in ["F", "B"]:
            if char == "F":
                high = (low + high) // 2
            elif char == "B":
                low = (low + high) // 2 + 1
            if bp[idx + 1] not in ["F", "B"]:
                last_row_op = char
        if char in ["L", "R"]:
            if char == "L":
                high_row = (low_row + high_row) // 2
            elif char == "R":
                low_row = (low_row + high_row) // 2 + 1
            if idx == len(bp) - 1:
                last_col_op = char
    row = low if last_row_op == "F" else high
    col = low_row if last_col_op == "L" else high_row
    return row * 8 + col


with open("input.txt", "r") as file:
    seating_input = file.read()
    seating_input = seating_input.split("\n")
    max_id = -1
    seat_ids = [convert_bp_to_id(seating) for seating in seating_input]

seat_ids = sorted(seat_ids)
for idx, char in enumerate(seat_ids):
    if idx + 1 < len(seat_ids) and seat_ids[idx] + 1 != seat_ids[idx + 1]:
        print(seat_ids[idx] + 1)
