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