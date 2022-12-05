from PIL import Image
import os


def imgProcessing():
    path = "images"
    testing = "testing/"
    with os.scandir(path) as imagesDirectory:
        for entry in imagesDirectory:
            # Shows files which don't start with a point and
            # are indeed files
            if not entry.name.startswith('.') and entry.is_file():
                imgName = entry.name
                img = Image.open(path + '/' + imgName)
                img.convert('RGB').rotate(90).resize((128, 128)).save(testing+imgName + ".jpeg")

    imagesDirectory.close()


def main():
    imgProcessing()


main()
