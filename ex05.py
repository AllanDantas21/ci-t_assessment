def possibilities(signals):
    morse_tree = {
        "-": ["T"],
        ".": ["E"],
        "..": ["I"],
        ".-": ["A"],
        "...": ["S"],
        "..-": ["U"],
        ".-.": ["R"],
        ".--": ["W"],
        "-.": ["N"],
        "--": ["M"],
        "-..": ["D"],
        "-.-": ["K"],
        "--.": ["G"],
        "---": ["O"]
    }
    def helper(path, signals):
        if not signals:
            return morse_tree.get(path, [])
        if signals[0] == '?':
            return helper(path + '.', signals[1:]) + helper(path + '-', signals[1:])
        return helper(path + signals[0], signals[1:])
    possibilities = helper("", signals)
    return possibilities