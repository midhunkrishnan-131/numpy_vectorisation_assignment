import numpy as np


def normalise(arr):
    """Scale values to the 0-1 range."""
    arr = np.asarray(arr, dtype=float)
    minimum = np.min(arr)
    maximum = np.max(arr)

    if maximum == minimum:
        return np.zeros_like(arr)

    return (arr - minimum) / (maximum - minimum)


def standardise(arr):
    """Return z-scores using population standard deviation."""
    arr = np.asarray(arr, dtype=float)
    mean = np.mean(arr)
    std = np.std(arr)

    if std == 0:
        return np.zeros_like(arr)

    return (arr - mean) / std


def replace_outliers(arr, n):
    """Replace values more than n standard deviations from the mean."""
    arr = np.asarray(arr, dtype=float)
    mean = np.mean(arr)
    std = np.std(arr)
    mask = np.abs(arr - mean) > n * std
    return np.where(mask, mean, arr)


def top_k_indices(arr, k):
    """Return indices of the k largest values, largest first."""
    arr = np.asarray(arr)

    if arr.ndim != 1:
        raise ValueError("arr must be one-dimensional")
    if k < 0 or k > arr.size:
        raise ValueError("k must be between 0 and array size")

    return np.argsort(arr)[-k:][::-1] if k else np.array([], dtype=int)


def moving_average(arr, w):
    """Return the valid w-element moving average."""
    arr = np.asarray(arr, dtype=float)

    if arr.ndim != 1:
        raise ValueError("arr must be one-dimensional")
    if w < 1 or w > arr.size:
        raise ValueError("w must be between 1 and array size")

    return np.convolve(arr, np.ones(w) / w, mode="valid")
