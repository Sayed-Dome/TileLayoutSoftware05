import panda3d

def visualize_3d(tile_layout: list) -> None:
    """
    Visualize the tile layout in 3D.

    Args:
        tile_layout: Tile layout
    """
    # Create a 3D window
    window = panda3d.ShowBase()

    # Create a 3D model of the tile layout
    model = panda3d.Model()
    for i in range(len(tile_layout)):
        for j in range(len(tile_layout[i])):
            if tile_layout[i][j] == 1:
                model.add_node(panda3d.NodePath(panda3d.ModelNode("tile")))
                model.set_pos(i * 10, j * 10, 0)
                model.set_scale(10, 10, 10)
                model.reparent_to(window.render)

    # Run the 3D visualization
    window.run()
