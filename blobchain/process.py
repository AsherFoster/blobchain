import subprocess
import os
from PIL import Image, ImageFont, ImageDraw, ImageEnhance

margin = 30


def get_text():
    cmd = ['git', 'show', '--no-patch', '--format=format:%h %aN -- %s']
    return subprocess.check_output(cmd).decode('ascii').strip()


# This is the fun part
# It's called with two paths, and it's only requirement is to output a valid image at new_path
def process(old_path, new_path):
    im = Image.open(old_path).convert('RGB')
    width, height = im.size

    out = Image.new('RGB', (width, height), (239, 97, 145))

    region = im.crop((0, 0, width, height))
    region = region.resize((width - margin * 2, height - margin * 2))
    out.paste(region, (margin, margin))

    fnt = ImageFont.truetype(os.getcwd() + '/blobchain/RobotoMono-Medium.ttf', 28)

    draw = ImageDraw.Draw(out)
    txt = get_text()
    print('Drawing: ' + txt)
    draw.text((10, height - 33), txt, font=fnt, fill=(0, 0, 0))

    commit_hash = int(txt.split(" ")[0], 16)
    contrast = ImageEnhance.Contrast(out)
    out = contrast.enhance((commit_hash % 300) / 100 + 0.75)

    out.save(new_path)
