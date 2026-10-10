import sys
import json
import os
from utils import run_test_and_time, measure_readability

def rank_solutions(problem_dir: str, sol_a: str, sol_b: str):
    """
    Compares two solutions and outputs a JSON report.
    """
    path_a = os.path.join(problem_dir, sol_a)
    path_b = os.path.join(problem_dir, sol_b)
    test_script = os.path.join(problem_dir, "test_all.py")

    with open(path_a, 'r') as f:
        code_a = f.read()
    with open(path_b, 'r') as f:
        code_b = f.read()

    # Evaluation
    res_a = run_test_and_time(path_a, test_script)
    res_b = run_test_and_time(path_b, test_script)
    
    read_a = measure_readability(code_a)
    read_b = measure_readability(code_b)

    # Decision Logic
    winner = "A"
    reason = "Solution A is superior."

    if not res_a['passed'] and res_b['passed']:
        winner = "B"
        reason = "A failed tests, B passed."
    elif res_a['passed'] and not res_b['passed']:
        winner = "A"
        reason = "B failed tests, A passed."
    elif res_a['passed'] and res_b['passed']:
        # Both passed, check efficiency
        if res_a['time'] < res_b['time'] * 0.8: # At least 20% faster
            winner = "A"
            reason = f"A is significantly faster ({res_a['time']:.4f}s vs {res_b['time']:.4f}s)."
        elif res_b['time'] < res_a['time'] * 0.8:
            winner = "B"
            reason = f"B is significantly faster ({res_b['time']:.4f}s vs {res_a['time']:.4f}s)."
        else:
            # Similar performance, check readability
            if read_a > read_b:
                winner = "A"
                reason = "Similar performance, but A is more readable/idiomatic."
            else:
                winner = "B"
                reason = "Similar performance, but B is more readable/idiomatic."

    report = {
        "winner": winner,
        "rationale": reason,
        "metrics": {
            "A": {"time": res_a['time'], "passed": res_a['passed'], "readability": read_a},
            "B": {"time": res_b['time'], "passed": res_b['passed'], "readability": read_b}
        }
    }

    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python rank.py <problem_dir> <sol_a> <sol_b>")
    else:
        rank_solutions(sys.argv[1], sys.argv[2], sys.argv[3])
