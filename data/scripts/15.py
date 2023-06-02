def fill_room():
    # Object dimensions
    desk_scale = (1, 2, 0.8)
    radius = 4  # Radius of the circle of desks

    # Create Desks
    for i in range(6):
        # Calculate the location for each desk
        angle = 2 * math.pi * i / 6  # Divide the circle into 6 equal parts
        desk_location_x = 5 + radius * math.cos(angle)  # x = r*cos(theta)
        desk_location_y = 7.5 + radius * math.sin(angle)  # y = r*sin(theta)

        desk_location = (desk_location_x, desk_location_y, desk_scale[2] / 2)
        create_cube(desk_location, desk_scale, get_color("desk"))