def fill_room():
    # Sizes of objects
    table_radius = 2
    chair_scale = (0.75, 0.75, 0.75)
    chandelier_radius = 0.5
    sideboard_scale = (3, 0.75, 1)

    # Create round table
    table_location = (5, 7.5, table_radius)
    create_sphere(table_location, table_radius, get_color("table"))

    # Create dining chairs
    for i in range(8):
        angle = i * math.pi / 4  # 45 degrees in radians
        chair_location = (5 + (table_radius + chair_scale[0]) * math.cos(angle), 7.5 + (table_radius + chair_scale[1]) * math.sin(angle), chair_scale[2] / 2)
        create_cube(chair_location, chair_scale, get_color("chair"))

    # Create chandelier
    chandelier_location = (5, 7.5, 4.5)
    create_sphere(chandelier_location, chandelier_radius, get_color("chandelier"))

    # Create sideboard
    sideboard_location = (sideboard_scale[0] / 2, 15 - sideboard_scale[1] / 2, sideboard_scale[2] / 2)
    create_cube(sideboard_location, sideboard_scale, get_color("sideboard"))