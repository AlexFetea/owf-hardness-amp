import time

import numpy as np
from src.weak_owf import weak_owf, random_permutation
from src.hardness_amp import create_expander_graph, direct_product_construction, expander_construction, generate_random_inputs

n = 10
q = 10
inputs = generate_random_inputs(n, q)

result = direct_product_construction(weak_owf, inputs)

print("inputs:", inputs)
print("Direct Product Construction output (hex):", result, end='\n\n')

n = 2**4
d = 10
expander = create_expander_graph(n, d)
pi = random_permutation(n)
steps = np.random.randint(0, d, size=10)
input = 0

print(f"input: {input}{''.join(format(step,'x') for step in steps)}")
result = expander_construction(expander, start=input, steps=steps, pi=pi)

print("Random Walk on Expanders Construction output (hex):", result)