columns = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
rows    = {'1': 8, '2': 7, '3': 6, '4': 5, '5': 4, '6': 3, '7': 2, '8': 1}

def parse_move(move):
    return [columns[move[0]], rows[move[1]], columns[move[2]], rows[move[3]]]