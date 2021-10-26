
from text_gen import *
from PIL import Image, ImageFont, ImageDraw 
# title_text = "The Beauty of Nature"
# my_image = Image.open("nature.jpg")
    # title_font = ImageFont.truetype('playfair/playfair-font.ttf', 200)
    # image_editable.text((15,15), title_text, (237, 230, 211), font=title_font)
    # image_editable = ImageDraw.Draw(my_image)
    # my_image.save("result.jpg")
import os

while True:
    sleep(1)
    img = Image.new('RGB', (1920, 1080), color = (0, 0, 0))
    text = getText()
    draw = ImageDraw.Draw(img)
    fnt = ImageFont.truetype('./times.ttf', 150)
    draw.text((1000,100), text, font=fnt, fill=(255, 255, 0))
    img.save('result.png')
    os.system("/bin/feh --bg-fill /home/ls/dynamic-wallpaper/result.png")





 
 
 