import sys

with open("script.py") as f:
    prompt = f.readlines()
    prompt = [line.replace("(fill_room)", sys.argv[1]) for line in prompt]
    print("".join(prompt))