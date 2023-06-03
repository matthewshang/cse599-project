import bpy
import mathutils
from mathutils import Vector
import math
import random

def make_emissive(color):
    mat = bpy.data.materials.new(name="Material")
    mat.use_nodes = True
    material_output = mat.node_tree.nodes.get('Material Output')
    emission = mat.node_tree.nodes.new('ShaderNodeEmission')
    emission.inputs['Strength'].default_value = 1.0
    adjusted_color = (color[0] / 255, color[1] / 255, color[2] / 255, 1)
    emission.inputs['Color'].default_value = adjusted_color
    mat.node_tree.links.new(material_output.inputs[0], emission.outputs[0])

def create_cube(location, scale, color):
    bpy.ops.mesh.primitive_cube_add(location=location)
    cube = bpy.context.active_object
    cube.scale = (scale[0] / 2, scale[1] / 2, scale[2] / 2)
    cube.active_material = make_emissive(color)
    return cube

def create_sphere(location, scale, color):
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=5, location=location, radius=scale)
    sphere = bpy.context.active_object
    sphere.active_material = make_emissive(color)
    return sphere

# Segmentation colors used by ADE20K Color150 Semantic Segmentation
# Source: https://github.com/Mikubill/sd-webui-controlnet/discussions/445
colors = {
    "airplane": (0, 255, 82),
    "animal": (255, 0, 122),
    "apparel": (0, 112, 255),
    "arcade": (255, 92, 0),
    "armchair": (8, 255, 214),
    "ashcan": (173, 0, 255),
    "awning": (0, 255, 61),
    "bag": (70, 184, 160),
    "ball": (255, 0, 163),
    "bannister": (0, 122, 255),
    "bar": (0, 255, 153),
    "barrel": (255, 0, 112),
    "base": (255, 122, 8),
    "basket": (92, 255, 0),
    "bathtub": (102, 8, 255),
    "bed": (204, 5, 255),
    "bench": (194, 255, 0),
    "bicycle": (255, 245, 0),
    "blanket": (20, 0, 255),
    "blind": (0, 61, 255),
    "boat": (173, 255, 0),
    "book": (255, 163, 0),
    "bookcase": (0, 255, 245),
    "booth": (255, 0, 204),
    "bottle": (0, 255, 10),
    "box": (0, 255, 20),
    "bridge": (255 ,82, 0),
    "buffet": (255, 112, 0),
    "building": (180, 120, 120),
    "bulletin": (184, 255, 0),
    "bus": (255, 0, 245),
    "cabinet": (224, 5, 255),
    "canopy": (0, 255, 92),
    "car": (0, 102, 200),
    "case": (0, 0, 255),
    "ceiling": (120, 120, 80),
    "chair": (204, 70, 3),
    "chandelier": (0, 31, 255),
    "chest": (6, 51, 255),
    "clock": (102, 255, 0),
    "coffee": (0, 255, 112),
    "column": (255, 8, 41),
    "computer": (0, 255, 173),
    "conveyer": (133, 0, 255),
    "counter": (235, 12, 255),
    "countertop": (0, 143, 255),
    "cradle": (153, 0, 255),
    "crt": (122, 0, 255),
    "curtain": (255, 51, 7),
    "cushion": (255, 194, 7),
    "desk": (10, 255, 71),
    "dirt": (0, 10, 255),
    "dishwasher": (214, 255, 0),
    "door": (8, 255, 51),
    "earth": (120, 120, 70),
    "escalator": (0, 255, 163),
    "fan": (0, 245, 255),
    "fence": (255, 184, 6),
    "field": (112, 9, 255),
    "fireplace": (250, 10, 15),
    "flag": (92, 0, 255),
    "floor": (80, 50, 50),
    "flower": (255, 0, 0),
    "food": (255, 204, 0),
    "fountain": (8, 184, 170),
    "glass": (25, 194, 194),
    "grandstand": (31, 255, 0),
    "grass": (4, 250, 7),
    "hill": (255, 102, 0),
    "hood": (0, 153, 255),
    "house": (255, 9, 224),
    "hovel": (255, 0, 255),
    "kitchen": (0, 255, 41),
    "lake": (10, 190, 212),
    "lamp": (224, 255, 8),
    "land": (0, 194, 255),
    "light": (255, 173, 0),
    "microwave": (255, 0, 235),
    "minibike": (163, 0, 255),
    "mirror": (220, 220, 220),
    "monitor": (0, 92, 255),
    "mountain": (143, 255, 140),
    "ottoman": (255, 153, 0),
    "oven": (71, 255, 0),
    "painting": (255, 6, 51),
    "palm": (0, 82, 255),
    "path": (255, 31, 0),
    "person": (150, 5, 61),
    "pier": (71, 0, 255),
    "pillow": (0, 235, 255),
    "plant": (204, 255, 4),
    "plate": (0, 255, 184),
    "plaything": (255, 0, 31),
    "pole": (51, 0, 255),
    "pool": (255, 71, 0),
    "poster": (143, 255, 0),
    "pot": (245, 0, 255),
    "radiator": (255, 214, 0),
    "railing": (255, 61, 6),
    "refrigerator": (20, 255, 0),
    "river": (11, 200, 200),
    "road": (140, 140, 140),
    "rock": (255, 41, 10),
    "rug": (255, 9, 92),
    "runway": (153, 255, 0),
    "sand": (160, 150, 20),
    "sconce": (0, 41, 255),
    "screen": (0, 173, 255),
    "screen": (0, 204, 255),
    "sculpture": (255, 255, 0),
    "sea": (9, 7, 230),
    "seat": (7, 255, 224),
    "shelf": (255, 7, 71),
    "ship": (255, 235, 0),
    "shower": (0, 133, 255),
    "sidewalk": (235, 255, 7),
    "signboard": (255, 5, 153),
    "sink": (0, 163, 255),
    "sky": (6, 230, 230),
    "skyscraper": (140, 140, 140),
    "sofa": (11, 102, 255),
    "stage": (82, 0, 255),
    "stairs": (255, 224, 0),
    "stairway": (31, 0, 255),
    "step": (255, 0, 143),
    "stool": (0, 214, 255),
    "stove": (51, 255, 0),
    "streetlight": (0, 71, 255),
    "swimming": (0, 184, 255),
    "swivel": (10, 0, 255),
    "table": (255, 6, 82),
    "tank": (0, 255, 235),
    "television": (0, 255, 194),
    "tent": (112, 224, 255),
    "toilet": (0, 255, 133),
    "towel": (255, 0, 102),
    "tower": (255, 184, 184),
    "trade": (133, 255, 0),
    "traffic": (41, 0, 255),
    "tray": (41, 255, 0),
    "tree": (4, 200, 3),
    "truck": (255, 0, 20),
    "van": (163, 255, 0),
    "vase": (0, 255, 204),
    "wall": (120, 120, 120),
    "wardrobe": (7, 255, 255),
    "washer": (184, 0, 255),
    "water": (61, 230, 250),
    "waterfall": (0, 224, 255),
    "windowpane": (230, 230, 230),
}

def get_color(name):
    if name in colors:
        return colors[name]
    else:
        # Unused color
        return (10, 10, 10)

ROOM_DIMS = (10, 15, 5)

def create_room():
    # Create floor
    create_cube((ROOM_DIMS[0] / 2, ROOM_DIMS[1] / 2, 0), 
                (ROOM_DIMS[0],     ROOM_DIMS[1],     0.1), get_color("floor"))

    # Front wall
    create_cube((ROOM_DIMS[0] / 2, 0,   ROOM_DIMS[2] / 2), 
                (ROOM_DIMS[0],     0.1, ROOM_DIMS[2]), get_color("wall"))  
    # Back wall
    create_cube((ROOM_DIMS[0] / 2, ROOM_DIMS[1], ROOM_DIMS[2] / 2), 
                (ROOM_DIMS[0],     0.1,          ROOM_DIMS[2]), get_color("wall"))  
    # Left wall
    create_cube((0,   ROOM_DIMS[1] / 2, ROOM_DIMS[2] / 2), 
                (0.1, ROOM_DIMS[1],     ROOM_DIMS[2]), get_color("wall"))  
    # Right wall
    create_cube((ROOM_DIMS[0], ROOM_DIMS[1] / 2, ROOM_DIMS[2] / 2), 
                (0.1,          ROOM_DIMS[1],     ROOM_DIMS[2]), get_color("wall"))  

    # Create ceiling
    create_cube((ROOM_DIMS[0] / 2, ROOM_DIMS[1] / 2, ROOM_DIMS[2]), 
                (ROOM_DIMS[0],     ROOM_DIMS[1], 0.1), get_color("ceiling"))

(fill_room)

# Raw is important so the segmentation map has the intended colors
bpy.context.scene.view_settings.view_transform = 'Raw'

bpy.context.scene.render.resolution_x = 1024
bpy.context.scene.render.resolution_y = 768

# Clear existing objects
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Prepare camera
cam = bpy.data.cameras.new("Camera 1")
cam.lens = 30
cam_obj = bpy.data.objects.new("Camera 1", cam)
scn = bpy.context.scene
scn.collection.objects.link(cam_obj)

cam_obj.location = (1, 1, 3.5)
direction = mathutils.Vector((5 - 1, 5 - 1, 0.5 - 3.5))
rot_quat = direction.to_track_quat('-Z', 'Y')
cam_obj.rotation_euler = rot_quat.to_euler()

create_room()
fill_room()