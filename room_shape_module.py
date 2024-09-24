def complex_room_shape(room_dimensions):
    width, length = room_dimensions
    room_shape = []
    for i in range(10):
        point = (i * width, i * length)
        room_shape.append(point)
    return room_shape
