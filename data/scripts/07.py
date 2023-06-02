def fill_room():
    # Spacing between objects
    spacing = 0.2

    # Sizes of objects
    sofa_scale = (3, 1, 1)
    armchair_scale = (1, 1, 1)
    coffee_table_scale = (1.5, 1, 0.5)
    lamp_radius = 0.3
    rug_scale = (5, 7, 0.1)
    tv_scale = (2, 0.05, 1.5)
    tv_stand_scale = (2, 0.5, 0.75)

    # Create L-shaped sofa
    sofa_location1 = (sofa_scale[0] / 2, sofa_scale[1] / 2, sofa_scale[2] / 2)
    sofa_location2 = (sofa_scale[0] / 2, 1.5 * sofa_scale[1] + sofa_scale[1] / 2, sofa_scale[2] / 2)
    create_cube(sofa_location1, sofa_scale, get_color("sofa"))
    create_cube(sofa_location2, sofa_scale, get_color("sofa"))

    # Create armchairs
    armchair_location1 = (8, 4, armchair_scale[2] / 2)
    armchair_location2 = (8, 10, armchair_scale[2] / 2)
    create_cube(armchair_location1, armchair_scale, get_color("armchair"))
    create_cube(armchair_location2, armchair_scale, get_color("armchair"))

    # Create coffee table
    coffee_table_location = (5, 7, coffee_table_scale[2] / 2)
    create_cube(coffee_table_location, coffee_table_scale, get_color("table"))

    # Create lamp
    lamp_location = (0, 15, 4)
    create_sphere(lamp_location, lamp_radius, get_color("lamp"))

    # Create rug
    rug_location = (5, 7.5, 0)
    create_cube(rug_location, rug_scale, get_color("rug"))

    # Create TV and TV stand
    tv_location = (10 - tv_scale[0] / 2, 7.5, 3)
    tv_stand_location = (10 - tv_stand_scale[0] / 2, 7.5, tv_stand_scale[2] / 2)
    create_cube(tv_location, tv_scale, get_color("tv"))
    create_cube(tv_stand_location, tv_stand_scale, get_color("stand"))
