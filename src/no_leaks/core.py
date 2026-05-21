"""
Core service: runs the validator and reports results.
"""
import sys
from no_leaks.validator import validate


def run_scan(files: list[str]) -> None:
    is_valid = validate(files)

    if not is_valid:
        print("Potential secret detected. Commit blocked.")
        print("Fix the issue, then try again.")
        sys.exit(1)

    print("No secrets found. Proceeding.")
    sys.exit(0)
