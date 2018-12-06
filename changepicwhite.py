from PIL import Image

imagepath = '/Users/huangjiewen/photo/after.png'
outputimg = '/Users/huangjiewen/photo/after.jpg'


def execute(srcImage, color):
    (r1, g1, b1) = color
    width = srcImage.size[0]
    height = srcImage.size[1]
    pixelSrc = srcImage.load()
    newImg = Image.new('RGB', srcImage.size)
    pixelOut = newImg.load()
    for x in range(0, width):
        for y in range(0, height):
            (r, g, b) = pixelSrc[x, y]
            if r > r1:
                r = r1
            if g > g1:
                g = g1
            if b > b1:
                b = b1
            pixelOut[x, y]= (r, g, b)
    newImg.save(outputimg)


if __name__ == '__main__':
    color = (227, 224, 216)
    with Image.open(imagepath) as img:
        if img.mode != 'RGB':
            img = img.convert('RGB')
        execute(img, color)
