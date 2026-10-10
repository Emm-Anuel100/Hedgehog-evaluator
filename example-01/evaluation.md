# Ranking: A > B

## Why?
Solution A uses a `set` to achieve **O(n)** time complexity. 
Solution B uses nested loops, resulting in **O(n^2)**.

On a list of 1,000,000 items:
- **Solution A:** ~0.05 seconds.
- **Solution B:** Would take hours.

Additionally, Solution A includes **type hints** and a **docstring**, making it production-ready.
