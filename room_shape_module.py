def complex_room_shape(room_dimensions):
    # Allow for complex room shapes, such as non-rectangular or curved spaces
    # For example, we can use a polygon to represent the room shape
    room_shape = []
    for i in range(10):
        point = (i * room_dimensions[0], i * room_dimensions[1])
        room_shape.append(point)
    return room_shape
