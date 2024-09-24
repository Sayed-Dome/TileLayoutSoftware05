import matplotlib.pyplot as plt

def render_tile_layout(num_tiles: int, tile_size: tuple, layout_pattern: str) -> plt.Figure:
    """
    Render the tile layout using Matplotlib.

    Args:
        num_tiles: Number of tiles
        tile_size: Tile size (width, length)
        layout_pattern: Layout pattern (brick, herringbone, hexagonal)

    Returns:
        plt.Figure: Rendered tile layout
    """
    width, length = tile_size

    fig, ax = plt.subplots()
    ax.set_xlim(0, num_tiles * width)
    ax.set_ylim(0, num_tiles * length)
    ax.set_aspect('equal')

    for i in range(num_tiles):
        for j in range(num_tiles):
            if layout_pattern == "brick":
                ax.add_patch(plt.Rectangle((i * width, j * length), width, length, fill=False))
            elif layout_pattern == "herringbone":
                ax.add_patch(plt.Rectangle((i * width, j * length), width, length, fill=False))
            elif layout_pattern == "hexagonal":
                ax.add_patch(plt.Rectangle((i * width, j * length), width, length, fill=False))
    return fig

