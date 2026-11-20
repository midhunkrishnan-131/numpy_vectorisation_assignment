# NumPy Performance & Vectorisation Assignment

## Files
- `benchmark.py`: compares a Python loop, list comprehension, and NumPy vectorisation on 1,000,000 floats. Run it to get timings for your own computer.
- `part_b_views_copies.py`: demonstrates views versus fancy-indexing copies.
- `part_c_broadcasting.py`: verifies the five broadcasting examples.
- `stats.py`: five vectorised functions with no Python loops.
- `test_stats.py`: simple tests for the functions in `stats.py`.

## Requirements
Install NumPy:
```bash
python -m pip install numpy
```

Run each file:
```bash
python benchmark.py
python part_b_views_copies.py
python part_c_broadcasting.py
python test_stats.py
```

Benchmark results vary by computer. Use the timings printed by `benchmark.py` in your report.
