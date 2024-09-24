import matplotlib.pyplot as plt

def save_rendering(rendering: plt.Figure) -> None:
    """
    Save the rendered tile layout to a file.

    Args:
        rendering: Rendered tile layout
    """
    rendering.savefig('tile_layout.png')
