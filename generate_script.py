import os
import openai
import sys

openai.api_key = os.getenv("OPENAI_API_KEY")

SYSTEM_PROMPT = """
You are an expert interior designer, 3D artist, and programmer. 
"""

SCENE_PROMPT_TEMPLATE = """
I want to create a full 3D scene representing a {scene}. 
The scene should be inside a bounding box with one corner at (0, 0, 0) 
and the other corner at (10, 15, 5). 
Note that the z-axis is the upwards direction.

First, think about what objects should appear in the room, 
where they should be located, and what size they should be. 
Think of as many objects that might be in the room as you can. 
Make sure the objects are separated and also close enough to be realistic.

Next, write a function called fill_room() to generate the scene in Blender 
from the Python API. You do not need to create the walls, ceiling, or floor. 
You also have access to the following functions: 
create_cube(location, scale, color), 
create_sphere(location, radius, color), 
get_color(object_name). 
For example, to get the wall color, you would use get_color("wall").
End the function with a comment saying "END fill_room".
"""

scene = "classroom" if len(sys.argv) == 1 else sys.argv[1]

prompt = SCENE_PROMPT_TEMPLATE.format(scene=scene)

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": prompt}
    ]
)

content = response.choices[0].message.content
fill_room_begin = content.find("def fill_room")
fill_room_end = content.rfind("# END fill_room")

fill_room_impl = content[fill_room_begin:fill_room_end]

with open("blender_template.py", "r") as f:
    blender_template = f.read()

blender_script = blender_template.replace("# fill_room stub", fill_room_impl)
print(blender_script)

# blender -noaudio --background --python blender_script.py