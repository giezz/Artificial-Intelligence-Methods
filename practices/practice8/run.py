from PIL import Image, ImageFilter

img = Image.open("1.png")
img.show()
img.filter(ImageFilter.BLUR).show()
