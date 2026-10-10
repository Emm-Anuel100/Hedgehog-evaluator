# Ranking: A > B

## Why?
This is a classic "Big O" trap. 
- **Solution B (Python):** Uses a loop. For $N=10^{18}$, this would never finish in a human lifetime.
- **Solution A (C++):** Uses the arithmetic series formula $N(N+1)/2$, which is **O(1)**.

Even if Solution A was written in Python, the formula would still beat the loop. The evaluator ranks A higher because it correctly identifies the mathematical shortcut necessary for the given constraints.
