
from text_gen import *
from PIL import Image, ImageFont, ImageDraw 
# title_text = "The Beauty of Nature"
# my_image = Image.open("nature.jpg")
    # title_font = ImageFont.truetype('playfair/playfair-font.ttf', 200)
    # image_editable.text((15,15), title_text, (237, 230, 211), font=title_font)
    # image_editable = ImageDraw.Draw(my_image)
    # my_image.save("result.jpg")
import os
pwd = '/home/ls/dynamic-wallpaper'
x = 0
text_new =""
seconds = 60
while True:
    img = Image.new('RGB', (1920, 1080), color = (0, 0, 0))
    text = getText()
    draw = ImageDraw.Draw(img)
    fnt = ImageFont.truetype(f'{pwd}/times.ttf', 150)
    draw.text((500,100), text, font=fnt, fill=(60, 168, 50))
    if x > 160 or x == 0:
        x = 0
        text_new = getLastfewHours(False)
        text_new += get_manictime_last_x_days(1)

    fnt = ImageFont.truetype(f'{pwd}/times.ttf', 15)
    draw.text((1500,300), text_new, font=fnt, fill=(60, 168, 50))

    x = x + seconds
    img.save(f'{pwd}/result.png')
    os.system(f"/bin/feh --bg-fill {pwd}/result.png")
    sleep(seconds)





 
 
 