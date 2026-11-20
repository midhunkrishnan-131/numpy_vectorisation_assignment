import numpy as np

tests = [
    ((3, 4), (4,)),
    ((3, 4), (3,)),
    ((3, 1), (1, 4)),
    ((2, 3), (3, 2)),
    ((5,), (5, 1)),
]

for shape_a, shape_b in tests:
    a = np.ones(shape_a)
    b = np.ones(shape_b)
    try:
        result = a + b
        print(f"{shape_a} + {shape_b} -> {result.shape}")
    except ValueError:
        print(f"{shape_a} + {shape_b} -> Broadcasting error")
