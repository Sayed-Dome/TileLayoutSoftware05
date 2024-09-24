from PIL import Image
import numpy as np

def save_rendering(rendering):
    rendering.savefig('tile_layout.png')
    img = Image.open('tile_layout.png')
    img.save('tile_layout.jpg')
