from bisect import bisect_right

def pairwise(l):
    """Return subsequent pairs of items from a list l, e.g. return
    (l[0], l[1]), then (l[2], l[3]), and so on.
    """
    i = iter(l)
    return zip(i, i)

def interpolate(edge, x):
    """Given a sorted edge ((x1, y1), (x2, y2)) and an x value x,
    return a vertex (x, y') where y' is on the given edge.
    """
    t = (x - edge[0][0]) / (edge[1][0] - edge[0][0])
    y_prime = edge[0][1] + t * (edge[1][1] - edge[0][1])
    return x, y_prime

def multipolygon2quadlist(edges):
    """Function that converts a multipolygon, potentially
    with holes in it, to a list of quadrilaterals that render
    to the equivalent shape.

    Args:
        edges: A list of pairs of pairs of (x, y) coordinates.

    Returns:
        A list of 4-element lists of (x, y) coordinates.
    """

    # Make a sorted list of all unique x-coordinates of all vertices
    X = sorted({ e[0][0] for e in edges })

    # This will become a list of edge fragments that together describe the
    # same polygon.
    fragments = []

    # We create this list by making a vertical cut through all the edges at
    # each vertex in the original polygon. So all edges above or below each
    # vertex are cut at that x-coordinate.
    for edge in edges:
        if edge[1] < edge[0]:
            edge = (edge[1], edge[0])

        prev_vertex = edge[0]

        # find the first x in X that is past the left vertex of edge
        xi = bisect_right(X, edge[0][0])
        if xi < len(X):
            x = X[xi]
        else:
            x = edge[1][0] + 1

        # if x is within the x range of edge
        if x < edge[1][0]:
            while x <= edge[1][0]:
                fragments.append((prev_vertex, interpolate(edge, x)))
                prev_vertex = interpolate(edge, x)
                # find the next larger x, could keep index and just increment
                xi = bisect_right(X, x)
                if xi < len(X):
                    x = X[xi]
                else:
                    x = edge[1][0] + 1
        else:
            # Copy the whole edge if it doesn't need to be split, but only
            # if it's not vertical or zero-length.
            if edge[0][0] < edge[1][0]:
                fragments.append(edge)

    # At this point:
    # - Each edge in fragments has edge[0].x < edge[1].x
    # - None of the edges in fragments intersect
    # - Each edge in fragments starts and ends on subsequent x-coordinates
    #   in X

    result = []
    for x in X:
        # find all edge fragments spanning this column
        column_fragments = [ f for f in fragments if f[0][0] == x ]
        # sort all edge fragments spanning this column bottom to top
        col_frags_sorted = sorted(column_fragments, key = lambda edge: (edge[0][1], edge[1][1]))
        assert(len(col_frags_sorted) % 2 == 0)
        # make a quad from each subsequent pair of spanning edges
        for bottom_frag, top_frag in pairwise(col_frags_sorted):
            result.append((bottom_frag[0], bottom_frag[1], top_frag[1], top_frag[0]))

    return result
