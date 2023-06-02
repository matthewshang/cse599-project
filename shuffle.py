import random
import shutil

# This code was used to prepare the human eval.
# The shuffled images can be found in eval-data, and the labels are in shuffle.txt.
for i in range(1, 15 + 1):
    f_lm = f"lm-outputs/{i:02}-lm.png"
    f_sd = f"sd-outputs/{i:02}-sd.png"
    if random.randint(0, 1) == 0:
        shutil.copyfile(f_lm, f"eval-data/{i:02}-a.png")
        shutil.copyfile(f_sd, f"eval-data/{i:02}-b.png")
        print("F")
    else:
        shutil.copyfile(f_lm, f"eval-data/{i:02}-b.png")
        shutil.copyfile(f_sd, f"eval-data/{i:02}-a.png")
        print("T")