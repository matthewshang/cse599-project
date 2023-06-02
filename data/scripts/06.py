def fill_room():
    # Spacing between objects
    spacing = 0.2

    # Sizes of objects
    student_desk_scale = (1, 1.5, 0.75)
    student_chair_scale = (0.5, 0.5, 0.5)
    teacher_desk_scale = (1.5, 2, 0.75)
    teacher_chair_scale = (0.75, 0.75, 0.75)
    whiteboard_scale = (6, 0.05, 3)
    projector_radius = 0.3

    # Create student desks and chairs
    for i in range(3):
        for j in range(4):
            desk_location = (1 + j * (student_desk_scale[0] + spacing), 1 + i * (student_desk_scale[1] + spacing), 0)
            chair_location = (desk_location[0], desk_location[1] - student_desk_scale[1] / 2 - student_chair_scale[1] / 2 - spacing, 0)
            create_cube(desk_location, student_desk_scale, get_color("desk"))
            create_cube(chair_location, student_chair_scale, get_color("chair"))

    # Create teacher's desk and chair
    teacher_desk_location = (5, 13, 0)
    teacher_chair_location = (teacher_desk_location[0], teacher_desk_location[1] - teacher_desk_scale[1] / 2 - teacher_chair_scale[1] / 2 - spacing, 0)
    create_cube(teacher_desk_location, teacher_desk_scale, get_color("desk"))
    create_cube(teacher_chair_location, teacher_chair_scale, get_color("chair"))

    # Create whiteboard
    whiteboard_location = (5, 14.75, whiteboard_scale[2] / 2)
    create_cube(whiteboard_location, whiteboard_scale, get_color("whiteboard"))

    # Create projector
    projector_location = (5, 7.5, 4.5)
    create_sphere(projector_location, projector_radius, get_color("projector"))