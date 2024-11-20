def handle_left_zero(time, digit_map, i):
    if time[0] == '0' and i == 0:
        digit_map['0'] = ['   ', '   ', '   ']
    else:
        digit_map['0'] =  [' _ ', '| |', '|_|']
 
def build_time(time, digit_map):
    lines = ['', '', '']
    for i, char in enumerate(time):
            handle_left_zero(time, digit_map, i)
            for j in range(3):
                lines[j] += digit_map[char][j]
    return lines

def seven_segmentify(time):
    digit_map = {
        '0': [' _ ', '| |', '|_|'],
        '1': ['   ', '  |', '  |'],
        '2': [' _ ', ' _|', '|_ '],
        '3': [' _ ', ' _|', ' _|'],
        '4': ['   ', '|_|', '  |'],
        '5': [' _ ', '|_ ', ' _|'],
        '6': [' _ ', '|_ ', '|_|'],
        '7': [' _ ', '  |', '  |'],
        '8': [' _ ', '|_|', '|_|'],
        '9': [' _ ', '|_|', ' _|'],
        ':': ['   ', ' . ', ' . ']
    }
    lines = build_time(time, digit_map)
    return '\n'.join(lines)