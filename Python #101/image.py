from PIL import Image
from PIL import ImageFilter

def main():
    with Image.open("cat1.gif") as img:
        print(img.format)
        img = img.rotate(90)
        # img = img.filter(ImageFilter.FIND_EDGES)
        # the code above is to apply a filter to the image
        img.save("cat3.gif")

main()
