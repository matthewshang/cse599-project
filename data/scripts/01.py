def fill_room():
    def create_chairs(start_pos, num, color):
        for i in range(num):
            create_cube((start_pos[0] + i*2, start_pos[1], start_pos[2]), (0.5, 0.5, 1.5), color)


    # Create chairs
    create_chairs((1, 4, 0), 5, get_color("chair"))
    create_chairs((2, 7, 0), 3, get_color("chair"))

    # Create teacher's desk
    create_cube((7, 12, 0), (2, 1, 1), get_color("desk"))

    # Create chalkboard/whiteboard
    create_cube((5, 14.95, 1.5), (4, 0.1, 3), get_color("board"))

    # Create podium
    create_cube((9, 12, 0), (1, 1, 1), get_color("podium"))

    # Create clock
    create_sphere((5, 14.95, 4), 0.5, get_color("clock"))

    # Create students' desks
    for i in range(5):
        create_cube((1 + i*2, 3.5, 0), (1, 0.7, 1.5), get_color("desk"))
    for i in range(3):
        create_cube((2 + i*2, 6.5, 0), (1, 0.7, 1.5), get_color("desk"))

    # Create bookshelf
    create_cube((0.5, 7, 2), (1, 3, 4), get_color("bookshelf"))