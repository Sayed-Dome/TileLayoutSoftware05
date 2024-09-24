import matplotlib.pyplot as plt

def render_tile_layout(num_tiles, tile_size, layout_pattern):
    width, length = tile_size

    fig, ax = plt.subplots()
    ax.set_xlim(0, num_tiles * width)
    ax.set_ylim(0, num_tiles * length)
    ax.set_aspect('equal')

    for i in range(int(num_tiles)):
        for j in range(int(num_tiles)):
            if layout_pattern == "Brick":
                ax.add_patch(plt.Rectangle((i * width, j * length), width, length, fill=False))
            elif layout_pattern == "Herringbone":
                ax.add_patch(plt.Rectangle((i * width, j * length), width, length, fill=False))
            elif layout_pattern == "Hexagonal":
                ax.add_patch(plt.Rectangle((i * width, j * length), width, length, fill=False))

    return fig
