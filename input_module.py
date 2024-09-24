def get_room_dimensions() -> tuple:
    """
    Get room dimensions from user input.

    Returns:
        tuple: Room dimensions (width, length)
    """
    while True:
        try:
            width = float(input("Enter room width (in mm): "))
            length = float(input("Enter room length (in mm): "))
            if width <= 0 or length <= 0:
                print("Invalid input. Please enter positive values.")
            else:
                return width, length
        except ValueError:
            print("Invalid input. Please enter numeric values.")

def get_tile_size() -> tuple:
    """
    Get tile size from user input.

    Returns:
        tuple: Tile size (width, length)
    """
    while True:
        try:
            width = float(input("Enter tile width (in mm): "))
            length = float(input("Enter tile length (in mm): "))
            if width <= 0 or length <= 0:
                print("Invalid input. Please enter positive values.")
            else:
                return width, length
        except ValueError:
            print("Invalid input. Please enter numeric values.")

def get_layout_pattern() -> str:
    """
    Get layout pattern from user input.

    Returns:
        str: Layout pattern (brick, herringbone, hexagonal)
    """
    while True:
        pattern = input("Enter layout pattern (brick, herringbone, hexagonal): ")
        if pattern.lower() in ["brick", "herringbone", "hexagonal"]:
            return pattern.lower()
        else:
            print("Invalid input. Please enter a valid layout pattern.")
