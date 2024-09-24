import input_module
import calculation_module
import rendering_module
import output_module
import integration_module

def main():
    try:
        room_dimensions = input_module.get_room_dimensions()
        tile_size = input_module.get_tile_size()
        layout_pattern = input_module.get_layout_pattern()
        num_tiles = calculation_module.calculate_num_tiles(room_dimensions, tile_size, layout_pattern)
        rendering = rendering_module.render_tile_layout(num_tiles, tile_size, layout_pattern)
        output_module.save_rendering(rendering)
        integration_module.integrate_with_autocad(rendering)
        integration_module.integrate_with_revit(rendering)
        integration_module.integrate_with_sketchup(rendering)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
