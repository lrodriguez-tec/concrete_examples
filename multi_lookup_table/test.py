# from concrete import fhe
# import numpy as np

# row1 = fhe.LookupTable([1, 2, 3, 4])
# row2 = fhe.LookupTable([5, 6, 7, 8])
# row3 = fhe.LookupTable([9, 10, 11, 12])
# row4 = fhe.LookupTable([-1, -2, -3, -4])

# table = fhe.LookupTable([row1, row2, row3, row4])
# print(table)

# @fhe.compiler({"x": "encrypted"})
# def f(x):
    # return table[x]

# inputset = [[1,2,3,2], [3,3,1,1], [0,0,1,1]]
# circuit = f.compile(inputset)

# sample = [0,1,3,2]

# actual_output = circuit.encrypt_run_decrypt(np.array(sample))

# print(actual_output)

# # assert np.array_equal(actual_output, expected_output)

from concrete import fhe
import numpy as np

row1 = fhe.LookupTable([1, 2, 3, 4])
row2 = fhe.LookupTable([5, 6, 7, 8])
row3 = fhe.LookupTable([9, 10, 11, 12])

matrix = fhe.LookupTable( [row1, row2, row3] )
print(matrix[ np.array([1]*3) ])

@fhe.compiler({"table": "clear", "i": "encrypted"})
def f(table, i):
    return table[i]

# inputset = [
        # (matrix[0], 1),
        # (matrix[1], 3),
        # (matrix[2], 2),
# ]

# circuit = f.compile(inputset)

# i = 2
# j = 2

# enc_sample = circuit.encrypt( matrix[i], j )
# enc_output = circuit.run ( enc_sample )
# dec_output = circuit.decrypt( enc_output )

# print(matrix)
# print(str(i) + ","+ str(j) + ": " + str(dec_output))
