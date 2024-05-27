import trimesh
trimesh.util.attach_to_log()

height_map = [
    [0, 3, 0, 2, 0],
    [0, 1, 2, 1, 0],
    [0, 2, 3, 2, 0],
    [0, 1, 2, 1, 0],
    [0, 0, 0, 0, 0]
]
print(len(height_map))
vertices = []
print(enumerate(height_map))
for row, y in enumerate(height_map):
    print(row)
    print(y)
    for col, z in enumerate(y):
        vertices.append([row, col, z])

faces = []
for row in range(len(height_map) - 1):
    for col in range(len(height_map[0]) - 1):
        v1 = row * len(height_map[0]) + col
        v2 = v1 + 1
        v3 = v1 + len(height_map[0])
        v4 = v3 + 1
        faces.append([v1, v3, v2])
        faces.append([v2, v3, v4])

mesh = trimesh.Trimesh(vertices=vertices, faces=faces)
mesh.export('model.stl')

# print(enumerate(height_map))
# for row, y in enumerate(height_map):
#     print(row)
#     print(y)
#     for col, z in enumerate(y):
#         vertices.append([row, col, z])

# faces = []
# for row in range(len(height_map)-1):
#     for col in range(len(height_map[0])-1):
#         v1 = row * len(height_map[0]) + col
#         v2 = v1 + 1
#         v3 = v1 + len(height_map[0])
#         v4 = v3 + 1
#         faces.append([v1, v3, v2])
#         faces.append([v2, v3, v4])

# mesh = trimesh.Trimesh(vertices=vertices, faces=faces)

# mesh.export('model.stl')





# Add faces for the base
# faces.append([(len(vertices)-1),(len(vertices)-2),(len(vertices)-4)])
# faces.append([(len(vertices)-1),(len(vertices)-3),(len(vertices)-4)])


#add faces connecting the base vertices with the vertices of the model
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