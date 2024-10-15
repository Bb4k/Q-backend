# Python3 program to implement traveling salesman
# problem using naive approach.
import os
import sys
from sys import maxsize
from itertools import permutations
from collections import deque
import cv2
from PIL import Image
import base64
from django.core.files import File

# Below lists detail all four possible movements from a cell
row = [-1, 0, 0, 1]
col = [0, -1, 1, 0]
module_dir = os.path.dirname(__file__)
alb = cv2.imread(os.path.join(module_dir, 'assets', "puzzle", "alb.png"))
gri = cv2.imread(os.path.join(module_dir, 'assets', "puzzle", "gri.png"))
rosu = cv2.imread(os.path.join(module_dir, 'assets', "puzzle", "rosu.png"))
verde = cv2.imread(os.path.join(module_dir, 'assets', "puzzle", "verde.png"))


# implementation of traveling Salesman Problem
def travelling_salesman_problem(graph, s):
    # store all vertex apart from source vertex
    vertex = []
    order = None
    for i in range(len(graph)):
        # if i != s:
        vertex.append(i)

    # store minimum weight Hamiltonian Cycle
    min_path = maxsize
    next_permutation = permutations(vertex)

    for i in next_permutation:
        # store current Path weight(cost)
        current_pathweight = 0

        # compute current path weight
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]

        # update minimum
        if min_path >= current_pathweight:
            min_path = current_pathweight
            order = i
        else:
            if order is None:
                order = i

    return [min_path, order]


# User defined Product class
class Product:
    def __init__(self, product_id, x, y):
        self.product_id = product_id
        self.x = x
        self.y = y


# Function to check if it is possible to go to position (row, col)
# from the current position. The function returns false if row, col
# is not a valid position or has a value 0 or already visited.
def is_valid(mat, visited, row, col):
    return (row >= 0) and (row < len(mat)) and (col >= 0) and (col < len(mat[0])) \
           and mat[row][col] == 1 and not visited[row][col]


# Find the shortest possible route in a matrix `mat` from source `src` to
# destination `dest`
def find_shortest_path_length(mat, src: Product, dest: Product):
    # get source cell (i, j)
    i = src.x
    j = src.y

    # get destination cell (x, y)
    x = dest.x
    y = dest.y

    # base case: invalid input
    if not mat or len(mat) == 0 or mat[i][j] == 0 or mat[x][y] == 0:
        return -1, -1

    # `M × N` matrix
    (M, N) = (len(mat), len(mat[0]))

    # construct a matrix to keep track of visited cells
    visited = [[False for x in range(N)] for y in range(M)]

    # create an empty queue
    q = deque()

    # mark the source cell as visited and enqueue the source node
    visited[i][j] = True

    # (i, j, dist) represents matrix cell coordinates, and their
    # minimum distance from the source
    q.append((i, j, 0, []))

    # stores length of the longest path from source to destination
    min_dist = sys.maxsize

    path_to_return = []

    # loop till queue is empty
    while q:

        # dequeue front node and process it
        (i, j, dist, path) = q.popleft()

        # (i, j) represents a current cell, and `dist` stores its
        # minimum distance from the source

        # if the destination is found, update `min_dist` and stop
        if i == x and j == y:
            path_to_return = path + [(i, j)]
            min_dist = dist
            break

        # check for all four possible movements from the current cell
        # and enqueue each valid movement
        for k in range(4):
            # check if it is possible to go to position
            # (i + row[k], j + col[k]) from current position
            if is_valid(mat, visited, i + row[k], j + col[k]):
                # mark next cell as visited and enqueue it
                # print(i, j)
                visited[i + row[k]][j + col[k]] = True
                q.append((i + row[k], j + col[k], dist + 1, path + [(i + row[k], j + col[k])]))

    if min_dist != sys.maxsize:
        return min_dist, path_to_return
    else:
        return -1, -1


def read_map(file_name):
    mat = []
    module_dir = os.path.dirname(__file__)
    f = open(os.path.join(module_dir, 'maps', "map_1.txt"), "r")
    for file_line in f:
        row = []
        for char in file_line:
            if char == '-' or char == 'X':
                row.append(0)
            elif char == '1':
                row.append(1)
        mat.append(row)
    f.close()
    return mat


def read_map_for_puzzle(file_name):
    mat = []
    module_dir = os.path.dirname(__file__)
    f = open(os.path.join(module_dir, 'maps', "map_1.txt"), "r")
    # f = open(file_name, "r")
    for file_line in f:
        row = []
        for char in file_line:
            if char == '-':
                row.append(0)
            elif char == 'X':
                row.append(2)
            elif char == '1':
                row.append(1)
        mat.append(row)
    f.close()
    return mat


def puzzle(matrix):
    for i in range(0, len(matrix)):
        if matrix[i][0] == 0 or matrix[i][0] == 1:
            # drum alb
            im_h = alb
        elif matrix[i][0] == 2:
            # raft
            im_h = gri
        elif matrix[i][0] == 3:
            # drum de parcurs
            im_h = verde
        for j in range(1, len(matrix)):
            if matrix[i][j] == 4:
                # drum de parcurs
                im_h = cv2.hconcat([im_h, rosu])
                continue
            elif matrix[i][j] == 0 or matrix[i][j] == 1:
                # drum alb
                im_h = cv2.hconcat([im_h, alb])
            elif matrix[i][j] == 2:
                # raft
                im_h = cv2.hconcat([im_h, gri])
            elif matrix[i][j] == 3:
                # drum de parcurs
                im_h = cv2.hconcat([im_h, verde])
        if i == 0:
            im_v = im_h
        else:
            im_v = cv2.vconcat([im_v, im_h])

    cv2.imwrite('harta.jpeg', im_v)


def get_min_index(inputlist):
    min_value = min(inputlist)
    min_index = inputlist.index(min_value)
    return min_index


def generate_map(x_intrare, y_intrare, x_iesire, y_iesire, products: [Product]):
    # id 1 = chio
    # id 2 = doritos
    # id 3 = portocale
    # id 4 = granini
    # id 5 = almette

    # NR 1
    # intrare = Product('intrare', 15, 16)
    # iesire = Product('iesire', 78, 16)
    # products = [Product(1, 30, 78), Product(2, 70, 88),
    #             Product(3, 86, 38), Product(4, 110, 16)]

    # NR 2
    # intrare = Product('intrare', 15, 16)
    # iesire = Product('iesire', 110, 16)
    # products = [Product(1, 102, 59), Product(2, 46, 80),
    #             Product(3, 10, 64), Product(5, 11, 28)]

    # NR 3
    # intrare = Product('intrare', 15, 16)
    # iesire = Product('iesire', 110, 16)
    # products = [Product(1, 102, 59), Product(2, 54, 35),
    #             Product(3, 10, 64), Product(4, 11, 28), Product(5, 102, 42)]

    # NR 4
    # intrare = Product('intrare', 15, 16)
    # iesire = Product('iesire', 70, 100)
    # products = [Product(1, 102, 59), Product(2, 54, 35),
    #             Product(3, 10, 64), Product(4, 11, 28), Product(5, 78, 32)]
    intrare = Product('intrare', x_intrare, y_intrare)
    iesire = Product('iesire', x_iesire, y_iesire)

    mat = read_map("maps/map_1.txt")

    graph = []
    paths = []
    for i in range(0, len(products)):
        line_graph = []
        line_paths = []
        for j in range(0, len(products)):
            line_graph.append(0)
            line_paths.append(None)
        graph.append(line_graph)
        paths.append(line_paths)

    for i in range(0, len(products)):
        for j in range(i + 1, len(products)):
            path_length, path = find_shortest_path_length(mat, products[i], products[j])
            graph[i][j] = graph[j][i] = path_length
            paths[i][j] = paths[j][i] = path

    # GOOD
    # print('graph:')
    # for i in range(0, len(graph)):
    #     print(graph[i])
    # print('')
    # print('paths:')
    # for i in range(0, len(paths)):
        # print(paths[i])

    s = 0
    [length, order] = travelling_salesman_problem(graph, s)

    # print(order)

    map_for_puzzle = read_map_for_puzzle("maps/map_1.txt")

    # print('SHORTEST PATH')
    for i in range(0, len(order) - 1):
        from_product = order[i]
        to_product = order[i + 1]

        # print(from_product, to_product)
        # print(paths[from_product][to_product])

        k = 0
        for (pair_i, pair_j) in paths[from_product][to_product]:
            if k == 0 or k == len(paths[from_product][to_product]) - 1:
                map_for_puzzle[pair_i][pair_j] = 4
            else:
                map_for_puzzle[pair_i][pair_j] = 3
            k += 1

    source_distance = []
    destination_distance = []
    source_paths = []
    destination_paths = []

    products.insert(0, intrare)
    products.append(iesire)
    for j in range(0, len(products)):
        path_length, path = find_shortest_path_length(mat, products[0], products[j])
        if path_length == 0 or j == len(products) - 1:
            source_distance.append(maxsize)
        else:
            source_distance.append(path_length)
        source_paths.append(path)

    for j in range(0, len(products)):
        path_length, path = find_shortest_path_length(mat, products[len(products) - 1], products[j])
        if path_length == 0 or j == len(products) - 1:
            destination_distance.append(maxsize)
        else:
            destination_distance.append(path_length)
        destination_paths.append(path)

    sd_index = get_min_index(source_distance)
    dd_index = get_min_index(destination_distance)

    # print(source_distance, destination_distance)
    # print(sd_index, dd_index)
    # print(source_paths[sd_index], destination_paths[dd_index])

    k = 0
    for (pair_i, pair_j) in source_paths[sd_index]:
        if k == 0 or k == len(source_paths[sd_index]) - 1:
            map_for_puzzle[pair_i][pair_j] = 4
        else:
            map_for_puzzle[pair_i][pair_j] = 3
        k += 1

    k = 0
    for (pair_i, pair_j) in destination_paths[dd_index]:
        if k == 0 or k == len(destination_paths[dd_index]) - 1:
            map_for_puzzle[pair_i][pair_j] = 4
        else:
            map_for_puzzle[pair_i][pair_j] = 3
        k += 1

    puzzle(map_for_puzzle)

    puzzle_image = Image.open('harta.jpeg')
    for product in products:
        # img_to_add = Image.open('assets/products/%s.jpeg' % product.product_id)
        img_to_add = Image.open(os.path.join(module_dir, 'assets', "products", str(product.product_id) + ".jpeg"))
        img_to_add = img_to_add.resize((50, 50))
        puzzle_image.paste(img_to_add, ((product.y - 2) * 10, (product.x - 2) * 10))

    puzzle_image.save('harta.jpeg')

    with open('harta.jpeg', 'rb') as image2string:
        converted_string = base64.b64encode(image2string.read())
        return converted_string.decode("utf-8")


if __name__ == "__main__":
    # [Product(1, 30, 78), Product(2, 70, 88), Product(3, 86, 38), Product(4, 110, 16)]
    # generate_map(15, 16, 78, 16, products)
    pass