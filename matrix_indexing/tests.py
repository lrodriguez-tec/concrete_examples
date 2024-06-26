from concrete import fhe
import numpy as np

matrix = [ [1,2,3,4],
           [4,5,6,3],
           [7,8,9,3]
         ]

@fhe.compiler({"table": "clear", "i": "encrypted"})
def f(table, i):
    return table[i]

inputset = [
        (
            np.random.randint(0, 9, size=(4,)),
            np.random.randint(0, 4, size=())
        ) for _ in range(100)
]

circuit = f.compile(inputset)

i = 2
j = 2

enc_sample = circuit.encrypt( matrix[i], j )
enc_output = circuit.run ( enc_sample )
dec_output = circuit.decrypt( enc_output )

print(matrix)
print(str(i) + ","+ str(j) + ": " + str(dec_output))

