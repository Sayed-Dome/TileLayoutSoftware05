import unittest
from tile_layout_module import TileLayout

class TestTileLayout(unittest.TestCase):
    def test_tile_layout(self):
        tile_layout = TileLayout()
        self.assertEqual(tile_layout.get_tile_layout(), [])

    def test_add_tile(self):
        tile_layout = TileLayout()
        tile_layout.add_tile("Tile 1")
        self.assertEqual(tile_layout.get_tile_layout(), ["Tile 1"])

    def test_remove_tile(self):
        tile_layout = TileLayout()
        tile_layout.add_tile("Tile 1")
        tile_layout.remove_tile("Tile 1")
        self.assertEqual(tile_layout.get_tile_layout(), [])

if __name__ == "__main__":
    unittest.main()
