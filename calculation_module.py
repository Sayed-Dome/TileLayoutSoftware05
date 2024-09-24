import numpy as np
from scipy import optimize

def calculate_num_tiles(room_dimensions, tile_size, layout_pattern):
    width, length = room_dimensions
    tile_width, tile_length = tile_size

    if layout_pattern == "Brick":
        num_tiles = (width * length) / (tile_width * tile_length)
    elif layout_pattern == "Herringbone":
        num_tiles = (width * length) / (tile_width * tile_length)
    elif layout_pattern == "Hexagonal":
        num_tiles = (width * length) / (tile_width * tile_length)

    return num_tiles
