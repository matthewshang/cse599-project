def fill_room():
    # Sizes of objects
    bookshelf_scale = (1.5, 0.5, 4)
    table_scale = (2, 1, 1)
    chair_radius = 0.5
    lamp_radius = 0.2

    # Create bookshelves
    for i in range(6):
        bookshelf_location = ((bookshelf_scale[0] + 0.1) * i + bookshelf_scale[0] / 2, bookshelf_scale[1] / 2, bookshelf_scale[2] / 2)
        create_cube(bookshelf_location, bookshelf_scale, get_color("bookshelf"))

    # Create reading tables
    for i in range(3):
        table_location = (5, 5 + (table_scale[1] + 0.5) * i, table_scale[2] / 2)
        create_cube(table_location, table_scale, get_color("table"))

    # Create chairs
    for i in range(6):
        angle = i * 180  # 180 degrees to place two chairs per table
        chair_location = (5 + (table_scale[0] / 2 + chair_radius) * math.cos(angle), 5 + (table_scale[1] / 2 + chair_radius) * math.sin(angle), chair_radius)
        create_sphere(chair_location, chair_radius, get_color("chair"))

    # Create lamps
    for i in range(3):
        lamp_location = (5, 5 + (table_scale[1] + 0.5) * i, table_scale[2] + lamp_radius)
        create_sphere(lamp_location, lamp_radius, get_color("lamp"))