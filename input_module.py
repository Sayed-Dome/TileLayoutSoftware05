def get_room_dimensions():
    width = float(input("Enter room width (in mm): "))
    length = float(input("Enter room length (in mm): "))
    return width, length

def get_tile_size():
    width = float(input("Enter tile width (in mm): "))
    length = float(input("Enter tile length (in mm): "))
    return width, length

def get_layout_pattern():
    pattern = input("Enter layout pattern (brick, herringbone, or hexagonal): ")
    return pattern.lower()
