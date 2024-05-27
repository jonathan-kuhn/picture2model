from PIL import Image
import numpy as np
from time import sleep, perf_counter
#image = Image.open("Green-Wallpaper-36-640x360.jpg")  # the image to use
starttime = perf_counter()

filename = "Hannah(2).jpeg"
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

for x in range(len(height_map)):
    print(f'Progress with adding vertecies: {x*100//len(height_map)}%')
    for y in range(len(height_map[x])):
        vertecies.append([x, y, height_map[x][y]])

# base_width = len(height_map[0])   #define the size of the base
# base_length = len(height_map)
# vertecies.append([0,0 -base_thickness])   #add four vertecies for the base
# vertecies.append([0,len(height_map[0])-1,-base_thickness])
# vertecies.append([len(height_map)-1,0,-base_thickness])
# vertecies.append([len(height_map)-1,len(height_map[0])-1,-base_thickness])

def add_Faces(a):
    for b in range(len(height_map[a])-1):
        counter = vertecies.index([a, b, height_map[a][b]])
        faces.append([counter, counter+1, counter+len(height_map[a])+1])
        faces.append([counter, counter+len(height_map[a]), counter+len(height_map[x])+1])
        
for a in range(len(height_map)-1):
    print(f'Progress with adding faces: {a*100//(len(height_map)-1)}%')
    add_Faces(a)


faces.append([0, len(height_map[a])-1, len(vertecies)-1])
faces.append([0, len(vertecies)-(len(height_map[a])), len(vertecies)-1])



mesh = trimesh.Trimesh(vertecies, faces)
mesh.export('final.stl')


endtime = perf_counter()
print(f'hat {endtime-starttime} gedauert')