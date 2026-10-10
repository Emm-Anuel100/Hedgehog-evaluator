# Hedgehog Evaluator

This project demonstrates the ability to build automated tools for code evaluation, ranking, and quality assessment. 

## What this proves
1. **Automated Grading:** Building logic to programmatically verify code correctness against a suite of tests.
2. **Performance Benchmarking:** Implementing timing and resource tracking to compare O(n) vs O(n^2) solutions.
3. **Qualitative Analysis:** Developing heuristics or criteria for "readability" and "idiomatic code."
4. **Ranking Logic:** Aggregating multiple metrics (Correctness, Speed, Style) into a final "Winner" decision with a JSON rationale.

## How it works
- `rank.py`: The core engine that loads two solutions, runs them against a problem's tests, and picks a winner.
- `utils.py`: Contains helpers for sub-process execution and execution time measurement.
- `example-*/`: Real-world scenarios showing the evaluator in action on common algorithmic problems.
"# Hedgehog-evaluator" 
