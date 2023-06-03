import sys

print("LM Prompt:\n")
with open("chatgpt-prompt.txt") as f:
    prompt = f.readlines()
    prompt = [line.replace("(PROMPT)", sys.argv[1]) for line in prompt]
    print("".join(prompt))

print("\nSD Prompt:\n")
SD_PROMPT = ("colorful accents, cozy and calm, fabrics and textiles, "
             "wall decorations, interior photo, atmospheric, detailed, "
             "realistic lighting, sunlight, reflections, award winning "
             "contemporary interior design, waite, award - winning photograph, "
             "canon eos 5 d mark iv, fujifilm x - t 4")
print(sys.argv[1] + ", " + SD_PROMPT)