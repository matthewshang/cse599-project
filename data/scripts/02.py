def fill_room():
    # Sofa
    create_cube((5, 6, 0), (2, 0.8, 0.7), get_color("sofa"))
    
    # Armchair
    create_cube((7, 7, 0), (1.2, 0.8, 0.7), get_color("armchair"))
    
    # TV
    create_cube((5, 11, 1), (1.5, 0.1, 1), get_color("tv"))
    
    # Coffee Table
    create_cube((5, 7, 0), (1.2, 0.6, 0.4), get_color("table")))
    
    # Rug
    create_cube((5, 7, -0.05), (3, 2, 0.05), get_color("rug"))
    
    # Lamp
    create_cube((2, 2, 0), (0.3, 0.3, 1.5), get_color("lamp"))
    create_sphere((2, 2, 1.5), 0.5, get_color("lamp"))
    
    # Bookshelf
    create_cube((1, 11, 0), (0.4, 2, 2), get_color("bookshelf"))
    
    # Plants
    create_sphere((9, 13, 0), 0.5, get_color("plant"))
    create_sphere((1, 1, 0), 0.5, get_color("plant"))
