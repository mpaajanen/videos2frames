import imageio.v3 as iio
from pathlib import Path
from PIL import Image
from PIL import ImageOps

videopath = "./kaarina"
videos = list()

FPS = 15
CUTOFF = 360

for file in Path(videopath).iterdir():
    if not file.is_file():
        continue
    
    for i, frame in enumerate(iio.imiter(file)):
        if (i%120==0):
            framepath = f"./frames_kaarina/{file.stem}_{i}.png"
            iio.imwrite(framepath, frame, extension=".png")
        if (i==CUTOFF):
            break