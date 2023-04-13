import imageio.v3 as iio
from pathlib import Path
from PIL import Image
from PIL import ImageOps

videopath = "./testi-vp60"
videos = list()

#FPS = 15

START = 30
CUTOFF = 360
FREQUENCY = 5

for file in Path(videopath).iterdir():
    if not file.is_file():
        continue
    
    for i, frame in enumerate(iio.imiter(file)):
        if (i>START and i%FREQUENCY==0):
            framepath = f"./frames_testi/{file.stem}_{i}.png"
            iio.imwrite(framepath, frame, extension=".png")
        if (i==CUTOFF):
            break