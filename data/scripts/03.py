def fill_room():
    bed_scale = Vector((2, 5, 1))
    nightstand_scale = Vector((1, 1, 1))
    lamp_scale = Vector((0.5, 0.5, 0.5))
    rug_radius = 2
    ceiling_light_radius = 0.5
    
    # Create the beds
    for i in range(3):
        bed_location = Vector((2, i*5 + 2.5, bed_scale.z/2))
        create_cube(bed_location, bed_scale, get_color("bed"))

        # Add a nightstand between the beds, but not after the last one
        if i < 2:
            nightstand_location = Vector((2, i*5 + 5, nightstand_scale.z/2))
            create_cube(nightstand_location, nightstand_scale, get_color("table"))

            # Add a lamp on each nightstand
            lamp_location = Vector((2, i*5 + 5, nightstand_scale.z + lamp_scale.z/2))
            create_cube(lamp_location, lamp_scale, get_color("lamp"))

    # Create the rug in the center of the room
    rug_location = Vector((5, 7.5, rug_radius))
    create_sphere(rug_location, rug_radius, get_color("rug"))

    # Create the ceiling light in the middle of the ceiling
    ceiling_light_location = Vector((5, 7.5, 5 - ceiling_light_radius))
    create_sphere(ceiling_light_location, ceiling_light_radius, get_color("lamp"))