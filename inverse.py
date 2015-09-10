from PIL import Image
import PIL.ImageOps    

image = Image.open('test1_thinned.jpg')

inverted_image = PIL.ImageOps.invert(image)

inverted_image.save('new_name.png')