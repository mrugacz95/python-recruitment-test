import glob
from typing import Tuple
import re
import cv2
import numpy as np


def categoryColor(color: Tuple):
    h = color[0] / 255
    s = color[1] / 255
    v = color[2] / 255
    if s < 0.5:
        if v < 0.5:
            return 0
        else:
            return 1
    val = int(round(h * 6)) % 6 + 2
    return val

def findDominantColor(image: np.ndarray) -> str:
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV_FULL)
    colors = ("black", "white", "red", "yellow", "green", "cyan", "blue", "magenta")
    col = np.zeros(8)
    image = np.reshape(image, (np.product(image.shape[0:2]), 3))
    for color in image:
        col[categoryColor(color)] += 1
    return colors[np.argmax(col)]


def main():
    for file in glob.glob("./*.png"):
        image = cv2.imread(file)
        print("File " + file)
        domainColor = findDominantColor(image)
        print("Dominant color: " + domainColor)
        if re.search(domainColor, file, re.IGNORECASE):
            print("OK")
        print("\n",end="")


if __name__ == '__main__':
    main()
