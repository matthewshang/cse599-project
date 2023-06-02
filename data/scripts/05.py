def fill_room():    
    # Shelves (two cubes stacked)
    shelf_height = 2.5
    create_cube((5, 7.5, shelf_height/2), (1, 7, shelf_height), get_color("shelf"))
    create_cube((5, 7.5, shelf_height*1.5 + 1), (1, 7, shelf_height), get_color("shelf"))

    # Random books on shelves
    for z in [shelf_height/2, shelf_height*1.5 + 1]:
        for x in range(1, 9):
            book_height = random.uniform(0.1, 0.3)
            book_width = random.uniform(0.5, 1)
            book_depth = random.uniform(0.05, 0.1)
            create_cube((x, 7.5, z + book_height/2), (book_width, book_depth, book_height), get_color("book"))

    # Desk
    create_cube((5, 3, 0.75), (3, 1.5, 0.5), get_color("desk"))

    # Chair
    create_cube((5, 1.5, 0.45), (1, 1, 0.9), get_color("chair"))

    # Table lamp on desk (represented by a sphere)
    create_sphere((5, 3, 1.5), 0.25, get_color("lamp"))

    # Plants
    create_sphere((1, 1, 0.5), 0.5, get_color("plant"))
    create_sphere((9, 1, 0.5), 0.5, get_color("plant"))

    # Carpet under desk and chair
    create_cube((5, 2.25, 0.01), (4, 2.5, 0.02), get_color("rug"))