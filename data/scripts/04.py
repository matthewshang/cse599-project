def fill_room():
    TABLE_SCALE = (4, 3, 0.1)
    CHAIR_SCALE = (0.5, 0.5, 1)
    PROJECTOR_SCALE = (0.5, 0.5, 0.2)
    SCREEN_SCALE = (3, 0.02, 2)
    CABINET_SCALE = (1, 1, 2)
    
    # Create the conference table at the center of the room
    table_location = (5, 7.5, TABLE_SCALE[2]/2)
    create_cube(table_location, TABLE_SCALE, get_color("table"))
    
    # Create the chairs
    for i in range(6):
        angle = 2*math.pi*i/6  # Calculate the position of the chair around the table
        chair_x = 5 + 2.5*math.cos(angle)  # Keep a 2.5 meter distance from the table center
        chair_y = 7.5 + 2.5*math.sin(angle)
        chair_location = (chair_x, chair_y, CHAIR_SCALE[2]/2)
        create_cube(chair_location, CHAIR_SCALE, get_color("chair"))

    # Create the projector
    projector_location = (5, 7.5, 5 - PROJECTOR_SCALE[2]/2)
    create_cube(projector_location, PROJECTOR_SCALE, get_color("projector"))
    
    # Create the screen
    screen_location = (0.5 + SCREEN_SCALE[0]/2, 7.5, 1 + SCREEN_SCALE[2]/2)
    create_cube(screen_location, SCREEN_SCALE, get_color("screen"))
    
    # Create the cabinet
    cabinet_location = (8.5, 13, CABINET_SCALE[2]/2)
    create_cube(cabinet_location, CABINET_SCALE, get_color("cabinet"))