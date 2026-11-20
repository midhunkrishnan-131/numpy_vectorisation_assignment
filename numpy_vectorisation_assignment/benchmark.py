import numpy as np
import time

# Create an array of 1,000,000 floats
arr = np.random.rand(1_000_000)

# 1. Plain Python for loop
start = time.perf_counter()
result_loop = []
for x in arr:
    result_loop.append(x ** 2)
loop_time = time.perf_counter() - start

# 2. List comprehension
start = time.perf_counter()
result_comprehension = [x ** 2 for x in arr]
comprehension_time = time.perf_counter() - start

# 3. NumPy vectorisation
start = time.perf_counter()
result_vectorised = arr ** 2
vectorised_time = time.perf_counter() - start

print(f"Python loop:        {loop_time:.6f} seconds")
print(f"List comprehension: {comprehension_time:.6f} seconds")
print(f"NumPy vectorised:   {vectorised_time:.6f} seconds")

if vectorised_time > 0:
    print(f"Loop speedup: {loop_time / vectorised_time:.2f}x")
    print(
        "Comprehension speedup: "
        f"{comprehension_time / vectorised_time:.2f}x"
    )
else:
    print("Vectorised timing was too small to calculate speedup.")

print("\nWhy vectorisation is faster:")
print("1. NumPy performs element-wise calculations in optimised compiled code.")
print("2. It avoids repeated Python interpreter and per-element list-append overhead.")
print("3. Typed arrays support efficient memory access and avoid Python-float object overhead.")
