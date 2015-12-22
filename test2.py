from PIL import Image, ImageChops

point_table = ([0] + ([255] * 255))

def black_or_b(a, b):
    diff = ImageChops.difference(a, b)
    diff = diff.convert('L')
    # diff = diff.point(point_table)
    # new = diff.convert('RGB')
    # new.paste(b, mask=diff)
    print diff
    return diff
def PixelCompare(im1, im2, mode = "pct", alpha = .01):
    if im1.size == im2.size and im1.mode == im2.mode:
        randPix = int(im1.getpixel((0,0)))
        # print len(randPix)
        maxSum = []
        diff = []
        for channel in range((randPix)):
            diff += [0.0]
            maxSum += [0.0]
        width = im1.size[0]
        height = im1.size[1]
        for i in range(width):
            for j in range(height):
                pixel1 = im1.getpixel((i,j))
                pixel2 = im2.getpixel((i,j))
                for channel in range((randPix)):
                    maxSum[channel] += 255
                    diff[channel] += abs(pixel1 - pixel2)
        if mode == "pct":
            ret = ()
            for channel in range((randPix)):
                ret += (diff[channel]/maxSum[channel],)
            return ret
        for channel in range((randPix)):
            if diff[channel] > alpha*maxSum[channel]:
                return False
        return True
    return False
a = Image.open('cover_image.bmp')
b = Image.open('cover_image.bmp')
c = PixelCompare(a,b)
print c
# c.save('c.png')