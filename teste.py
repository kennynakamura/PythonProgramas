from Pillow import Image
import glob
image_list = []
#for filename in glob.glob('CAMISA.png'): #assuming gif
im=Image.open("CAMISA.png")
image_list.append(im)
for im in image_list:
    im.rotate(180).resize((640, 480)).save("flipped_and_resized.jpeg")
