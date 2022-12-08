#!/usr/bin/env python3

from PIL import Image
import os


def imgProcessing():
    path = "~/supplier-data/images"
    with os.scandir(path) as imagesDirectory:
        for entry in imagesDirectory:
            if not entry.name.startswith('.') and entry.is_file():
                imgName = entry.name
                if imgName not in ['README', 'LICENSE']:
                    img = Image.open(path + '/' + imgName)
                    img.convert('RGB').resize((600, 400)).save(path + '/' + imgName[:3] + ".jpeg")

    imagesDirectory.close()


def main():
    imgProcessing()


main()