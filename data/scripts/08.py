def fill_room():
    # Sizes of objects
    bed_scale = (2, 3, 1)
    bedside_table_scale = (0.75, 0.75, 0.75)
    lamp_radius = 0.25
    wardrobe_scale = (2, 1, 3)
    desk_scale = (2.5, 1, 1)
    chair_scale = (0.75, 0.75, 0.75)

    # Create twin beds
    bed_location1 = (bed_scale[0] / 2, bed_scale[1] / 2, bed_scale[2] / 2)
    bed_location2 = (1.5 * bed_scale[0], bed_scale[1] / 2, bed_scale[2] / 2)
    create_cube(bed_location1, bed_scale, get_color("bed"))
    create_cube(bed_location2, bed_scale, get_color("bed"))

    # Create bedside tables and lamps
    bedside_table_location1 = (bed_scale[0] / 2 - bedside_table_scale[0] / 2 - 0.5, bed_scale[1] / 2, bedside_table_scale[2] / 2)
    bedside_table_location2 = (2.5 * bed_scale[0] + bedside_table_scale[0] / 2 + 0.5, bed_scale[1] / 2, bedside_table_scale[2] / 2)
    lamp_location1 = (bedside_table_location1[0], bedside_table_location1[1], bedside_table_scale[2] + lamp_radius)
    lamp_location2 = (bedside_table_location2[0], bedside_table_location2[1], bedside_table_scale[2] + lamp_radius)
    create_cube(bedside_table_location1, bedside_table_scale, get_color("table"))
    create_cube(bedside_table_location2, bedside_table_scale, get_color("table"))
    create_sphere(lamp_location1, lamp_radius, get_color("lamp"))
    create_sphere(lamp_location2, lamp_radius, get_color("lamp"))

    # Create wardrobe
    wardrobe_location = (10 - wardrobe_scale[0] / 2, 7.5, wardrobe_scale[2] / 2)
    create_cube(wardrobe_location, wardrobe_scale, get_color("wardrobe"))

    # Create desk and chair
    desk_location = (desk_scale[0] / 2, 15 - desk_scale[1] / 2, desk_scale[2] / 2)
    chair_location = (desk_scale[0] / 2, 15 - desk_scale[1] / 2 - chair_scale[1] - 0.5, chair_scale[2] / 2)
    create_cube(desk_location, desk_scale, get_color("desk"))
    create_cube(chair_location, chair_scale, get_color("chair"))
