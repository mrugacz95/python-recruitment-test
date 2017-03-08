from __future__ import print_function
import glob
import re
import numpy as np
from skimage import color
from skimage import io


def categoryColor(color):
    h = color[0]
    s = color[1]
    v = color[2]
    if s < 0.5:
        if v < 0.5:
            return 0
        else:
            return 1
    return int(round(h * 6)) % 6 + 2


def findDominantColor(image):
    if image.shape[2] > 3:  # remove alpha
        image = image[:, :, :3]
    image = color.rgb2hsv(image)
    colors = ("black", "white", "red", "yellow", "green", "cyan", "blue", "magenta")
    image = np.array(image)
    col = np.zeros(8)
    image = np.reshape(image, (np.product(image.shape[0:2]), 3))
    for c in image:
        col[categoryColor(c)] += 1
    return colors[np.argmax(col)]


def main():
    for file in glob.glob("./*.png"):
        image = io.imread(file)
        print("File " + file)
        domainColor = findDominantColor(image)
        print("Dominant color: " + domainColor)
        if re.search(domainColor, file, re.IGNORECASE):
            print("OK")
        else:
            print("ERROR")
        print("\n", end='')


if __name__ == '__main__':
    main()
