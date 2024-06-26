from concrete import fhe
import numpy as np

matrix = [ [1,2,3,4],
           [4,5,6,3],
           [7,8,9,3]
         ]

@fhe.compiler({"matrix": "clear", "i": "encrypted", "j" : "encrypted"})
def f(matrix, i, j):
    return matrix[i][j]

inputset = [
        (
            matrix,
            np.random.randint(0, 3, size=()),
            np.random.randint(0, 3, size=())
        ) for _ in range(100)
]

circuit = f.compile(inputset)

