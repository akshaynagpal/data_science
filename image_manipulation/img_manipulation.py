import PIL
from PIL import Image

"""
#resizing the image to 32 X 32 pixels
img = Image.open('one.png')
img = img.resize((32,32),PIL.Image.ANTIALIAS)
img.save('one_2.png')
"""

img = Image.open('one_2.png')

x = list(img.getdata())
for k in x:
        print k
fo = open('one.txt',"w")

for i in range(32):
	for j in range(32):	
		if x[32*i+j] == (0, 0, 0, 0):
			fo.write('0')
		else:
			fo.write('1')
	fo.write('\n')
fo.close()

