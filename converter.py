
import trimesh
import numpy as np
trimesh.util.attach_to_log()
height_map = []
print(len(height_map))

base_thickness = 1

vertices = []
faces = []

for x in range(len(height_map)):
    for y in range(len(height_map[x])):
        vertices.append([x, y, height_map[x][y]])

# base_width = len(height_map[0])   #define the size of the base
# base_length = len(height_map)
# vertices.append([0,0 -base_thickness])   #add four vertices for the base
# vertices.append([0,len(height_map[0])-1,-base_thickness])
# vertices.append([len(height_map)-1,0,-base_thickness])
# vertices.append([len(height_map)-1,len(height_map[0])-1,-base_thickness])

print(vertices)

counter = 0
for a in range(len(height_map)-1):
    print(a)
    for b in range(len(height_map[a])-1):
        counter = vertices.index([a, b, height_map[a][b]])
        faces.append([counter, counter+1, counter+len(height_map[a])+1])
        faces.append([counter, counter+len(height_map[a]), counter+len(height_map[x])+1])
faces.append([0, len(height_map[a])-1, len(vertices)-1])
faces.append([0, len(vertices)-(len(height_map[a])), len(vertices)-1])

# Add faces for the base
# faces.append([(len(vertices)-1),(len(vertices)-2),(len(vertices)-4)])
# faces.append([(len(vertices)-1),(len(vertices)-3),(len(vertices)-4)])


#add faces connecting the base vertices with the vertices of the model
print(vertices)
# for i in range(len(vertices)-1, len(vertices)-5, -1):
#     if i%2 == 0:
#         i_and_height = vertices.index([vertices[i][0], vertices[i][1], vertices[i][2]+base_thickness])
#         i_and_height_and_y = vertices.index([vertices[i][0], vertices[i][1]+len(height_map), vertices[i][2]+base_thickness])
#         i_and_y = vertices.index([vertices[i][0],vertices[i][1]+len(height_map),vertices[i][2]])
#         faces.append([i, i_and_height, i_and_height_and_y])
#         faces.append([i, i_and_y, i_and_height_and_y])
#     else:
#         print(f'vertices[i] is {vertices[i]}')
#         i_and_height = vertices.index([vertices[i][0], vertices[i][1], vertices[i][2]+base_thickness])
#         i_and_height_and_x = vertices.index([vertices[i][0]+len(height_map[0]), vertices[i][1], vertices[i][2]+base_thickness])
#         i_and_x = vertices.index([vertices[i][0]+len(height_map[0]), vertices[i][1], vertices[i][2]])
#         faces.append([i, i_and_height, i_and_height_and_x])
#         faces.append([i, i_and_x, i_and_height_and_x])


mesh = trimesh.Trimesh(vertices=vertices, faces=faces)
mesh.export('model2.stl')
