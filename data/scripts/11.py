def fill_room():
    # Sizes of objects
    desk_scale = (3, 1, 1)
    filing_cabinet_scale = (1, 1, 1)
    chair_radius = 0.5
    computer_scale = (0.5, 0.75, 0.25)
    bookshelf_scale = (2, 0.75, 4)

    # Create desk
    desk_location = (5, 1 + desk_scale[1] / 2, desk_scale[2] / 2)
    create_cube(desk_location, desk_scale, get_color("desk"))

    # Create filing cabinets
    filing_cabinet_location_left = (5 - desk_scale[0] / 2 - filing_cabinet_scale[0] / 2, 1 + filing_cabinet_scale[1] / 2, filing_cabinet_scale[2] / 2)
    filing_cabinet_location_right = (5 + desk_scale[0] / 2 + filing_cabinet_scale[0] / 2, 1 + filing_cabinet_scale[1] / 2, filing_cabinet_scale[2] / 2)
    create_cube(filing_cabinet_location_left, filing_cabinet_scale, get_color("filing_cabinet"))
    create_cube(filing_cabinet_location_right, filing_cabinet_scale, get_color("filing_cabinet"))

    # Create swivel chair
    chair_location = (5, 1 + desk_scale[1] + chair_radius + 0.1, chair_radius)
    create_sphere(chair_location, chair_radius, get_color("chair"))

    # Create computer
    computer_location = (5, 1 + desk_scale[1] / 2, desk_scale[2] + computer_scale[2] / 2)
    create_cube(computer_location, computer_scale, get_color("computer"))

    # Create bookshelf
    bookshelf_location = (bookshelf_scale[0] / 2, 15 - bookshelf_scale[1] / 2, bookshelf_scale[2] / 2)
    create_cube(bookshelf_location, bookshelf_scale, get_color("bookshelf"))