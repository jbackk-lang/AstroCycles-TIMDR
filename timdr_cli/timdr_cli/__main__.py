"""
TIMDR Command Line Interface

Usage:
    timdr run
    timdr plot
"""

import sys
from pipeline.run_pipeline import run_pipeline
from visualization.ascii_plot import ascii_plot

def main():
    if len(sys.argv) < 2:
        print("TIMDR CLI")
        print("Usage:")
        print("  timdr run")
        print("  timdr plot")
        return

    command = sys.argv[1]

    if command == "run":
        print("Running TIMDR pipeline...\n")
        summary = run_pipeline()
        print("\nPipeline completed.")
        print("Resonance events:", len(summary["resonance_events"]))

    elif command == "plot":
        print("Generating ASCII resonance plot...\n")
        summary = run_pipeline()
        events = summary["resonance_events"]
        print(ascii_plot(events, total_steps=200))

    else:
        print(f"Unknown command: {command}")
        print("Available commands: run, plot")

if __name__ == "__main__":
    main()
