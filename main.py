import input_module
import calculation_module
import rendering_module
import output_module

def main():
    room_dimensions = input_module.get_room_dimensions()
    tile_size = input_module.get_tile_size()
    layout_pattern = input_module.get_layout_pattern()
    num_tiles = calculation_module.calculate_num_tiles(room_dimensions, tile_size, layout_pattern)
    rendering = rendering_module.render_tile_layout(num_tiles, tile_size, layout_pattern)
    output_module.save_rendering(rendering)

if __name__ == "__main__":
    main()
