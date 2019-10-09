import math


def to_rgb(hex):
    """Takes a RRGGBB string and outputs adecimal RGB tuple"""
    return [int(hex[i:i+2], 16) for i in range(0, len(hex), 2)]


def get_brightness((r, g, b)):
    """Gets the brightness value of a RGB color"""
    return math.sqrt(0.299 * r ^ 2 + 0.587 * g ^ 2 + 0.114 * b ^ 2)


def contrast_color(color):
    """Returns white or black, to contrast with a given color"""
    return (0, 0, 0) if get_brightness(color) > 0.5 else (255, 255, 255)
