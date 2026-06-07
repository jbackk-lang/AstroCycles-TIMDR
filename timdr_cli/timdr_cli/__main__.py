timdr_cli/__main__.py
"""
TIMDR Command Line Interface

Usage:
    timdr run
"""

import sys
from pipeline.run_pipeline import run_pipeline

def main():
    if len(sys.argv) < 2:
        print("TIMDR CLI")
        print("Usage: timdr run")
        return

    command = sys.argv[1]

    if command == "run":
        print("Running TIMDR pipeline...\n")
        summary = run_pipeline()
        print("\nPipeline completed.")
        print("Resonance events:", len(summary["resonance_events"]))
    else:
        print(f"Unknown command: {command}")
        print("Available commands: run")

if __name__ == "__main__":
    main()
