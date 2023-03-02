import imageio.v3 as iio
from pathlib import Path
from PIL import Image
from PIL import ImageOps

videopath = "./videos"
videos = list()

for file in Path(videopath).iterdir():
    if not file.is_file():
        continue
    
    for i, frame in enumerate(iio.imiter(file)):
        framepath = f"./frames/{file.stem}_{i}.png"
        iio.imwrite(framepath, frame, extension=".png")
        if (i==10):
            break