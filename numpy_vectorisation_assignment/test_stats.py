import numpy as np
from stats import (
    normalise,
    standardise,
    replace_outliers,
    top_k_indices,
    moving_average,
)

arr = np.array([1, 2, 3, 4, 5, 100], dtype=float)

print("Normalised:", normalise(arr))
print("Standardised:", standardise(arr))
print("Outliers replaced:", replace_outliers(arr, 2))
print("Top 3 indices:", top_k_indices(arr, 3))
print("Moving average:", moving_average(arr, 3))
