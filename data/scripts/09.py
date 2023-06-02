def fill_room():
    # Sizes of objects
    countertop_scale = (0.75, 8, 1)
    bar_stool_scale = (0.5, 0.5, 0.5)
    fridge_scale = (1, 1, 2)
    stove_scale = (1, 0.75, 1)
    sink_scale = (0.75, 0.5, 0.25)

    # Create countertop
    countertop_location = (countertop_scale[0] / 2, countertop_scale[1] / 2, countertop_scale[2] / 2)
    create_cube(countertop_location, countertop_scale, get_color("countertop"))

    # Create bar stools
    for i in range(4):
        bar_stool_location = (countertop_scale[0] + bar_stool_scale[0] / 2 + 0.5, (i + 1) * 2 - bar_stool_scale[1] / 2, bar_stool_scale[2] / 2)
        create_cube(bar_stool_location, bar_stool_scale, get_color("stool"))

    # Create fridge
    fridge_location = (10 - fridge_scale[0] / 2, 15 - fridge_scale[1] / 2, fridge_scale[2] / 2)
    create_cube(fridge_location, fridge_scale, get_color("fridge"))

    # Create stove
    stove_location = (2 * countertop_scale[0] + stove_scale[0] / 2, countertop_scale[1] / 2, stove_scale[2] / 2)
    create_cube(stove_location, stove_scale, get_color("stove"))

    # Create sink
    sink_location = (countertop_scale[0] / 2, countertop_scale[1] / 2, countertop_scale[2] + sink_scale[2] / 2)
    create_cube(sink_location, sink_scale, get_color("sink"))