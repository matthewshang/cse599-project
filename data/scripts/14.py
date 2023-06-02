def fill_room():
    # Object dimensions
    conference_table_scale = (8, 4, 0.7)
    chair_scale = (0.6, 0.6, 1)
    chair_distance = 1.2  # Distance from the edge of the table

    # Create Conference Table
    conference_table_location = (5, 7.5, conference_table_scale[2] / 2)
    create_cube(conference_table_location, conference_table_scale, get_color("table"))

    # Create Chairs
    for i in range(10):
        # Calculate the location for each chair
        if i < 5:
            chair_location_x = 5 - conference_table_scale[0] / 2 + (i + 1) * chair_distance
            chair_location_y = 7.5 + conference_table_scale[1] / 2 + chair_distance
        else:
            chair_location_x = 5 - conference_table_scale[0] / 2 + (i - 4) * chair_distance
            chair_location_y = 7.5 - conference_table_scale[1] / 2 - chair_distance

        chair_location = (chair_location_x, chair_location_y, chair_scale[2] / 2)
        create_cube(chair_location, chair_scale, get_color("chair"))