# Run Guide: Hedgehog Evaluator

This tool ranks two Python solutions based on performance, correctness, and style.

## Setup
```bash
pip install pytest
```

## How to Run
The main entry point is `rank.py`. You pass it a problem directory and two solution filenames.

### Example: Comparing Duplicate Finders
```bash
# Compare O(n) Solution A vs O(n^2) Solution B
python rank.py example-01 solution_A.py solution_B.py
```

### Example: Comparing Summation Strategies
```bash
python rank.py example-02 solution_A.cpp solution_B.py
```

The script will output a JSON object containing the `winner`, `rationale`, and performance `metrics`.
