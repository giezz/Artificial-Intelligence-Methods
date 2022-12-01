from PIL import Image, ImageEnhance

img = Image.open("1.png")
img.show()
enhancer = ImageEnhance.Brightness(img)
img = enhancer.enhance(1.2)
img.show()
