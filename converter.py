from PIL import Image
import numpy as np
from time import sleep, perf_counter
from sys import exit
#image = Image.open("Green-Wallpaper-36-640x360.jpg")  # the image to use
starttime = perf_counter()

filename = "Tree.jpeg"
image = Image.open(filename)
greyscale = Image.open(filename).convert('L')
img_width = image.size[0]  # the width and height of the input image
img_height = image.size[1]
height_map = [[0] * (img_height + 2)]  # Initialize the first row with 0s
print()

for pix_x in range(img_width):
    row = [0]  # Start with a 0 for the left edge
    for pix_y in range(img_height):
        luminance = 0.21 * image.getpixel((pix_x, pix_y))[0] + 0.72 * image.getpixel((pix_x, pix_y))[1] + 0.07 * image.getpixel((pix_x, pix_y))[2]
        brightness = greyscale.getpixel((pix_x, pix_y))
        if brightness>100:
                row.append(2)
        elif brightness>3:
                row.append(3)
        else:
                row.append(4)
    row.append(0)  # Add 0 for the right edge
    height_map.append(row)

height_map.append([0] * (img_height + 2))  # Add the last row with 0s





import trimesh

trimesh.util.attach_to_log()
print(len(height_map))

base_thickness = 1

vertecies = []
faces = []

counter = 0
for x in range(len(height_map)):
    print(f'x is {x}, len(height_map) is {len(height_map)}')
    print(f'Progress with adding vertecies: {x*100//len(height_map)}%')
    for y in range(len(height_map[x])):
        vertecies.append([x, y, height_map[x][y]]) 
        if (x != len(height_map)-1) and (y != len(height_map[x])-1):
            faces.append([counter, counter+1, counter+len(height_map[x])+1])
            faces.append([counter, counter+len(height_map[y]), counter+len(height_map[x])+1])
            print(counter)

        counter += 1 
# base_width = len(height_map[0])   #define the size of the base
# base_length = len(height_map)
# vertecies.append([0,0 -base_thickness])   #add four vertecies for the base
# vertecies.append([0,len(height_map[0])-1,-base_thickness])
# vertecies.append([len(height_map)-1,0,-base_thickness])
# vertecies.append([len(height_map)-1,len(height_map[0])-1,-base_thickness])

faces.append([0, len(height_map[x])-1, len(vertecies)-1])
faces.append([0, len(vertecies)-(len(height_map[x])), len(vertecies)-1])



mesh = trimesh.Trimesh(vertecies, faces)
mesh.export('final.stl')


endtime = perf_counter()
print(f'hat {endtime-starttime} gedauert')