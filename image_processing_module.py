import numpy as np
from PIL import Image

def process_image(image: np.ndarray) -> np.ndarray:
    """
    Process the tile layout image.

    Args:
        image: Tile layout image

    Returns:
        np.ndarray: Processed tile layout image
    """
    # Convert image to grayscale
    gray = np.dot(image[...,:3], [0.2989, 0.5870, 0.1140])
    # Apply threshold to segment out objects
    thresh = np.where(gray > 128, 255, 0)
    # Save processed image
    Image.fromarray(thresh.astype(np.uint8)).save("processed_image.png")
    return thresh
