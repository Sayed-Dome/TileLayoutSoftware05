def brick_pattern(tile_size):
    # Define the brick pattern
    pattern = []
    for i in range(10):
        row = []
        for j in range(10):
            if (i + j) % 2 == 0:
                row.append(1)
            else:
                row.append(0)
        pattern.append(row)
    return pattern

def herringbone_pattern(tile_size):
    # Define the herringbone pattern
    pattern = []
    for i in range(10):
        row = []
        for j in range(10):
            if (i + j) % 2 == 0:
                row.append(1)
            else:
                row.append(0)
        pattern.append(row)
    return pattern

def hexagonal_pattern(tile_size):
    # Define the hexagonal pattern
    pattern = []
    for i in range(10):
        row = []
        for j in range(10):
            if (i + j) % 2 == 0:
                row.append(1)
            else:
                row.append(0)
        pattern.append(row)
    return pattern
