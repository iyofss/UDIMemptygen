# pip install Pillow
from PIL import Image
# pip install tkinter
from tkinter import filedialog as fd


# folder selector:
filename = fd.askdirectory()
print('path selected: ' + filename)


def imageMaker(turns, name, imgRes):
    count = 1
    while int(turns) >= count:

        # UDIM naming
        if count < 1000:
            naming = name + '.1' + str(f'{count:03}') + '.png'

        elif count >= 1000:
            naming= name + '.' + str(f'{count:04}') + '.png'
        count = count + 1

        # UDIM saving
        img  = Image.new( mode = "RGB", size = (int(imgRes), int(imgRes)), color = (0, 0, 0) )
        img.save(filename + '/' + naming, 'png')


# this will run the the function above
imageMaker(input('how many turns? '), input('what name? '), input('what res? '))
