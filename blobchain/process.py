import subprocess
import os
import color
from PIL import Image, ImageFont, ImageDraw, ImageEnhance


def get_text():
    """Retrieves some text to put on the image"""
    # Gets the current commit info in "hash name -- subject" format
    cmd = ['git', 'show', '--no-patch', '--format=format:%p']
    # Get the second parent hash, and hope like hell that's the correct on
    parents = subprocess.check_output(cmd).decode('ascii').strip().split(' ')

    if len(parents) > 1:
        # Feed the second parent into a richer info command
        cmd = ['git', 'show', '--no-patch', '--format=format:%h %aN -- %s', parents[1]]
    else:
        # If there's only one parent, this isn't a merge, so just grab info for this commit
        cmd = ['git', 'show', '--no-patch', '--format=format:%h %aN -- %s']
    return subprocess.check_output(cmd).decode('ascii').strip()



def get_current_commit():
    """Returns the current commit hash (in short form)"""
    return subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).decode('ascii').strip()


def process(old_path, new_path):
    """
    Reads an image file at old_path, processes it, and outputs it at new_path
    The only requirement is that we get an image at the end
    """
    # Open the image, and make sure it's in RGB color
    im = Image.open(old_path).convert('RGB')
    width, height = im.size
    margin = 30

    # Convert the current hash to a color (they're both 6 char hex strings!)
    bg_color = color.to_rgb(get_current_commit())
    text_color = color.contrast_color(color)

    # Create a new image that's RGB, the same size, and has a (R, G, B) background
    out = Image.new('RGB', (width, height), bg_color)

    # Grab the entire old image as a region
    region = im.crop((0, 0, width, height))
    # Shrink it a little
    region = region.resize((width - margin * 2, height - margin * 2))
    # Stick it in the middle of the new image, shifted by the margins
    out.paste(region, (margin, margin))

    # Load the Roboto Mono font
    fnt = ImageFont.truetype(os.getcwd() + '/blobchain/RobotoMono-Medium.ttf', 28)
    # Get a drawing context for the new image
    draw = ImageDraw.Draw(out)
    txt = get_text()
    draw.text((10, height - 33), txt, font=fnt, fill=text_color)

    # Hashes the commit id, and uses that to adjust the contrast
    commit_hash = int(txt.split(" ")[0], 16)
    contrast = ImageEnhance.Contrast(out)
    out = contrast.enhance((commit_hash % 300) / 100 + 0.75)

    # Saves the new image to the output path
    out.save(new_path)
