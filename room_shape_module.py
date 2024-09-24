class RoomShape:
    def __init__(self):
        self.room_shape = []

    def add_point(self, point):
        self.room_shape.append(point)

    def remove_point(self, point):
        self.room_shape.remove(point)

    def get_room_shape(self):
        return self.room_shape

class RectangularRoom(RoomShape):
    def __init__(self):
        super().__init__()

    def add_point(self, point):
        if len(self.room_shape) % 2 == 0:
            self.room_shape.append(point)
        else:
            self.room_shape.insert(0, point)

class NonRectangularRoom(RoomShape):
    def __init__(self):
        super().__init__()

    def add_point(self, point):
        if len(self.room_shape) % 2 == 0:
            self.room_shape.append(point)
        else:
            self.room_shape.insert(0, point)
