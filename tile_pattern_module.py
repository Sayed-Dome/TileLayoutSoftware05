class TilePattern:
    def __init__(self):
        self.tile_pattern = []

    def add_tile(self, tile):
        self.tile_pattern.append(tile)

    def remove_tile(self, tile):
        self.tile_pattern.remove(tile)

    def get_tile_pattern(self):
        return self.tile_pattern

class BrickPattern(TilePattern):
    def __init__(self):
        super().__init__()

    def add_tile(self, tile):
        if len(self.tile_pattern) % 2 == 0:
            self.tile_pattern.append(tile)
        else:
            self.tile_pattern.insert(0, tile)

class HerringbonePattern(TilePattern):
    def __init__(self):
        super().__init__()

    def add_tile(self, tile):
        if len(self.tile_pattern) % 2 == 0:
            self.tile_pattern.append(tile)
        else:
            self.tile_pattern.insert(0, tile)

class HexagonalPattern(TilePattern):
    def __init__(self):
        super().__init__()

    def add_tile(self, tile):
        if len(self.tile_pattern) % 2 == 0:
            self.tile_pattern.append(tile)
        else:
            self.tile_pattern.insert(0, tile)
