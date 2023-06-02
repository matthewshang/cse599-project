def fill_room():
    # Object dimensions
    worktable_scale = (2, 2, 1)
    easel_stand_scale = (0.1, 0.1, 1.5)
    easel_canvas_scale = (1, 0.05, 1.5)
    art_supply_radius = 0.1

    # Create worktable
    worktable_location = (5, 7.5, worktable_scale[2] / 2)
    create_cube(worktable_location, worktable_scale, get_color("worktable"))

    # Create easels
    for i in range(4):
        angle = i * (2 * math.pi / 4)  # Distribute easels evenly around the table
        easel_distance = 3  # Distance from the center of the table
        easel_center_location = (5 + easel_distance * math.cos(angle), 7.5 + easel_distance * math.sin(angle), 0)
        easel_stand_location = (easel_center_location[0], easel_center_location[1], easel_stand_scale[2] / 2)
        easel_canvas_location = (easel_center_location[0], easel_center_location[1], easel_canvas_scale[2] / 2)
        create_cube(easel_stand_location, easel_stand_scale, get_color("easel"))
        create_cube(easel_canvas_location, easel_canvas_scale, get_color("canvas"))

    # Create art supplies
    for i in range(10):
        angle = i * (2 * math.pi / 10)  # Distribute art supplies evenly across the table
        art_supply_distance = worktable_scale[0] / 2  # Place art supplies at the edge of the table
        art_supply_location = (5 + art_supply_distance * math.cos(angle), 7.5 + art_supply_distance * math.sin(angle), worktable_scale[2] + art_supply_radius)
        create_sphere(art_supply_location, art_supply_radius, get_color("art_supply"))