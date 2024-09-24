def optimize_cutting(tile_size, num_tiles):
    width, length = tile_size
    waste = 0
    for i in range(int(num_tiles)):
        for j in range(int(num_tiles)):
            if (i + j) % 2 == 0:
                waste += width * length
    return waste
