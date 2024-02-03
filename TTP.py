from PIL import Image,ImageFont,ImageDraw
import os
from PIL import Image,ImageFont,ImageDraw
import pandas as pd
import numpy as np
def TTP(txt, path, length=600, width=100,font_size=14):
    im = Image.new("RGB", (length, width), (255, 255, 255))
    dr = ImageDraw.Draw(im)
    font = ImageFont.truetype(os.path.join("fonts", "kaiu.ttf"), font_size)
    dr.text((10, 5), txt, font=font, fill="#000000")
    #im.show()
    im.save(path)
    return
def OE(path, SheetName=None, cols=None):
    df=pd.read_excel(path, sheet_name=SheetName, usecols=[cols])
    return df.values.T