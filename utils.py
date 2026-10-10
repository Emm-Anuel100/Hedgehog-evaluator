import time
import subprocess
import os
from typing import Dict, Any

def run_test_and_time(file_path: str, test_script: str) -> Dict[str, Any]:
    """
    Executes a solution file against a test script and measures time.
    """
    start_time = time.perf_counter()
    
    # We use a subprocess to ensure one solution doesn't crash the evaluator
    try:
        result = subprocess.run(
            ["pytest", test_script],
            capture_output=True,
            text=True,
            timeout=10
        )
        passed = (result.returncode == 0)
    except subprocess.TimeoutExpired:
        passed = False
        result = "Timeout"
    except Exception as e:
        passed = False
        result = str(e)
        
    end_time = time.perf_counter()
    
    return {
        "passed": passed,
        "time": end_time - start_time,
        "output": result.stdout if hasattr(result, 'stdout') else str(result)
    }

def measure_readability(content: str) -> int:
    """
    A simple heuristic for readability.
    Checks for docstrings, type hints, and moderate line lengths.
    """
    score = 0
    if '"""' in content or "'''" in content:
        score += 30
    if "->" in content and ":" in content: # Type hints
        score += 30
    if len(content.split('\n')) < 100: # Not overly bloated
        score += 20
    if "  " in content: # Uses indentation
        score += 20
    return score
