def calculate_num_tiles(room_dimensions: tuple, tile_size: tuple, layout_pattern: str) -> int:
    """
    Calculate the number of tiles needed based on room dimensions, tile size, and layout pattern.

    Args:
        room_dimensions: Room dimensions (width, length)
        tile_size: Tile size (width, length)
        layout_pattern: Layout pattern (brick, herringbone, hexagonal)

    Returns:
        int: Number of tiles needed
    """
    width, length = room_dimensions
    tile_width, tile_length = tile_size

    if layout_pattern == "brick":
        num_tiles = (width * length) / (tile_width * tile_length)
    elif layout_pattern == "herringbone":
        num_tiles = (width * length) / (tile_width * tile_length)
    elif layout_pattern == "hexagonal":
        num_tiles = (width * length) / (tile_width * tile_length)

    return int(num_tiles)
