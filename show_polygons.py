from polygon_hasher import multipolygon2quadlist

import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

square = [((-1,-1),(2,-1)), ((2,-1),(2,2)), ((2,2),(-1,2)), ((-1,2),(-1,-1))]
square_quads = multipolygon2quadlist(square)
print('Square:')
print(square_quads)

triangle = [((0,0),(1,0)), ((1,0),(0.5,1)), ((0.5,1),(0,0))]
triangle_quads = multipolygon2quadlist(triangle)
print('Triangle:')
print(triangle_quads)

triangle_in_square = square + triangle
tis_quads = multipolygon2quadlist(triangle_in_square)
print('Triangular hole in square:')
print(tis_quads)

weird_outer = [
    ((20,20),(20,24)),
    ((20,24),(30,27)),
    ((30,27),(36,30)),
    ((36,30),(38,35)),
    ((38,35),(35,40)),
    ((35,40),(30,50)),
    ((30,50),(34,54)),
    ((34,54),(56,64)),
    ((56,64),(68,60)),
    ((68,60),(64,50)),
    ((64,50),(52,48)),
    ((52,48),(50,36)),
    ((50,36),(61,31)),
    ((61,31),(80,34)),
    ((80,34),(88,30)),
    ((88,30),(85,20)),
    ((85,20),(80,18)),
    ((80,18),(67,22)),
    ((67,22),(71,10)),
    ((71,10),(66,6)),
    ((66,6),(50,19)),
    ((50,19),(40,16)),
    ((40,16),(30,12)),
    ((30,12),(23,14)),
    ((23,14),(20,20))
    ]

weird_hole1 = [
    ((74,24),(74,30)),
    ((74,30),(81,31)),
    ((81,31),(79,25)),
    ((79,25),(74,24))
    ]

weird_hole2 = [
    ((26,20),(30,24)),
    ((30,24),(42,26)),
    ((42,26),(42,34)),
    ((42,34),(36,46)),
    ((36,46),(40,49)),
    ((40,49),(45,46)),
    ((45,46),(50,30)),
    ((50,30),(50,24)),
    ((50,24),(33,16)),
    ((33,16),(27,16)),
    ((27,16),(26,20))
    ]

weird = weird_outer + weird_hole1 + weird_hole2
weird_quads = multipolygon2quadlist(weird)
print('Weird irregular shape')
print(weird_quads)

# Plot all hashed polygons
fig1 = plt.figure()

axes_square = fig1.add_subplot(131)
for quad in square_quads:
    path = Path(quad)
    patch = patches.PathPatch(path, facecolor="red", lw=2)
    axes_square.add_patch(patch)
axes_square.set_xlim(-3, 3)
axes_square.set_ylim(-3, 3)

axes_square = fig1.add_subplot(132)
for quad in triangle_quads:
    path = Path(quad)
    patch = patches.PathPatch(path, facecolor="yellow", lw=2)
    axes_square.add_patch(patch)
axes_square.set_xlim(-3, 3)
axes_square.set_ylim(-3, 3)

axes_square = fig1.add_subplot(133)
for quad in tis_quads:
    path = Path(quad)
    patch = patches.PathPatch(path, facecolor="cyan", lw=2)
    axes_square.add_patch(patch)
axes_square.set_xlim(-3, 3)
axes_square.set_ylim(-3, 3)

fig2 = plt.figure()
axes = fig2.add_subplot(111)
for quad in weird_quads:
    path = Path(quad)
    patch = patches.PathPatch(path, facecolor="green", lw=2)
    axes.add_patch(patch)
axes.set_xlim(0, 100)
axes.set_ylim(0, 100)

plt.show()

