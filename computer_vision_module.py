import cv2
import numpy as np

def detect_objects(image: np.ndarray) -> list:
    """
    Detect objects in the tile layout image.

    Args:
        image: Tile layout image

    Returns:
        list: List of detected objects
    """
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply threshold to segment out objects
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    # Find contours of objects
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours

def recognize_objects(contours: list) -> list:
    """
    Recognize objects in the tile layout image.

    Args:
        contours: List of contours of objects

    Returns:
        list: List of recognized objects
    """
    objects = []
    for contour in contours:
        # Calculate area of contour
        area = cv2.contourArea(contour)
        # Check if area is within a certain range
        if area > 100 and area < 1000:
            # Calculate perimeter of contour
            perimeter = cv2.arcLength(contour, True)
            # Calculate aspect ratio of contour
            aspect_ratio = float(perimeter) / area
            # Check if aspect ratio is within a certain range
            if aspect_ratio > 2 and aspect_ratio < 5:
                # Recognize object as a tile
                objects.append("Tile")
    return objects
